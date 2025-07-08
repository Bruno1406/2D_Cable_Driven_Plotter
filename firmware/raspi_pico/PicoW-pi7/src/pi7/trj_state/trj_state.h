#ifndef __trj_state_h
#define __trj_state_h

#include "../comm_pic/comm_pic.h"

// external interface
extern int tst_getCurrentLine();
extern void tst_setCurrentLine(int line);
extern int tst_getLastLine();
extern void tst_setLastLine(int line);
extern float tst_getX();
extern float tst_getY();
extern float tst_getZ();
extern void tst_setX(float x);
extern void tst_setY(float y);
extern void tst_setZ(float z);
extern void tst_init();
extern pic_RxData tst_getPicState(uint8_t portNum);
extern void tst_setPicState(pic_RxData state, uint8_t portNum);

#endif
