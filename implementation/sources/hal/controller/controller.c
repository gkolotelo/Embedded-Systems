/**
 *
 * File name:        	controller.c
 * File description: 	File containing the methods implementing
 * 						a PID controller.
 *
 * Authors:          	Bruno de Souza Ferreira
 * 						Guilherme Kairalla Kolotelo
 * 						Guilherme Bersi Pereira
 *
 * Creation date:    	20Jun2016
 * Revision date:    	20Jun2016
 *
 */

/* System includes */
#include <stdlib.h>

/* Project includes */
#include "controller.h"

/**
 * Method name:			controller_initPID
 * Method description:	Initializes the t_PID_Data with safe values
 * Input params:      	pidData	= t_PID_Data struct
 * Output params:     	n/a
 */
void controller_initPID(t_PID_Data *pidData)
{
	pidData->dKp = 0;
	pidData->dKi = 0;
	pidData->dKd = 0;
	pidData->dSensorPreviousValue = 0;
	pidData->dErrorSum = 0;
	pidData->dMaxSumError = 0;
}

/**
 * Method name:			controller_setMaxSumError
 * Method description:	Sets the maximum integrative error
 * Input params:      	pidData	= t_PID_Data struct
 * 						dMaxError = Maximum error acceptable
 * Output params:     	n/a
 */
void controller_setMaxSumError(t_PID_Data *pidData, double dMaxSumError)
{
	pidData->dMaxSumError = dMaxSumError;
}

/**
 * Method name:			controller_setKp
 * Method description:	Sets the Kp
 * Input params:      	pidData	= t_PID_Data struct
 * 						dPGain = Proportional constant
 * Output params:     	n/a
 */
void controller_setKp(t_PID_Data *pidData, double dPGain)
{
	pidData->dKp = dPGain;
}

/**
 * Method name:			controller_setKi
 * Method description:	Sets the Ki
 * Input params:      	pidData	= t_PID_Data struct
 * 						dIGain = Integrative constant
 * Output params:     	n/a
 */
void controller_setKi(t_PID_Data *pidData, double dIGain)
{
	pidData->dKi = dIGain;
}

/**
 * Method name:			controller_setKd
 * Method description:	Sets the Kd
 * Input params:      	pidData	= t_PID_Data struct
 * 						dDGain = Derivative constant
 * Output params:     	n/a
 */
void controller_setKd(t_PID_Data *pidData, double dDGain)
{
	pidData->dKd = dDGain;
}

/**
 * Method name:			controller_PIDUpdate
 * Method description:	Updates the running controller and retrieves the actuation value
 * Input params:      	pidData	= t_PID_Data struct
 * 						dSensorValue = Value from sensor
 * 						dReferenceValue = Reference value
 * Output params:     	double = Actuation value
 */
double controller_PIDUpdate(t_PID_Data *pidData, double dSensorValue, double dReferenceValue)
{
	if(dReferenceValue < 20) return 0;
	double dPterm, dIterm, dDterm;
	double dError, dDifference, dItemp;

	dError = dReferenceValue - dSensorValue;

	/* Proportional */
	dPterm = pidData->dKp * dError;

	/*  Integrative */
	dItemp = pidData->dErrorSum + dError;
	if(abs(dItemp) < pidData->dMaxSumError)
		pidData->dErrorSum = dItemp;
	dIterm = pidData->dKi * pidData->dErrorSum;

	/*  Derivative  */
	dDifference = pidData->dSensorPreviousValue - dSensorValue;
	pidData->dSensorPreviousValue = dSensorValue;
	dDterm = pidData->dKd * dDifference;

	return (dPterm + dIterm + dDterm);
}

