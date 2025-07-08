#ifndef __trj_program_h
#define __trj_program_h

#include <stdint.h>

#define PROGRAM_TOO_LONG_ERR 3

typedef enum {
	G00,
	G01,
	G02,
	G03
} tpr_GCode;

typedef struct {
	float x;
	float y;
} tpr_Vector;

typedef struct {
	uint32_t ticks_left;
	uint32_t ticks_right;
} tpr_setPoint;

typedef struct {
	float x_e;
	float y_e;
	float x_c;
	float y_c;
	char code;
} tpr_Command;

extern int tpr_generateLinearSetPoints(tpr_Command* cmd);
extern int tpr_generateCircularSetPoints(tpr_Command* cmd);
extern tpr_setPoint tpr_getLine(int line);
extern void tpr_init();
extern void tpr_reset();
#endif
