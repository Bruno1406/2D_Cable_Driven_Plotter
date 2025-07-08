#ifndef __command_interpreter_h
#define __command_interpreter_h

#include <stdint.h>

// identification of registers to read
#define REG_X 0
#define REG_Y 1
#define REG_Z 2
#define REG_LINHA 3
#define REG_PIC0_STATE 4
#define REG_PIC0_CE 5
#define REG_PIC0_CEP 6  
#define REG_PIC0_CEI 7
#define REG_PIC0_CED 8
#define REG_PIC1_STATE 9
#define REG_PIC1_CE 10
#define REG_PIC1_CEP 11
#define REG_PIC1_CEI 12
#define REG_PIC1_CED 13


// identification of register to write
#define REG_START 0
#define REG_CALIBRATE 1
#define REG_PARK 2

// error
#define CTL_ERR -1
#define INVALID_PROGRAM_ERR -2

extern int ctl_ReadRegister(int registerToRead);
extern int ctl_WriteRegister(int registerToWrite, int value);
extern int ctl_WriteProgram(int16_t* programBytes, uint16_t programSize);
extern void ctl_init();

#endif
