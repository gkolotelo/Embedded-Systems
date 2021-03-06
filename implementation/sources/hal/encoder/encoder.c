/**
 *
 * File name:           encoder.c                            
 * File description:    File containing the methods for the reading
 *                      of an incremental, 3-pin, encoder.
 *                      
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
#include "encoder.h"
#include "hal/target_definitions.h"

/* System Includes */
#include "fsl_tpm_hal.h"
#include "fsl_tpm_driver.h"
#include "fsl_clock_manager.h"
#include "fsl_port_hal.h"
#include "fsl_gpio_hal.h"
#include "fsl_interrupt_manager.h"

/* Defines */
/* Maximum number of pulses to be counted in the defined acquisition period before resetting */
#define ENCODER_MAX_PULSE_COUNT     0xFFFF
/* Encoder pulse count */
#define ENCODER_PULSE_COUNT         1024
/* Acquisition period, should be same as cyclic executive period */
#define ENCODER_ACQ_PERIOD_MS       CYCLIC_EXECUTIVE_PERIOD

/* Global variables: */
/* Measured pulses per second */
uint32_t uiEncoderPulsesPerSecond = 0;
/* Orientation of quadrature, -1 or 1 */
int iEncoderDirection = 0;
/* Angular position, in pulses */
uint32_t uiEncoderPosition = 0;

/*
 * For ENCODER_ACQ_PERIOD_MS = 10ms: 368 pulses @ 2100RPM; 33 pulses @ 3.2RPM
 * for ENCODER_ACQ_PERIOD_MS = 28ms: 1004 pulses@ 2100RPM; 91 pulses @ 3.2RPM
 */

/**
 * Method name:         ENCODER_CHO_IRQ_HANDLER
 * Method description:  Channel O IRQ handler
 * Input params:        n/a
 * Output params:       n/a
 */
extern void ENCODER_CHO_IRQ_HANDLER()
{
    PORT_HAL_ClearPinIntFlag(PORTD, 0);
    uiEncoderPosition = 0;
}

/**
 * Method name:         encoder_initEncoder
 * Method description:  Initializes the encoder for an incremental 3-pin encoder
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_initEncoder()
{

    /* Configure Channel PORTs */
    CLOCK_SYS_EnablePortClock(ENCODER_CHA_PORT_INSTANCE);
    CLOCK_SYS_EnablePortClock(ENCODER_CHB_PORT_INSTANCE);
    PORT_HAL_SetMuxMode(ENCODER_CHA_PORT_BASE, ENCODER_CHA_PIN_NUMBER, ENCODER_CHA_PORT_ALT);
    PORT_HAL_SetMuxMode(ENCODER_CHB_PORT_BASE, ENCODER_CHB_PIN_NUMBER, ENCODER_CHB_PORT_ALT);

    /* Configure external clock source for TPM modules */
    SIM_HAL_SetTpmExternalClkPinSelMode(SIM, ENCODER_CHA_TPM_INSTANCE, ENCODER_CHA_FTM_CLKIN);
    SIM_HAL_SetTpmExternalClkPinSelMode(SIM, ENCODER_CHB_TPM_INSTANCE, ENCODER_CHB_FTM_CLKIN);

    /* Will be using USB serial over OpenSDA, must enable Debug Mode */
    tpm_general_config_t config=
    {
            .isDBGMode = true
    };
    TPM_DRV_Init(ENCODER_CHA_TPM_INSTANCE, &config);
    TPM_DRV_Init(ENCODER_CHB_TPM_INSTANCE, &config);

    TPM_HAL_SetClockDiv(ENCODER_CHA_TPM_BASE, kTpmDividedBy1);
    TPM_HAL_SetClockDiv(ENCODER_CHB_TPM_BASE, kTpmDividedBy1);

    TPM_HAL_SetMod(ENCODER_CHA_TPM_BASE, ENCODER_MAX_PULSE_COUNT);
    TPM_HAL_SetMod(ENCODER_CHB_TPM_BASE, ENCODER_MAX_PULSE_COUNT);

    TPM_HAL_ClearCounter(ENCODER_CHA_TPM_BASE);
    TPM_HAL_ClearCounter(ENCODER_CHB_TPM_BASE);

    /* Set TPM clock to external for both channels */
    TPM_HAL_SetClockMode(ENCODER_CHA_TPM_BASE, kTpmClockSourceExternalClk);
    TPM_HAL_SetClockMode(ENCODER_CHB_TPM_BASE, kTpmClockSourceExternalClk);

    /* Set up and enable Channel O interrupt */
    CLOCK_SYS_EnablePortClock(ENCODER_CHO_PORT_INSTANCE);
    PORT_HAL_SetMuxMode(ENCODER_CHO_PORT_BASE, ENCODER_CHO_PIN_NUMBER, kPortMuxAsGpio);
    PORT_HAL_SetPinIntMode(ENCODER_CHO_PORT_BASE, ENCODER_CHO_PIN_NUMBER, kPortIntRisingEdge);
    NVIC_EnableIRQ(ENCODER_CHO_IRQn);


}

