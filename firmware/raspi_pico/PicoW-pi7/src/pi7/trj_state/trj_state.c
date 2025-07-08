/*
 * Modulo: Estado Trajetoria
 * Contem as variaveis de estado da trajetoria e de controle da maquina em geral
 */

#include "trj_state.h"
#include <stdio.h>

int tst_line;
int tst_lastLine;
float tst_x;
float tst_y;
float tst_z;
pic_RxData tst_picState0;
pic_RxData tst_picState1;

int tst_getCurrentLine() {
	return tst_line;
} // tst_getCurrentLine

void tst_setCurrentLine(int line) {
	tst_line = line;
} // tst_setCurrentLine

int tst_getLastLine() {
	return tst_lastLine;
} // tst_getLastLine

void tst_setLastLine(int line) {
	tst_lastLine = line;
} // tst_setLastLine

float tst_getX() {
	return tst_x;
} // tst_getX

float tst_getY() {
	return tst_y;
} // tst_getY

float tst_getZ() {
	return tst_z;
} // tst_getZ

void tst_setX(float x) {
	tst_x = x;
} // tst_setX

void tst_setY(float y) {
	tst_y = y;
} // tst_setY

void tst_setZ(float z) {
	tst_z = z;
} // tst_setZ

void tst_init() {
} // tst_init

pic_RxData tst_getPicState(uint8_t portNum) {
	if(portNum == 0) {
		return tst_picState0;
	} else if(portNum == 1) {
		return tst_picState1;
	} else {
		pic_RxData invalidState = {0, 0, 0, 0}; // return an invalid state
		return invalidState;
	}
}

void tst_setPicState(pic_RxData state, uint8_t portNum) {
	if(portNum == 0) {
		tst_picState0 = state;
	} else if(portNum == 1) {
		tst_picState1 = state;
	} else {
		printf("Invalid port number for tst_setPicState\n");
	}
}

