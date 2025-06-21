/*
 * Modulo: Programa Trajetoria
 * Armazena o programa da trajetoria a ser executada
 */

#include "trj_program.h"
#include <math.h>
#include <stdio.h>


// PRIVATE DEFINES

#define MAX_PROGRAM_LINES 2000 // max NC program size
#define MAX_ACCELERATION 300 // max acceleration in mm/s^2
#define MAX_LIN_ACCELERATION_CONSTANT 5.7735 // 120*((1+1/sqrt(3))/2)^3 - 180*((1+1/sqrt(3))/2)^2 - 60*(1+1/sqrt(3))/2 -> Obtained analytically 
#define MAX_CIRC_ACCELERATION_CONSTANT 1.8542 // Obtained from curve fitting of the model T = a * sqrtf(r*theta*sqrtf(1+theta*theta)/ MAX_ACCELERATION)
#define TIME_STEP 0.01f // time step in seconds for interpolation
#define TICKS_PER_MM 67.4068f // number of ticks per mm for the motors
#define MOTOR_DISTANCE 300 // distance between motors in mm
#define X_HOME 150 // home position X in mm
#define Y_HOME 400 // home position Y in mm



// Private Variables

static tpr_setPoint tpr_program[MAX_PROGRAM_LINES]; // structure to store NC program
//tpr_Vector tpr_trajectory[MAX_PROGRAM_LINES]; // trajectory points for logging
static uint16_t program_index = 0;
static tpr_Vector current_position = {X_HOME, Y_HOME}; // current position of the machine
static int test_index = 0; // index for testing purposes
static float tempo = 0.0f; // time variable for testing purposes

// PRIVATE FUNCTIONS

tpr_Vector tpr_interpolatorPolynomial(tpr_Vector* start, tpr_Vector* dir, float time, float T) {
	tpr_Vector result;
	result.x = dir->x*(6*powf(time/T, 5) - 15*powf(time/T, 4) + 10*powf(time/T, 3)) + start->x;
	result.y = dir->y*(6*powf(time/T, 5) - 15*powf(time/T, 4) + 10*powf(time/T, 3)) + start->y;
	return result;
};

tpr_setPoint tpr_vector2SetPoint(tpr_Vector* vec) {
	tpr_setPoint sp;
	sp.ticks_left = (uint32_t)(sqrtf(powf(vec->x, 2) + powf(vec->y, 2)) * TICKS_PER_MM);
	sp.ticks_right = (uint32_t)(sqrtf(powf(MOTOR_DISTANCE - vec->x, 2) + powf(vec->y, 2)) * TICKS_PER_MM);
	return sp;
} // tpr_vector2SetPoint


float tpr_computeTheta(tpr_Vector* start, tpr_Vector* end, tpr_Vector* center) {
	tpr_Vector vec_start = {start->x - center->x, start->y - center->y};
	tpr_Vector vec_end = {end->x - center->x, end->y - center->y};
	float r = sqrtf(powf(vec_start.x, 2) + powf(vec_start.y, 2)); // radius
	float sin_theta = (vec_start.x * vec_end.y - vec_start.y * vec_end.x) / (r * r); // sine of angle
	return asinf(sin_theta); // angle in radians
} // tpr_computeTheta

tpr_Vector tpr_interpolatorArcPolynomial(tpr_Vector* center, float t, float T, float theta, float phase, float r) {
	tpr_Vector point;
	point.x = center->x + r * cosf(phase + theta*(6*powf(t/T, 5) - 15*powf(t/T, 4) + 10*powf(t/T, 3)));
	point.y = center->y + r * sinf(phase + theta*(6*powf(t/T, 5) - 15*powf(t/T, 4) + 10*powf(t/T, 3)));
	return point;
}

// PUBLIC FUNCTIONS

