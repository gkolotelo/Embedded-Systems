/**
 *
 * File name:           encoder.h                          
 * File description:    File containing the definition of methods for the
 *                      reading of an incremental, 3-pin, encoder.
 *                      
 *
 * Authors:             Bruno de Souza Ferreira
 *                      Guilherme Kairalla Kolotelo
 *                      Guilherme Bersi Pereira
 *
 * Creation date:       10Jun2016                                       
 * Revision date:       27Jun2016
 *
 */


#ifndef SOURCES_ENCODER_H_
#define SOURCES_ENCODER_H_


/**
 * Method name:         ENCODER_CHO_IRQ_HANDLER
 * Method description:  Channel O IRQ handler
 * Input params:        n/a
 * Output params:       n/a
 */
extern void ENCODER_CHO_IRQ_HANDLER();

/**
 * Method name:         encoder_initEncoder
 * Method description:  Initializes the encoder for an incremental 3-pin encoder
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_initEncoder();

/**
 * Method name:         encoder_enableCounter
 * Method description:  Enables the counter
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_enableCounter();

/**
 * Method name:         encoder_disableCounter
 * Method description:  Disables the counter
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_disableCounter();

/**
 * Method name:         encoder_resetCounter
 * Method description:  Resets the counter
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_resetCounter();

/**
 * Method name:         encoder_enableChOInterrupt
 * Method description:  Enables the interrupt on Channel O
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_enableChOInterrupt();

/**
 * Method name:         encoder_disableChOInterrupt
 * Method description:  Disables the interrupt on channel O
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_disableChOInterrupt();

/**
 * Method name:         encoder_takeMeasurement
 * Method description:  Takes a measurement of speed, direction and position
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_takeMeasurement();

/* Data retrieval methods */


/**
 * Method name:         encoder_getAngularPositionDegree
 * Method description:  Returns the angular position of the encoder in degrees
 * Input params:        n/a
 * Output params:       double = Angular position of the encoder in degrees
 */
double encoder_getAngularPositionDegree();

/**
 * Method name:         encoder_getAngularPositionRad
 * Method description:  Returns the angular position of the encoder in radians
 * Input params:        n/a
 * Output params:       double = Angular position of the encoder in radians
 */
double encoder_getAngularPositionRad();

/**
 * Method name:         encoder_getAngularVelocity
 * Method description:  Returns the angular velocity of the encoder in pulses per second
 * Input params:        n/a
 * Output params:       double = Angular velocity of the encoder in pps
 */
double encoder_getAngularVelocity();

/**
 * Method name:         encoder_getAngularVelocityRadPerSec
 * Method description:  Returns the angular velocity of the encoder in Rad/s
 * Input params:        n/a
 * Output params:       double = Angular velocity of the encoder in Rad/s
 */
double encoder_getAngularVelocityRad();

/**
 * Method name:         encoder_getAngularVelocityRPM
 * Method description:  Returns the angular velocity of the encoder in RPM
 * Input params:        n/a
 * Output params:       double = Angular velocity of the encoder in RPM
 */
double encoder_getAngularVelocityRPM();
/**
 * Method name:         encoder_getDirection
 * Method description:  Returns the direction the encoder is spinning
 * Input params:        n/a
 * Output params:       int = Direction (-1 or 1)
 */
int encoder_getDirection();

#endif /* SOURCES_ENCODER_H_ */
