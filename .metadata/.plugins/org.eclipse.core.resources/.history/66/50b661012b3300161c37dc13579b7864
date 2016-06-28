/**
 *
 * File name:        	interpreter.c                             
 * File description: 	file containing the methods for interacting
 * 						with a serial host  
 *                    
 * Authors:          	Guilherme Kairalla Kolotelo                     
 * 		             	Kaique Arce de Almeida Camargo                  
 * Creation date:    	22Apr2016                                       
 * Revision date:    	29Apr2016
 *
 */

#include "interpreter.h"
#include "hal/display_7segments/display_7segments.h"
#include "hal/buzzer/buzzer.h"
#include "hal/ledswi/ledswi.h"
#include "fsl_debug_console.h"
#include "fsl_device_registers.h"
#include "hal/uart/debugUart.h"


/**
 * Method name:			interpreter_init
 * Method description:  Initializes UART port.
 * Input params:      	n/a
 * Output params:     	n/a
 */
void interpreter_init()
{
	debugUart_init();
}


/**
 * Method name:			sendACK
 * Method description: 	Writes acknowledgment, error and message bytes to UART
 * Input params:      	char cRetVal = an optional extra byte to be written                        
 * Output params:     	n/a                        
 */
void sendACK(char cRetVal)
{
	char cRetStr[7] = "\r\nACK\r\n";
	if(cRetVal == ERROR)
	{
		cRetStr[2] ='E';
		cRetStr[3] ='R';
		cRetStr[4] ='R';
	}
	PUTCHAR(cRetStr[0]);
	PUTCHAR(cRetStr[1]);
	PUTCHAR(cRetStr[2]);
	PUTCHAR(cRetStr[3]);
	PUTCHAR(cRetStr[4]);
	if(cRetVal != NONE && cRetVal != ERROR)
		PUTCHAR(cRetVal);
	PUTCHAR(cRetStr[5]);
	PUTCHAR(cRetStr[6]);
}



/**
 * Method name:			interpreter_ledCommand
 * Method description: 	Executes commands pertinent to led operation.
 * Input params:      	n/a                      
 * Output params:     	char = error code.                       
 */
char interpreter_ledCommand()
{
	uint8_t uiCommand, uiLedPos;
	status_type_e eStatus;
	while (UART0_BRD_S1_RDRF(UART0) == 0);
	uiCommand = GETCHAR();
	PUTCHAR(uiCommand);
	if(uiCommand >= 49 && uiCommand <= 52) // Leds 1 through 4
	{
		uiCommand = uiCommand - 48;
		ledswi_initLedSwitch(uiCommand,4-uiCommand);
		eStatus = ledswi_getLedStatus(uiCommand);
		if(eStatus == OFF) return 'L';
		if(eStatus == ON) return 'H';
		return ERROR;
	}
	if(uiCommand != 'c' && uiCommand != 'C' && uiCommand != 's' && uiCommand != 'S')
		return ERROR;
	while (UART0_BRD_S1_RDRF(UART0) == 0);
	uiLedPos = GETCHAR();
	PUTCHAR(uiLedPos);
	if(uiLedPos < 49 || uiLedPos > 52) // Leds 1 through 4
		return ERROR;
	uiLedPos = uiLedPos - 48;
	ledswi_initLedSwitch(uiLedPos,4-uiLedPos);
	switch(uiCommand)
	{
		case 'c':
		case 'C':
			ledswi_clearLed(uiLedPos);
			return NONE;

		case 's':
		case 'S':
			ledswi_setLed(uiLedPos);
			return NONE;

		default:
			return ERROR;
	}
}


/**
 * Method name:			interpreter_switchCommand
 * Method description: 	Executes commands pertinent to switch operation.
 * Input params:      	n/a                      
 * Output params:     	char = error code.                       
 */
char interpreter_switchCommand()
{
	uint8_t uiSwPos;
	status_type_e eStatus;
	while (UART0_BRD_S1_RDRF(UART0) == 0);
	uiSwPos = GETCHAR();
	PUTCHAR(uiSwPos);
	if(uiSwPos < 49 || uiSwPos > 52) // Switches 1 through 4
		return ERROR;
	uiSwPos = uiSwPos - 48;
	ledswi_initLedSwitch(4-uiSwPos,uiSwPos);
	eStatus = ledswi_getSwitchStatus(uiSwPos);
	if(eStatus == OFF) return 'C';
	if(eStatus == ON) return 'O';
	return ERROR;
}


/**
 * Method name:			interpreter_buzzerCommand
 * Method description: 	Executes commands pertinent to buzzer operation.
 * Input params:      	n/a                      
 * Output params:     	char = error code.                       
 */
char interpreter_buzzerCommand()
{
	uint8_t ui100, ui10, ui1, uiTime;
	while (UART0_BRD_S1_RDRF(UART0) == 0);
	ui100 = GETCHAR();
	PUTCHAR(ui100);
	while (UART0_BRD_S1_RDRF(UART0) == 0);
	ui10 = GETCHAR();
	PUTCHAR(ui10);
	while (UART0_BRD_S1_RDRF(UART0) == 0);
	ui1 = GETCHAR();
	PUTCHAR(ui1);
	if((ui100 < 48 || ui100 > 57) || (ui10 < 48 || ui10 > 57) || (ui1 < 48 || ui1 > 57)) // 0 through 9
		return ERROR;
	ui100 = ui100 - 48;
	ui10 = ui10 - 48;
	ui1 = ui1 - 48;
	uiTime = 100*ui100 + 10*ui10 + ui1;
	buzzer_1khz(uiTime);
	return NONE;
}

void interpreter_readCommand()
{
	if(UART0_BRD_S1_RDRF(UART0) == 0) return;
	uint8_t uiReceiveBuff, uiRetVal;
	uiReceiveBuff = GETCHAR();
	PUTCHAR(uiReceiveBuff);
	switch(uiReceiveBuff)
	{
		case 'L':
		case 'l':
			uiRetVal = interpreter_ledCommand();
			break;
		case 'S':
		case 's':
			uiRetVal = interpreter_switchCommand();
			break;
		case 'B':
		case 'b':
			uiRetVal = interpreter_buzzerCommand();
			break;
		default:
			uiRetVal = ERROR;
	}
	sendACK(uiRetVal);
}
