


#include "../es670_peripheral_board.h"
#include "../mcg/mcg.h"
#include "pwm.h"


#define TPM0_CHANNEL_WIDTH 5
#define TPM1_CHANNEL_WIDTH 1
#define TPM2_CHANNEL_WIDTH 1


/*
@ 8MHz min and max periods for prescalers:
ps  	min(ms)   	max(ms)
1		125e-6		8.19
2		25e-5		16.4
4		5e-4		32.7
8		0.001		65.6
16		0.002		131
32		0.004		262.1
64		0.008		524.2
128		0.016		1048.5

*/


int pwm_initPwm(TPM_Type * tTimer, tpm_config_t tTpmConfig)
{
	uint32_t cnt_period;

	if(TPM0 == tTimer)
		SIM_BASE_PTR->SCGC6 |= SIM_SCGC6_TPM0_MASK;
	else if(TPM1 == tTimer)
		SIM_BASE_PTR->SCGC6 |= SIM_SCGC6_TPM1_MASK;
	else if(TPM2 == tTimer)
		SIM_BASE_PTR->SCGC6 |= SIM_SCGC6_TPM2_MASK;
	else return 0;

	cnt_period= (1000*(tTpmConfig.uiXtal_frequency/((2 << tTpmConfig.ePrescaler_value)/2))/tTpmConfig.uiPeriod_ms);
	if(Center == tTpmConfig.eAlignment)
		cnt_period = cnt_period/2;
	if (cnt_period > 65536)
		return 0;

	SIM_BASE_PTR->SOPT2 |= SIM_SOPT2_TPMSRC(tTpmConfig.eClock_source); // Set clock source for TMPx

    tTimer->SC |= TPM_SC_CMOD(0); 					// Disable clock to TMPx  (SC,CMOD)
    while (tTimer->SC&TPM_SC_CMOD_MASK); 			// Wait to acknowledge tTimer is disabled (SC,CMOD)
    tTimer->SC |= TPM_SC_TOF(0); 					// Clear tTimer Overflow Flag (SC,TOF)
    tTimer->SC |= TPM_SC_CPWMS(tTpmConfig.eAlignment);// Set up counting mode (SC,CPWMS)
    tTimer->CNT = 0;								// Reset Counter  (CNT)

    tTimer->MOD = cnt_period;						// Set TPM counter period (MOD)
    tTimer->SC = TPM_SC_PS(tTpmConfig.ePrescaler_value);
	tTimer->SC = TPM_SC_CMOD(1);					//Selects the LPTPM counter clock modes

	return 1;
}

int pwm_channelInit (TPM_Type * tTimer, tpm_config_t tTpmConfig, channel_config_t tChannelConfig)
{
	uint32_t cnt_period, cnv_period, cnsc;

	cnsc = 0x00;
	cnt_period = (1000*(tTpmConfig.uiXtal_frequency/((2 << tTpmConfig.ePrescaler_value)/2))/tTpmConfig.uiPeriod_ms);
	if(Center == tTpmConfig.eAlignment)
		cnt_period = cnt_period/2;
	if (cnt_period > 65536)
		return 0;
	cnv_period = (cnt_period*tChannelConfig.uiPulse_width_ms)/tTpmConfig.uiPeriod_ms;

	if(TPM0 == tTimer)
		if(tChannelConfig.uiChannel > TPM0_CHANNEL_WIDTH) return 0;
	else if(TPM1 == tTimer)
		if(tChannelConfig.uiChannel > TPM1_CHANNEL_WIDTH) return 0;
	else if(TPM2 == tTimer)
		if(tChannelConfig.uiChannel > TPM2_CHANNEL_WIDTH) return 0;
	else return 0;

	if(DisableChannel == tChannelConfig.eChannelOutput)
	{
		cnsc = 0;
	}
	else if(NoInversion == tChannelConfig.eChannelOutput)
	{
		cnsc |= TPM_CnSC_MSB_MASK | TPM_CnSC_ELSB_MASK;
	}
	else if(Inversion == tChannelConfig.eChannelOutput)
	{
		cnsc |= TPM_CnSC_MSB_MASK | TPM_CnSC_ELSA_MASK;
	}

	if(0 != tChannelConfig.uiInterrupt_enable)
		cnsc |= TPM_CnSC_CHIE_MASK;

	tTimer->CNT = 0;
	tTimer->CONTROLS[tChannelConfig.uiChannel].CnSC = cnsc;
	tTimer->CONTROLS[tChannelConfig.uiChannel].CnV = cnv_period;

	return 1;
}

int pwm_changeChannelDuty(TPM_Type * tTimer, tpm_config_t tTpmConfig, uint16_t uiChannel, uint16_t uiPulseWidth_ms)
{
	uint32_t cnt_period, cnv_period;

	cnt_period= (1000*(tTpmConfig.uiXtal_frequency/((2 << tTpmConfig.ePrescaler_value)/2))/tTpmConfig.uiPeriod_ms);
	if(Center == tTpmConfig.eAlignment)
		cnt_period = cnt_period/2;
	if (cnt_period > 65536)
		return 0;
	cnv_period= (cnt_period*uiPulseWidth_ms)/tTpmConfig.uiPeriod_ms;

	tTimer->CONTROLS[uiChannel].CnV = cnv_period;
	return 1;
}

int pwm_changeModulePeriod(TPM_Type * tTimer, tpm_config_t tTpmConfig)
{
	uint32_t cnt_period;

	cnt_period = (1000*(tTpmConfig.uiXtal_frequency/((2 << tTpmConfig.ePrescaler_value)/2))/tTpmConfig.uiPeriod_ms);
	if(Center == tTpmConfig.eAlignment)
		cnt_period = cnt_period/2;
	if (cnt_period > 65536)
		return 0;
    tTimer->MOD = cnt_period;
	tTimer->CNT = 0;

	return 1;
}

void pwm_deinitPwm(TPM_Type * tTimer)
{
	tTimer->SC |= TPM_SC_CMOD(0); 						// Disable clock to TMPx  (SC,CMOD)
    while (tTimer->SC&TPM_SC_CMOD_MASK); 				// Wait to acknowledge tTimer is disabled (SC,CMOD)
	tTimer->SC |= TPM_SC_TOF(0); 						// Clear tTimer Overflow Flag (SC,TOF)
    tTimer->CNT = 0;									// Reset Counter  (CNT)
    if(TPM0 == tTimer)
		SIM_BASE_PTR->SCGC6 &= !SIM_SCGC6_TPM0_MASK;
	else if(TPM1 == tTimer)
		SIM_BASE_PTR->SCGC6 &= !SIM_SCGC6_TPM1_MASK;
	else if(TPM2 == tTimer)
		SIM_BASE_PTR->SCGC6 &= !SIM_SCGC6_TPM2_MASK;
}

void pwm_disableCounter(TPM_Type * tTimer)
{
	tTimer->SC |= TPM_SC_CMOD(0); 						// Disable clock to TMPx  (SC,CMOD)
    while (tTimer->SC&TPM_SC_CMOD_MASK); 				// Wait to acknowledge tTimer is disabled (SC,CMOD)
}

void pwm_enableCounter(TPM_Type * tTimer)
{
	tTimer->SC |= TPM_SC_CMOD(1);
}