/**
 * Method name:         encoder_enableCounter
 * Method description:  Enables the counter
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_enableCounter()
{
    TPM_HAL_SetClockMode(ENCODER_CHA_TPM_BASE, kTpmClockSourceExternalClk);
    TPM_HAL_SetClockMode(ENCODER_CHB_TPM_BASE, kTpmClockSourceExternalClk);
}

/**
 * Method name:         encoder_disableCounter
 * Method description:  Disables the counter
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_disableCounter()
{
    TPM_HAL_SetClockMode(ENCODER_CHA_TPM_BASE, kTpmClockSourceNoneClk);
    TPM_HAL_SetClockMode(ENCODER_CHB_TPM_BASE, kTpmClockSourceNoneClk);
    encoder_resetCounter();
}

/**
 * Method name:         encoder_resetCounter
 * Method description:  Resets the counter
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_resetCounter()
{
    TPM_HAL_ClearCounter(ENCODER_CHA_TPM_BASE);
    TPM_HAL_ClearCounter(ENCODER_CHB_TPM_BASE);
}

/**
 * Method name:         encoder_enableChOInterrupt
 * Method description:  Enables the interrupt on Channel O
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_enableChOInterrupt()
{
    NVIC_EnableIRQ(ENCODER_CHO_IRQn);
}

/**
 * Method name:         encoder_disableChOInterrupt
 * Method description:  Disables the interrupt on channel O
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_disableChOInterrupt()
{
    NVIC_DisableIRQ(ENCODER_CHO_IRQn);
}

/**
 * Method name:         encoder_takeMeasurement
 * Method description:  Takes a measurement of speed, direction and position
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_takeMeasurement()
{
    uiEncoderPulsesPerSecond = (1000*TPM_HAL_GetCounterVal(ENCODER_CHA_TPM_BASE))/ENCODER_ACQ_PERIOD_MS;
    iEncoderDirection = TPM_HAL_GetCounterVal(ENCODER_CHA_TPM_BASE) > TPM_HAL_GetCounterVal(ENCODER_CHB_TPM_BASE) ? 1 : -1;
    uiEncoderPosition += TPM_HAL_GetCounterVal(ENCODER_CHA_TPM_BASE);
    encoder_resetCounter();
}


/* Data retrieval methods */

/**
 * Method name:         encoder_getAngularPositionDegree
 * Method description:  Returns the angular position of the encoder in degrees
 * Input params:        n/a
 * Output params:       double = Angular position of the encoder in degrees
 */
double encoder_getAngularPositionDegree()
{
    return 360*((double)uiEncoderPosition/ENCODER_PULSE_COUNT);
}

/**
 * Method name:         encoder_getAngularPositionRad
 * Method description:  Returns the angular position of the encoder in radians
 * Input params:        n/a
 * Output params:       double = Angular position of the encoder in radians
 */
double encoder_getAngularPositionRad()
{
    return CONST_2PI*((double)uiEncoderPosition/ENCODER_PULSE_COUNT);
}

/**
 * Method name:         encoder_getAngularVelocity
 * Method description:  Returns the angular velocity of the encoder in pulses per second
 * Input params:        n/a
 * Output params:       double = Angular velocity of the encoder in pps
 */
double encoder_getAngularVelocity()
{
    return (double)uiEncoderPulsesPerSecond;
}

/**
 * Method name:         encoder_getAngularVelocityRadPerSec
 * Method description:  Returns the angular velocity of the encoder in Rad/s
 * Input params:        n/a
 * Output params:       double = Angular velocity of the encoder in Rad/s
 */
double encoder_getAngularVelocityRad()
{
    return CONST_2PI*((double)uiEncoderPulsesPerSecond/ENCODER_PULSE_COUNT);
}

/**
 * Method name:         encoder_getAngularVelocityRPM
 * Method description:  Returns the angular velocity of the encoder in RPM
 * Input params:        n/a
 * Output params:       double = Angular velocity of the encoder in RPM
 */
double encoder_getAngularVelocityRPM()
{
    return 60*((double)uiEncoderPulsesPerSecond/ENCODER_PULSE_COUNT);
}

/**
 * Method name:         encoder_getDirection
 * Method description:  Returns the direction the encoder is spinning
 * Input params:        n/a
 * Output params:       int = Direction (-1 or 1)
 */
int encoder_getDirection()
{
    return iEncoderDirection;
}








