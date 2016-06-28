typedef enum
{
    NoneClk,
    McgPllFllClk,
    OscerClk,
    McgIrcClk
} pwm_clock_source_e;

typedef enum
{
	Edge,
	Center
} pwm_alignment_e;

typedef enum
{
	DisableChannel,
	NoInversion,
	Inversion
} pwm_output_e;

typedef enum
{
	Prescaler1,
	Prescaler2,
	Prescaler4,
	Prescaler8,
	Prescaler16,
	Prescaler32,
	Prescaler64,
	Prescaler128
} pwm_prescaler_e;

typedef struct
{
	pwm_clock_source_e eClock_source;
	pwm_prescaler_e ePrescaler_value;
	uint16_t uiPeriod_ms;
	uint32_t uiXtal_frequency;
	pwm_alignment_e eAlignment;
} tpm_config_t;

typedef struct
{
	uint8_t uiChannel;
	uint16_t uiPulse_width_ms;
	pwm_output_e eChannelOutput;
	uint8_t uiInterrupt_enable;
} channel_config_t;

/**
 * Method name:			initPwm
 * Method description:  Initializes PWM module with specified configuration
 * Input params:      	tTimer = TPMx base address
 * 						tTpmConfig = Configuration for TPM module
 * Output params:     	int = Error (0) or Success (0)
 */
int pwm_initPwm(TPM_Type * tTimer, tpm_config_t tTpmConfig);

/**
 * Method name:			channelInit
 * Method description:  Initializes the PWM channel with specified configuration
 * Input params:      	tTimer = TPMx base address
 * 						tTpmConfig = Configuration for TPM module
 * 						tChannelConfig = Configuration for PWM channel
 * Output params:     	int = Error (0) or Success (0)
 */
int pwm_channelInit (TPM_Type * tTimer, tpm_config_t tTpmConfig, channel_config_t tChannelConfig);

/**
 * Method name:			changeChannelPeriod
 * Method description:  Changes the period of the PWM on the channel
 * Input params:      	tTimer = TPMx base address
 * 						tTpmConfig = Configuration for TPM module
 * 						uiChannel = PWM channel
 * 						uiPulseWidth_ms = Channel period in ms
 * Output params:     	int = Error (0) or Success (0)
 */
int pwm_changeChannelDuty(TPM_Type * tTimer, tpm_config_t tTpmConfig, uint16_t uiChannel, uint16_t uiPulseWidth_ms);

/**
 * Method name:			changeModulePeriod
 * Method description:  Changes the TPM module period
 * Input params:      	tTimer = TPMx base address
 * 						tTpmConfig = Configuration for TPM module
 * Output params:     	int = Error (0) or Success (0)  	                        
 */
int pwm_changeModulePeriod(TPM_Type * tTimer, tpm_config_t tTpmConfig);

/**
 * Method name:			deinitPwm
 * Method description:  Deinitializes PWM module
 * Input params:      	tTimer = TPMx base address
 * Output params:     	n/a
 */
void pwm_deinitPwm(TPM_Type * tTimer);

/**
 * Method name:			disableCounter
 * Method description:  Disables the module counter
 * Input params:      	tTimer = TPMx base address
 * Output params:     	n/a
 */
void pwm_disableCounter(TPM_Type * tTimer)

/**
 * Method name:			enableCounter
 * Method description:  Enables the module counter
 * Input params:      	tTimer = TPMx base address
 * Output params:     	n/a
 */
void pwm_enableCounter(TPM_Type * tTimer)
