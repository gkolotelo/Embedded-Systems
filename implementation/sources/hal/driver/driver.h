/**
 *
 * File name:           driver.h                            
 * File description:    File containing the definition of methods for the
 *                      operation of an H-Bridge in bipolar operation mode.
 *                      
 *                      - Driver actuation goes from -100 to 100, the former
 *                        being full reverse, and the latter, full steam ahead.
 *                      - Driver max freq @ 100kHz.
 *                      - Channel A on HighTrue and Channel B on LowTrue makes
 *                        for a bipolar H-Bridge operation.
 *
 * Authors:             Bruno de Souza Ferreira
 *                      Guilherme Kairalla Kolotelo
 *                      Guilherme Bersi Pereira
 *
 * Creation date:       10Jun2016                                       
 * Revision date:       20Jun2016                                       
 *
 */


#ifndef SOURCES_DRIVER_H_
#define SOURCES_DRIVER_H_

/**
 * Method name:         driver_initDriver
 * Method description:  Initializes the driver with the load in idle
 * Input params:        n/a
 * Output params:       n/a
 */
void driver_initDriver();

/**
 * Method name:         driver_disableDriver
 * Method description:  Disables the driver by clearing the enable pin
 * Input params:        n/a
 * Output params:       n/a
 */
void driver_disableDriver();

/**
 * Method name:         driver_enableDriver
 * Method description:  Enables the driver by setting the enable pin
 * Input params:        n/a
 * Output params:       n/a
 */
void driver_enableDriver();

/**
 * Method name:         driver_setChannelADutyCycle
 * Method description:  Sets duty cycle for Channel A only
 * Input params:        uiDutyCyclePercent = Duty cycle in percentage
 * Output params:       n/a
 */
void driver_setChannelADutyCycle(int uiDutyCyclePercent);

/**
 * Method name:         driver_setChannelBDutyCycle
 * Method description:  Sets duty cycle for Channel B only
 * Input params:        uiDutyCyclePercent = Duty cycle in percentage
 * Output params:       n/a
 */
void driver_setChannelBDutyCycle(int uiDutyCyclePercent);

/**
 * Method name:         driver_setHBridgeDutyCycle
 * Method description:  Sets duty cycle for H-Bridge operation. Both ChA and ChB
 * Input params:        uiDutyCyclePercent = Duty cycle in percentage (0% is full reverse, 100% is full ahead)
 * Output params:       n/a
 */
void driver_setHBridgeDutyCycle(int uiDutyCyclePercent);

/**
 * Method name:         driver_setDriver
 * Method description:  Sets the driver from -100 to 100, the former being full reverse, and the latter, full steam ahead.
 * Input params:        input = -100 to 100
 * Output params:       n/a
 */
void driver_setDriver(int input);

#endif /* SOURCES_DRIVER_H_ */
