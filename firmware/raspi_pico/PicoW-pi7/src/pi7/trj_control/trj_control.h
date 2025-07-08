#ifndef __trj_control_h
#define __trj_control_h

/**
 * Commands for TrajectoryController
 */

#define NO_CMD      0
#define CMD_START   0x31
#define CMD_STOP    0x30
#define CMD_CALIBRATE 0x32
#define CMD_PARK    0x33


// Possible status for TrajectoryController
#define STATUS_RUNNING   0
#define STATUS_NOT_RUNNING 2
#define STATUS_CALIBRATING 3

// struct for communication between TrajectoryController and Controller
typedef struct {
	int command;
} tcl_Data;

// external interface
extern void tcl_processCommand(tcl_Data data);
extern void tcl_getSetpoint();
extern void tcl_init();
#endif
