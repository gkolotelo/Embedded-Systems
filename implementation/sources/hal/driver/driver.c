/**
 *
 * File name:           driver.c                             
 * File description:    File containing the methods for the operation
 *                      of an H-Bridge in bipolar operation mode.
 *                      
 *                      - Driver actuation through driver_setDriver goes from -100 to 100, the
 *                        former being full reverse, and the latter, full steam ahead.
 *                      - Driver max freq @ 100kHz.
 *                      - Channel A on HighTrue and Channel B on LowTrue makes
 *                        for a bipolar H-Bridge pair of control signals.
 *
 * Authors:             Bruno de Souza Ferreira
 *                      Guilherme Kairalla Kolotelo
 *                      Guilherme Bersi Pereira
 *
 * Creation date:       10Jun2016                                       
 * Revision date:       27Jun2016
 *
 */


/* Project Includes */
#include "driver.h"
#include "hal/target_definitions.h"

/* System Includes */
#include "fsl_tpm_hal.h"
#include "fsl_tpm_driver.h"
#include "fsl_clock_manager.h"
#include "fsl_port_hal.h"
#include "fsl_gpio_hal.h"
#include "fsl_interrupt_manager.h"
#include "fsl_pwm_driver.h"

/* Nominal switching frequency */
/* 25kHz */
#define DRIVER_FREQUENCY            25000
/* Prescaler */
#define DRIVER_PRESCALER            kTpmDividedBy1

/**
 * Method name:         driver_initDriver
 * Method description:  Initializes the driver with the load in idle (50% duty cycle)
 * Input params:        n/a
 * Output params:       n/a
 */
void driver_initDriver()
{
    //Add Error reporting

    /* Configure Pins */
    /* Channel pins */
    CLOCK_SYS_EnablePortClock(DRIVER_CHA_PORT_INSTANCE);
    CLOCK_SYS_EnablePortClock(DRIVER_CHB_PORT_INSTANCE);
    PORT_HAL_SetMuxMode(DRIVER_CHA_PORT_BASE, DRIVER_CHA_PIN_NUMBER, DRIVER_CHA_PORT_ALT);
    PORT_HAL_SetMuxMode(DRIVER_CHB_PORT_BASE, DRIVER_CHB_PIN_NUMBER, DRIVER_CHB_PORT_ALT);

    /* Enable pin */
    CLOCK_SYS_EnablePortClock(DRIVER_EN_PORT_INSTANCE);
    PORT_HAL_SetMuxMode(DRIVER_EN_PORT_BASE, DRIVER_EN_PIN_NUMBER, DRIVER_EN_PORT_ALT);
    GPIO_HAL_SetPinDir(DRIVER_EN_GPIO_BASE, DRIVER_EN_PIN_NUMBER, DRIVER_EN_PIN_DIR);
    GPIO_HAL_ClearPinOutput(DRIVER_EN_GPIO_BASE, DRIVER_EN_PIN_NUMBER);

    /* Configure TPM module */
    /* Using 8MHz external clock source */
    CLOCK_SYS_SetTpmSrc(DRIVER_TPM_INSTANCE, kClockTpmSrcOsc0erClk);

    /* Will be using USB serial over OpenSDA, must enable Debug Mode */
    tpm_general_config_t config =
    {
            .isDBGMode = true
    };

    TPM_DRV_Init(DRIVER_TPM_INSTANCE, &config);
    TPM_DRV_SetClock(DRIVER_TPM_INSTANCE, kTpmClockSourceModuleClk, DRIVER_PRESCALER);

    /* Configure PWM channels. 50% duty cycle is idle, since the driver is bipolar */
    tpm_pwm_param_t pwmA =
        {
                .mode = kTpmEdgeAlignedPWM,
                .edgeMode = kTpmHighTrue, /* High true, on when channel B is off */
                .uFrequencyHZ = DRIVER_FREQUENCY,
                .uDutyCyclePercent = 50,

        };
    tpm_pwm_param_t pwmB =
    {
            .mode = kTpmEdgeAlignedPWM,
            .edgeMode = kTpmLowTrue, /* Low true, on when channel A is off*/
            .uFrequencyHZ = DRIVER_FREQUENCY,
            .uDutyCyclePercent = 50,

    };

    TPM_DRV_PwmStart(DRIVER_TPM_INSTANCE, &pwmA, DRIVER_CHA_INSTANCE);
    TPM_DRV_PwmStart(DRIVER_TPM_INSTANCE, &pwmB, DRIVER_CHB_INSTANCE);

    driver_enableDriver();

}

/**
 * Method name:         driver_disableDriver
 * Method description:  Disables the driver by clearing the enable pin
 * Input params:        n/a
 * Output params:       n/a
 */
void driver_disableDriver()
{
    GPIO_HAL_ClearPinOutput(DRIVER_EN_GPIO_BASE, DRIVER_EN_PIN_NUMBER);
}

/**
 * Method name:         driver_enableDriver
 * Method description:  Enables the driver by setting the enable pin
 * Input params:        n/a
 * Output params:       n/a
 */
void driver_enableDriver()
{
    GPIO_HAL_SetPinOutput(DRIVER_EN_GPIO_BASE, DRIVER_EN_PIN_NUMBER);
}

/**
 * Method name:         driver_setChannelADutyCycle
 * Method description:  Sets duty cycle for Channel A only
 * Input params:        uiDutyCyclePercent = Duty cycle in percentage
 * Output params:       n/a
 */
void driver_setChannelADutyCycle(int uiDutyCyclePercent)
{
    TPM_HAL_SetChnCountVal(DRIVER_TPM_BASE, DRIVER_CHA_INSTANCE, ((TPM_HAL_GetMod(DRIVER_TPM_BASE)*uiDutyCyclePercent)/100));
}

/**
 * Method name:         driver_setChannelBDutyCycle
 * Method description:  Sets duty cycle for Channel B only
 * Input params:        uiDutyCyclePercent = Duty cycle in percentage
 * Output params:       n/a
 */
void driver_setChannelBDutyCycle(int uiDutyCyclePercent)
{
    TPM_HAL_SetChnCountVal(DRIVER_TPM_BASE, DRIVER_CHB_INSTANCE, ((TPM_HAL_GetMod(DRIVER_TPM_BASE)*uiDutyCyclePercent)/100));
}

/**
 * Method name:         driver_setHBridgeDutyCycle
 * Method description:  Sets duty cycle for H-Bridge operation. Both ChA and ChB
 * Input params:        uiDutyCyclePercent = Duty cycle in percentage (0% is full reverse, 100% is full ahead)
 * Output params:       n/a
 */
void driver_setHBridgeDutyCycle(int uiDutyCyclePercent)
{
    uint32_t uichannelCnV = (TPM_HAL_GetMod(DRIVER_TPM_BASE)*uiDutyCyclePercent)/100;
    TPM_HAL_SetChnCountVal(DRIVER_TPM_BASE, DRIVER_CHA_INSTANCE, uichannelCnV);
    TPM_HAL_SetChnCountVal(DRIVER_TPM_BASE, DRIVER_CHB_INSTANCE, uichannelCnV);
}

/**
 * Method name:         driver_setDriver
 * Method description:  Sets the driver from -100 to 100, the former being full reverse, and the latter, full steam ahead.
 * Input params:        input = -100 to 100
 * Output params:       n/a
 */
void driver_setDriver(int input)
{
    /* Cap out-of-bound input */
    if(input < -100)
        input = -100;
    if(input > 100)
        input = 100;
    input = (input + 100)/2;
    driver_setHBridgeDutyCycle(input);
}
