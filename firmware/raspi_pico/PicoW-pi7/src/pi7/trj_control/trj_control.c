/**
 * Modulo: Controlador de trajetoria (exemplo!!)
 *
 */

/*
 * FreeRTOS includes
 */
#include "FreeRTOS.h"
#include "queue.h"

#include <stdio.h>

// Header files for PI7
#include "trj_control.h"
#include "../trj_program/trj_program.h"
#include "../trj_state/trj_state.h"
#include "../comm_pic/comm_pic.h"

// local variables
int tcl_status;
extern xQueueHandle qCommTxPIC;

void tcl_getSetpoint() {

  int currLine;
  tpr_setPoint line;
  pic_TxData toPic;

  if (tcl_status == STATUS_NOT_RUNNING) {
    return;
  }


  currLine = tst_getCurrentLine();
  if (currLine >= tst_getLastLine()) {
    printf("End of trajectory reached at line %d\n", currLine);
    tcl_status = STATUS_NOT_RUNNING;
    toPic.command = CMD_STOP;
    toPic.setPointLeft = 0;
    toPic.setPointRight = 0;
    xQueueSend(qCommTxPIC, &toPic, 0);
    return;
  }

  //printf("CurrLine %d\n", currLine);pic_Data
  line = tpr_getLine(currLine);
  toPic.command = CMD_START;
  toPic.setPointLeft = line.ticks_left;
  toPic.setPointRight = line.ticks_right;
  // printf("Sending to PIC: L=%d R=%d\n", toPic.setPointLeft, toPic.setPointRight);
  xQueueSend(qCommTxPIC, &toPic, 0);
  currLine++;
  tst_setCurrentLine(currLine);
} // trj_generateSetpoint

void tcl_processCommand(tcl_Data data) {
  pic_TxData toPic;
  if (data.command == CMD_STOP) {
    tcl_status = STATUS_NOT_RUNNING;
    toPic.command = CMD_STOP;
    toPic.setPointLeft = 0;
    toPic.setPointRight = 0;
    xQueueSend(qCommTxPIC, &toPic, 0);
  }

  if ((data.command == CMD_START)) {
    printf("starting trajectory\n");
    tcl_status = STATUS_RUNNING;
    tst_setCurrentLine(0);
  }

  if (data.command == CMD_CALIBRATE) {
    printf("Calibrating...\n");
    tcl_status = STATUS_NOT_RUNNING;
    toPic.command = CMD_CALIBRATE;
    toPic.setPointLeft = 0;
    toPic.setPointRight = 0;
    xQueueSend(qCommTxPIC, &toPic, 0);
  }

  if (data.command == CMD_PARK) {
    printf("Parking...\n");
    tcl_status = STATUS_NOT_RUNNING;
    toPic.command = CMD_START;
    toPic.setPointLeft = 5247;
    toPic.setPointRight = 5247;
    xQueueSend(qCommTxPIC, &toPic, 0);
  }

} // trj_executeCommand

void tcl_init() {
  tcl_status = STATUS_NOT_RUNNING;
} // init
