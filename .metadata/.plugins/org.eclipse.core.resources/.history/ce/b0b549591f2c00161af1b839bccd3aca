
/* system includes */
#include "fsl_debug_console.h"
#include "fsl_device_registers.h"

#include "hal/buzzer/buzzer.h"
#include "hal/mcg/mcg.h"
#include "hal/util/util.h"
#include "hal/ledswi/ledswi.h"
#include "hal/display_7segments/display_7segments.h"
#include "hal/uart/debugUart.h"
#include "hal/uart/interpreter.h"
#include "hal/lcd/lcd.h"
#include "hal/pwm/pwm.h"
#include "hal/util/tc_hal.h"
#include "hal/cooler/cooler.h"
#include "hal/tach/tach.h"

/* defines */
#define CYCLIC_EXECUTIVE_PERIOD         100 * 10000 /* 1000000 micro seconds */

/* globals */
volatile unsigned int uiFlagNextPeriod = 0;         /* cyclic executive flag */

void main_cyclicExecuteIsr(void)
{
    /* set the cyclic executive flag */
    uiFlagNextPeriod = 1;
}

int boardInit()
{
    mcg_clockInit();
}

int peripheralInit()
{
	interpreter_init();
	buzzer_init();
	ledswi_initLedSwitch(1,3);
	display_7segments_initDisplays();
	lcd_initLcd();
	//cooler_init();
	tach_init();

	tc_installLptmr0(CYCLIC_EXECUTIVE_PERIOD, main_cyclicExecuteIsr);
}

int main(void)
{
    boardInit();
    peripheralInit();
    // Set Red LED for Status
    SIM_SCGC5 |= (SIM_SCGC5_PORTB_MASK);
    //PORTB_PCR18 = PORT_PCR_MUX(1);
    //PTB_BASE_PTR->PDDR = 1 << 18;

    tpm_config_t tpmConfig =
    {
    		.eClock_source = McgIrcClk,
			.uiPeriod_ms = 1000,
			.ePrescaler_value = Prescaler1,
			.uiXtal_frequency = 32000,
			.eAlignment = Edge
    };

    channel_config_t channelConfig =
    {
    		.eChannelOutput = NoInversion,
			.uiChannel = 1,
			.uiInterrupt_enable = 0,
			.uiPulse_width_ms = 500
    };

    pwm_initPwm(TPM2, tpmConfig);
    pwm_channelInit (TPM1, tpmConfig, channelConfig);


    SIM_BASE_PTR->SCGC5 |= SIM_SCGC5_PORTB_MASK;
    PORTB_BASE_PTR->PCR[18] = PORTB_BASE_PTR->PCR[19] = PORT_PCR_MUX(3);
    PTB_BASE_PTR->PDDR = 0b11 << 19;

    // Locals
    char readout[15];
    uint16_t value;

    for (;;) {
    	//interpreter_readCommand();
    	// Blink Red LED for Status
    	//PTB_BASE_PTR->PTOR = 1 << 18;

    	// Read and print counter value
    	//value = tach_readCounter();
    	value = tach_Hz(CYCLIC_EXECUTIVE_PERIOD/1000);
    	lcd_itoa(value, readout);
    	lcd_clearLine(0);
    	lcd_writeString(readout);
    	lcd_writeString(" Hz");

    	// Wait for next period
    	while(!uiFlagNextPeriod);
    	uiFlagNextPeriod = 0;

    }

    return 0;
}
////////////////////////////////////////////////////////////////////////////////
// EOF
////////////////////////////////////////////////////////////////////////////////
