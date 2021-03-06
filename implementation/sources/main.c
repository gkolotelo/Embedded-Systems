/**
 *
 * File name:           main.c
 * File description:    File containing the main entry point for the system.
 *
 * Authors:             Bruno de Souza Ferreira
 *                      Guilherme Kairalla Kolotelo
 *                      Guilherme Bersi Pereira
 *
 * Creation date:       20Jun2016
 * Revision date:       27Jun2016
 *
 */

/* System includes */
#include "fsl_clock_manager.h"
#include "fsl_port_hal.h"
#include "fsl_gpio_hal.h"

/* Project includes */
#include "hal/target_definitions.h"
#include "hal/mcg/mcg.h"
#include "hal/util/tc_hal.h"
#include "hal/encoder/encoder.h"
#include "hal/driver/driver.h"
#include "hal/controller/controller.h"
#include "hal/hmi/hmi.h"

/* Globals */

/* cyclic executive flag */
volatile unsigned int uiFlagNextPeriod = 0;

/* PID controller globals */
/* HMI will send to host dSensorVelocity, dActuatorValue and dSensorPosition*/
/* HMI will receive from host dReferenceVelocity and dKp, dKi, dKd constants*/
/* Sensor reading variables */
double dSensorVelocity = 0, dSensorPosition = 0;
/* Reference variables */
double dReferenceVelocity = 40;
/* Controller variables */
double dKp = 17, dKi = 1.2, dKd = 0, dMaxSumError = 100, dActuatorValue = 0, dErrorCurrent = 0;
t_PID_Data pidData;

void main_cyclicExecuteIsr(void)
{
    /* Set the cyclic executive flag */
    uiFlagNextPeriod = 1;
}

int boardInit()
{
    mcg_clockInit();
}

int peripheralInit()
{
    /* Configure Red LED and pin for status and timing analysis */
    CLOCK_SYS_EnablePortClock(PORTB_IDX);
    PORT_HAL_SetMuxMode(PORTB, 18, 1);
    PORT_HAL_SetMuxMode(PORTB, 8, 1);
    GPIO_HAL_SetPinDir(GPIOB, 18, kGpioDigitalOutput);
    GPIO_HAL_SetPinDir(GPIOB, 8, kGpioDigitalOutput);

    /* Comm init */
    hmi_initHmi();

    /* Device init */
    encoder_initEncoder();
    driver_initDriver();
    controller_initPID(&pidData);

    /* Cyclic executive init */
    tc_installLptmr0(CYCLIC_EXECUTIVE_PERIOD, main_cyclicExecuteIsr);
}

int main(void)
{
    /* Initialization routines */
    boardInit();
    peripheralInit();

    /* Presets */
    controller_setKp(&pidData, dKp);
    controller_setKi(&pidData, dKi);
    controller_setKd(&pidData, dKd);
    controller_setMaxSumError(&pidData, dMaxSumError);


    for (;;) {
        /* Blink status LED */
        PTB_BASE_PTR->PTOR = 1 << 18;
        /* Set PTB8 for timing analysis */
        PTB_BASE_PTR->PTOR = 1 << 8;;

        /* Measure motor speed and position */
        encoder_takeMeasurement();

        dSensorVelocity = encoder_getAngularVelocityRad();
        dSensorPosition = encoder_getAngularPositionDegree();

        /* Execute PID calculations */
        dActuatorValue = 100*controller_PIDUpdate(&pidData, dSensorVelocity, dReferenceVelocity)/MAX_MOTOR_VELOCITY_RAD;

        /* Drive motor */
        driver_setDriver(dActuatorValue);

        /* Process serial communication */
        hmi_receive();
        hmi_transmit(dSensorVelocity, dSensorPosition, dActuatorValue);

        /* Clear PTB8 for timing analysis */
        PTB_BASE_PTR->PTOR = 1 << 8;

        while(!uiFlagNextPeriod);
        /* Unset the cyclic executive flag */
        uiFlagNextPeriod = 0;

    }

    return 0;
}
////////////////////////////////////////////////////////////////////////////////
// EOF
////////////////////////////////////////////////////////////////////////////////
