/* ***************************************************************** */
/* File name:        es670_peripheral_board.h                        */
/* File description: Header file containing the peripherals mapping  */
/*                     of the peripheral board for the ES670 hardware*/
/* Author name:      dloubach                                        */
/* Modified by:      Guilherme Kairalla Kolotelo                     */
/*                   Kaique Arce de Almeida Camargo                  */
/* Creation date:    16Oct2015                                       */
/* Revision date:    20May2016                                       */
/* ***************************************************************** */

#ifndef SOURCES_ES670_PERIPHERAL_BOARD_H_
#define SOURCES_ES670_PERIPHERAL_BOARD_H_

/* system includes */
#include <MKL25Z4.h>

/*                 General uC definitions                 */

/* Clock gate control */
#define  CGC_CLOCK_DISABLED         0x00U
#define  CGC_CLOCK_ENABLED          0x01U

/* GPIO input / output */
#define GPIO_INPUT                  0x00U
#define GPIO_OUTPUT                 0x01U


/*                 END OF General uC definitions         */


/*                 BUZZER Definitions                    */
#define BUZZER_PORT_BASE_PNT        PORTD                                   /* peripheral port base pointer */
#define BUZZER_GPIO_BASE_PNT        PTD                                     /* peripheral gpio base pointer */

#define BUZZER_PIN                  1U                                      /* buzzer pin */
#define BUZZER_DIR                  kGpioDigitalOutput
#define BUZZER_ALT                  0x01u
/*                 END OF BUZZER definitions             */


/*                 LED and SWITCH Definitions                    */
#define LS_PORT_BASE_PNT            PORTA                                   /* peripheral port base pointer */
#define LS_GPIO_BASE_PNT            PTA                                     /* peripheral gpio base pointer */

/* THIS PIN CONFLICTS WITH PTA1 USED AS UART0_RX IN THE OPENSDA SERIAL DEBUG PORT */
#define LS1_PIN                     1U                                      /* led/switch #1 pin */
#define LS1_DIR_OUTPUT              (GPIO_OUTPUT << LS1_PIN)
#define LS1_DIR_INPUT               (GPIO_OUTPUT << LS1_PIN)
#define LS1_ALT                     0x01u                                   /* GPIO alternative */

/* THIS PIN CONFLICTS WITH PTA2 USED AS UART0_TX IN THE OPENSDA SERIAL DEBUG PORT */
#define LS2_PIN                     2U                                      /* led/switch #2 pin */
#define LS2_DIR_OUTPUT              (GPIO_OUTPUT << LS2_PIN)
#define LS2_DIR_INPUT               (GPIO_OUTPUT << LS2_PIN)
#define LS2_ALT                     LS1_ALT

#define LS3_PIN                     4U                                      /* led/switch #3 pin */
#define LS3_DIR_OUTPUT              (GPIO_OUTPUT << LS3_PIN)
#define LS3_DIR_INPUT               (GPIO_OUTPUT << LS3_PIN)
#define LS3_ALT                     LS1_ALT

#define LS4_PIN                     5U                                      /* led/switch #4 pin */
#define LS4_DIR_OUTPUT              (GPIO_OUTPUT << LS4_PIN)
#define LS4_DIR_INPUT               (GPIO_OUTPUT << LS4_PIN)
#define LS4_ALT                     LS1_ALT

/*                 END OF LED and SWITCH definitions             */

/*                  7 Segment Display definitions                */

#define DS1_EN_PIN                      0x01u << 13u
#define DS2_EN_PIN                      0x01u << 12u
#define DS3_EN_PIN                      0x01u << 11u
#define DS4_EN_PIN                      0x01u << 10u

#define D7S_DIR                         0x3CFFu
#define D7S_ALT                         0x01u

/*              END OF 7 Segment Display definitions             */

/*                 LCD definitions                 */

/* LCD Register Selector
 * Used as register selector input
 * When (LCD_RS = LCD_RS_HIGH) => DATA register is selected
 * When (LCD_RS = LCD_RS_LOW)  => INSTRUCTION register is selected
*/
#define LCD_PORT_BASE_PNT           PORTC                                   /* peripheral port base pointer */
#define LCD_GPIO_BASE_PNT           PTC                                     /* peripheral gpio base pointer */

#define LCD_RS_PIN                  8U                                      /* register selector */
#define LCD_RS_DIR                  0x01 << 8
#define LCD_RS_ALT                  0x01

#define LCD_ENABLE_PIN              9U                                      /* enable pin */
#define LCD_ENABLE_DIR              0x01 << 9
#define LCD_ENABLE_ALT              0x01

#define LCD_RS_HIGH                 1U
#define LCD_RS_DATA                 LCD_RS_HIGH

#define LCD_RS_LOW                  0U
#define LCD_RS_CMD                  LCD_RS_LOW

#define LCD_ENABLED                 1U
#define LCD_DISABLED                0U

#define LCD_DATA_DIR_IO             0x01                                    /* LCD data pins */
#define LCD_DATA_DIR_MSK            0xFF                                    /* LCD data pins */
#define LCD_DATA_DIR                LCD_DATA_DIR_IO & LCD_DATA_DIR_MSK
#define LCD_DATA_ALT                0x01

#define LCD_DATA_PIN0               0U
#define LCD_DATA_PIN1               1U
#define LCD_DATA_PIN2               2U
#define LCD_DATA_PIN3               3U
#define LCD_DATA_PIN4               4U
#define LCD_DATA_PIN5               5U
#define LCD_DATA_PIN6               6U
#define LCD_DATA_PIN7               7U
/*                 END OF LCD definitions                 */

/*                 COOLER DEFINITIONS                     */
#define COOLER_PIN 					13U
#define COOLER_DIR					0X01
#define COOLER_MUX					0X01
/*             END OF COOLER DEFINITIONS                  */

/*                  TACH DEFINITIONS                      */
#define TACH_PIN 					29U
#define TACH_ALT					4U
#define TACH_CLK_SRC 				2U

/*              END OF TACH DEFINITIONS                   */

#endif /* SOURCES_ES670_PERIPHERAL_BOARD_H_ */
