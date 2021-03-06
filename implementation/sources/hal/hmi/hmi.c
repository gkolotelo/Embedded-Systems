/**
 *
 * File name:           hmi.c
 * File description:    File containing the methods for interaction with
 *                      a host device via a serial connection.
 *
 * Authors:             Bruno de Souza Ferreira
 *                      Guilherme Kairalla Kolotelo
 *                      Guilherme Bersi Pereira
 *
 * Creation date:       25Jun2016
 * Revision date:       27Jun2016
 *
 */



/* System includes */
#include "fsl_clock_manager.h"
#include "fsl_port_hal.h"
#include "fsl_smc_hal.h"
#include "fsl_debug_console.h"

/* Project includes */
#include "hal/target_definitions.h"
#include "hmi.h"
#include "hal/controller/controller.h"


extern double dReferenceVelocity, dReferenceDirection;
extern t_PID_Data pidData;

/**
 * Method name:         hmi_initHmi
 * Method description:  Initializes UART0 for debug mode for serial over USB, provided by OpenSDA.
 * Input params:        n/a
 * Output params:       n/a
 */
void hmi_initHmi()
{
    /* LPSCI0 */
    CLOCK_SYS_EnablePortClock(HMI_UART_PORT_INSTANCE);
    /* UART0_RX */
    PORT_HAL_SetMuxMode(HMI_UART_PORT_BASE, HMI_UART_PIN_RX, HMI_UART_PIN_ALT);
    /* UART0_TX */
    PORT_HAL_SetMuxMode(HMI_UART_PORT_BASE, HMI_UART_PIN_TX, HMI_UART_PIN_ALT);

    /* Select different clock source for LPSCI */
    CLOCK_SYS_SetLpsciSrc(HMI_UART_INSTANCE, kClockLpsciSrcPllFllSel);

    /* Initialize the debug console */
    DbgConsole_Init(HMI_UART_INSTANCE, HMI_UART_BAUD, kDebugConsoleLPSCI);
}

/**
 * Method name:         hmi_receive
 * Method description:  Receives and interprets data sent from the host device.
 * Input params:        n/a
 * Output params:       n/a
 */
void hmi_receive()
{
    /* Check if there are characters on buffer */
    if(0 == UART0_BRD_S1_RDRF(HMI_UART_BASE)) return;
    char uiReceiveCommand;
    int iReceiveNumber;
    SCANF("%c%d", &uiReceiveCommand, &iReceiveNumber);
    //PRINTF("Received: %c%d\r\n", uiReceiveCommand, iReceiveNumber);
    switch(uiReceiveCommand)
    {
        case 'P':
        case 'p':
            iReceiveNumber = abs(iReceiveNumber);
            controller_setKp(&pidData, ((double)iReceiveNumber/10000));
            break;
        case 'I':
        case 'i':
            iReceiveNumber = abs(iReceiveNumber);
            controller_setKi(&pidData, ((double)iReceiveNumber/10000));
            break;
        case 'D':
        case 'd':
            iReceiveNumber = abs(iReceiveNumber);
            controller_setKd(&pidData, ((double)iReceiveNumber/10000));
            break;
        case 'V':
        case 'v':
            iReceiveNumber = abs(iReceiveNumber);
            dReferenceVelocity = iReceiveNumber;
            break;
        default:
            break;
    }
}

/**
 * Method name:         hmi_transmit
 * Method description:  Transmits required data to the host device. Uses space as separator
 * Input params:        dVelocity: Velocity reading from encoder
 *                      dPosition: Position reading from encoder
 *                      dActuator: Actuator value from controller
 * Output params:       n/a
 */
void hmi_transmit(double dVelocity, double dPosition, double dActuator)
{
    PRINTF("%f %f %f\r\n", dVelocity, dPosition, dActuator);
}
