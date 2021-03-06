/**
 *
 * File name:           controller.h                            
 * File description:    File containing the definition of methods
 *                      implementing a PID controller.
 *
 * Authors:             Bruno de Souza Ferreira
 *                      Guilherme Kairalla Kolotelo
 *                      Guilherme Bersi Pereira
 *
 * Creation date:       20Jun2016                                       
 * Revision date:       20Jun2016                                       
 *
 */

#ifndef SOURCES_CONTROLLER_H_
#define SOURCES_CONTROLLER_H_

/**
 * Type name:           t_PID_Data
 * Method description:  Struct containing variable for PID controller
 * Params:              dKp:                    Proportional gain
 *                      dKi:                    Integrative gain
 *                      dKd:                    Derivative gain
 *                      dSensorPreviousValue:   previous value read by sensor
 *                      dErrorSum:              Summation of previous errors up to dMaxSumError
 *                      dMaxSumError:           Maximum value dErrorSum can reach
 */
typedef struct
{
    double dKp;
    double dKi;
    double dKd;
    double dSensorPreviousValue;
    double dErrorSum;
    double dMaxSumError;
} t_PID_Data;


/**
 * Method name:         controller_initPID
 * Method description:  Initializes the t_PID_Data with safe values
 * Input params:        pidData = t_PID_Data struct
 * Output params:       n/a
 */
void controller_initPID(t_PID_Data *pidData);

/**
 * Method name:         controller_setMaxError
 * Method description:  Sets the maximum integrative error
 * Input params:        pidData = t_PID_Data struct
 *                      dMaxError = Maximum error acceptable
 * Output params:       n/a
 */
void controller_setMaxSumError(t_PID_Data *pidData, double dMaxSumError);

/**
 * Method name:         controller_setKp
 * Method description:  Sets the Kp
 * Input params:        pidData = t_PID_Data struct
 *                      dPGain = Proportional constant
 * Output params:       n/a
 */
void controller_setKp(t_PID_Data *pidData, double dPGain);

/**
 * Method name:         controller_setKi
 * Method description:  Sets the Ki
 * Input params:        pidData = t_PID_Data struct
 *                      dIGain = Integrative constant
 * Output params:       n/a
 */
void controller_setKi(t_PID_Data *pidData, double dIGain);

/**
 * Method name:         controller_setKd
 * Method description:  Sets the Kd
 * Input params:        pidData = t_PID_Data struct
 *                      dDGain = Derivative constant
 * Output params:       n/a
 */
void controller_setKd(t_PID_Data *pidData, double dDGain);

/**
 * Method name:         controller_PIDUpdate
 * Method description:  Updates the running controller and retrieves the actuation value
 * Input params:        pidData = t_PID_Data struct
 *                      dSensorValue = Value from sensor
 *                      dReferenceValue = Reference value
 * Output params:       double = Actuation value
 */
double controller_PIDUpdate(t_PID_Data *pidData, double dSensorValue, double dReferenceValue);

#endif /* SOURCES_CONTROLLER_H_ */
