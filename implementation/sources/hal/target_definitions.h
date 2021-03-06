/**
 *
 * File name:           target_definitions.h
 * File description:    File containing the methods implementing
 *                      a PID controller.
 *
 * Authors:             Bruno de Souza Ferreira
 *                      Guilherme Kairalla Kolotelo
 *                      Guilherme Bersi Pereira
 *
 * Creation date:       25Jun2016
 * Revision date:       25Jun2016
 *
 */

#ifndef SOURCES_TARGET_PINS_H_
#define SOURCES_TARGET_PINS_H_

/* system includes */
#include <MKL25Z4.h>

/*                    General uC Definitions             */
/* GPIO input / output */
#define GPIO_INPUT                  0x00U
#define GPIO_OUTPUT                 0x01U

/* Project specific definitions */
#define CONST_2PI                   2 * 3.14159
#define MAX_MOTOR_VELOCITY_RAD      2100*CONST_2PI/60

/* Cyclic executive period in microseconds */
/* 20ms */
#define CYCLIC_EXECUTIVE_PERIOD         20 * 1000



/*                 END OF General uC Definitions         */





/*                     Driver Definitions                */
/* TPM module */
#define DRIVER_TPM_INSTANCE         TPM0_IDX
#define DRIVER_TPM_BASE             TPM0
/* ChA:     PTC1(J10 12) */
#define DRIVER_CHA_PORT_INSTANCE    PORTC_IDX
#define DRIVER_CHA_PORT_BASE        PORTC
#define DRIVER_CHA_PORT_ALT         4U
#define DRIVER_CHA_PIN_NUMBER       1U
#define DRIVER_CHA_INSTANCE         0U
/* ChB:     PTC2(J10 10) */
#define DRIVER_CHB_PORT_INSTANCE    PORTC_IDX
#define DRIVER_CHB_PORT_BASE        PORTC
#define DRIVER_CHB_PORT_ALT         4U
#define DRIVER_CHB_PIN_NUMBER       2U
#define DRIVER_CHB_INSTANCE         1U
/* Enable:  PTE30(J10 11) */
#define DRIVER_EN_PORT_INSTANCE     PORTE_IDX
#define DRIVER_EN_PORT_BASE         PORTE
#define DRIVER_EN_GPIO_BASE         GPIOE
#define DRIVER_EN_PORT_ALT          1U
#define DRIVER_EN_PIN_DIR           GPIO_OUTPUT
#define DRIVER_EN_PIN_NUMBER        30U
/*                  END OF Driver Definitions            */


/*                     Encoder Definitions               */
/* ChA: PTC12(J2 01) @ FTM_CLKIN0, TPM1 for encoder pin A */
#define ENCODER_CHA_PORT_INSTANCE       PORTC_IDX
#define ENCODER_CHA_PORT_BASE           PORTC
#define ENCODER_CHA_PORT_ALT            4U
#define ENCODER_CHA_PIN_NUMBER          12U         // Interrupt enabled on TPM2
#define ENCODER_CHA_TPM_INSTANCE        TPM2_IDX
#define ENCODER_CHA_TPM_BASE            TPM2
#define ENCODER_CHA_FTM_CLKIN           0U
/* ChB:  PTC13(J2 03) @ FTM_CLKIN1, TPM2 for encoder pin B */
#define ENCODER_CHB_PORT_INSTANCE       PORTC_IDX
#define ENCODER_CHB_PORT_BASE           PORTC
#define ENCODER_CHB_PORT_ALT            4U
#define ENCODER_CHB_PIN_NUMBER          13U
#define ENCODER_CHB_TPM_INSTANCE        TPM1_IDX
#define ENCODER_CHB_TPM_BASE            TPM1
#define ENCODER_CHB_FTM_CLKIN           1U
/* ChO:  PTD0(J2 06) interrupt pin */
#define ENCODER_CHO_PORT_INSTANCE       PORTD_IDX
#define ENCODER_CHO_PORT_BASE           PORTD
#define ENCODER_CHO_PIN_NUMBER          0U

/* Interrupt definitions */
#define ENCODER_CHA_IRQ_HANDLER         TPM2_IRQHandler
#define ENCODER_CHA_IRQN                TPM2_IRQn
#define ENCODER_CHO_IRQ_HANDLER         PORTD_IRQHandler
#define ENCODER_CHO_IRQn                PORTD_IRQn

/*                  END OF Encoder Definitions           */

/*                      HMI Definitions                  */
#define HMI_UART_PORT_INSTANCE      PORTA_IDX
#define HMI_UART_PORT_BASE          PORTA
#define HMI_UART_PIN_RX             1
#define HMI_UART_PIN_TX             2
#define HMI_UART_PIN_ALT            2
#define HMI_UART_INSTANCE           UART0_IDX
#define HMI_UART_BASE               UART0
#define HMI_UART_BAUD               115200

/*                   END OF HMI Definitions              */



#endif /* SOURCES_TARGET_PINS_H_*/