int tpr_generateLinearSetPoints(tpr_Command* cmd) {
    float L = sqrtf(powf(cmd->x_e - current_position.x, 2) + powf(cmd->y_e - current_position.y, 2));
	tpr_Vector dir = {cmd->x_e - current_position.x, cmd->y_e - current_position.y};
	float T = sqrtf(MAX_LIN_ACCELERATION_CONSTANT * L / MAX_ACCELERATION);
	uint16_t num_steps = (uint16_t)(T / TIME_STEP) + 1;
	tpr_Vector point;
	for (uint16_t i = 1; i < num_steps; i++) {
		float t = i * TIME_STEP;
		if (i == num_steps - 1) {
			t = T; // last point at time T
		}
		point = tpr_interpolatorPolynomial(&current_position, &dir, t, T);
		//printf("%.2f,%.6f,%.6f\n",t+tempo,point.x, point.y); // debug output
		tpr_setPoint setPoint = tpr_vector2SetPoint(&point);
		printf("%.2f,%d,%d\n", t + tempo, setPoint.ticks_left, setPoint.ticks_right); // debug output
		if (program_index < MAX_PROGRAM_LINES) {
			tpr_program[program_index] = setPoint;
//			tpr_trajectory[program_index] = point; // store trajectory point for logging
			program_index++;
		} else {
			return PROGRAM_TOO_LONG_ERR; // error: program too long
		}
	}
	current_position = point; // update current position
	tempo += T; // update time variable for testing
	return 0; // success 
} // tpr_generateLinearSetPoints

int tpr_generateCircularSetPoints(tpr_Command* cmd) {
	tpr_Vector center = {current_position.x + cmd->x_c, current_position.y + cmd->y_c}; // center of the arc
	float theta = tpr_computeTheta(&current_position, &(tpr_Vector){cmd->x_e, cmd->y_e}, &(tpr_Vector){center.x, center.y}); // angle in radians
	if (cmd->code == G02) {
		if (theta <= 0) {
			theta += 2 * M_PI; // ensure positive angle for clockwise direction
		}
	} else if (cmd->code == G03) {
		if (theta >= 0) {
			theta -= 2 * M_PI; // ensure negative angle for counter-clockwise direction
		}
	} else {
		return -1; // error: invalid G-code
	}
	float r = sqrtf(powf(center.x - current_position.x, 2) + powf(center.y - current_position.y, 2)); // radius
	float T = MAX_CIRC_ACCELERATION_CONSTANT * sqrtf(r*theta*sqrtf(1+theta*theta)/ MAX_ACCELERATION); // time to complete the arc
	uint16_t num_steps = (uint16_t)(T / TIME_STEP) + 1; // number of steps
	float phase = atan2f(current_position.y - center.y, current_position.x - center.x); // phase angle
	tpr_Vector point;
	for (uint16_t i = 1; i < num_steps; i++) {
		float t = i * TIME_STEP;
		if (i == num_steps - 1) {
			t = T; // last point at time T
		}
		point = tpr_interpolatorArcPolynomial(&(tpr_Vector){center.x, center.y}, t, T, theta, phase, r);
		//printf("%.2f,%.6f,%.6f\n",t+tempo, point.x, point.y); // debug output
		tpr_setPoint setPoint = tpr_vector2SetPoint(&point);
		printf("%.2f,%d,%d\n", t + tempo, setPoint.ticks_left, setPoint.ticks_right);
		if (program_index < MAX_PROGRAM_LINES) {
			tpr_program[program_index] = setPoint;
//			tpr_trajectory[program_index] = point; // store trajectory point for logging
			program_index++;
		} else {
			return PROGRAM_TOO_LONG_ERR; // error: program too long
		}	
	}
	current_position = point; // update current position
	tempo += T; // update time variable for testing
	return 0; // success
} // tpr_generateCircularSetPoints

tpr_setPoint tpr_getLine(int line) {
	return tpr_program[line];
} // tpr_getLine

void tpr_init() {
  int i;

  for (i=0; i<MAX_PROGRAM_LINES;i++) {
	  tpr_program[i].ticks_left = 0;
	  tpr_program[i].ticks_right = 0;

  }
} //tpr_init

void tpr_reset() {
  int i;

  for (i=0; i<MAX_PROGRAM_LINES;i++) {
	  tpr_program[i].ticks_left = 0;
	  tpr_program[i].ticks_right = 0;
  }
  program_index = 0;
  current_position.x = X_HOME;
  current_position.y = Y_HOME;
} //tpr_reset