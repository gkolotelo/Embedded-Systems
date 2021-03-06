/**
 *
 * File name:           hmi.c
 * File description:    File containing the definition of methods for interaction
 *                      with a host device via a serial connection.
 *
 * Authors:             Bruno de Souza Ferreira
 *                      Guilherme Kairalla Kolotelo
 *                      Guilherme Bersi Pereira
 *
 * Creation date:       25Jun2016
 * Revision date:       27Jun2016
 *
 */

#ifndef SOURCES_HMI_H_
#define SOURCES_HMI_H_

/**
 * Method name:         hmi_initHmi
 * Method description:  Initializes UART0 for debug mode for serial over USB, provided by OpenSDA.
 * Input params:        n/a
 * Output params:       n/a
 */
void hmi_initHmi();

/**
 * Method name:         hmi_receive
 * Method description:  Receives and interprets data sent from the host device.
 * Input params:        n/a
 * Output params:       n/a
 */
void hmi_receive();

/**
 * Method name:         hmi_transmit
 * Method description:  Transmits required data to the host device. Uses space as separator
 * Input params:        dVelocity: Velocity reading from encoder
 *                      dPosition: Position reading from encoder
 *                      dActuator: Actuator value from controller
 * Output params:       n/a
 */
void hmi_transmit(double dVelocity, double dPosition, double dActuator);

#endif /* SOURCES_HMI_H_ */
