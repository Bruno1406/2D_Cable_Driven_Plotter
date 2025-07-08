/*
 * Modulo: Interpretador de Comandos
 * Interpreta os comandos recebidos da IHM e processa-os
 */

#define byte uint8_t

/*
 * FreeRTOS includes
 */
#include "FreeRTOS.h"
#include "queue.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>

// Drivers for UART, LED and Console(debug)
//#include <cr_section_macros.h>
//#include <NXP/crp.h>
//#include "LPC17xx.h"
//#include "type.h"

// Includes for PI7
#include "command_interpreter.h"
#include "../trj_state/trj_state.h"
#include "../trj_control/trj_control.h"
#include "../trj_program/trj_program.h"

// communication with TrajectoryController
extern xQueueHandle qControlCommands;

void ctl_init(){

  // TODO: implementar

} // ctl_init

/************************************************************************
 ctl_ReadRegister
 Le o valor de um registrador
 Parametros de entrada:
    (int) numero do registrador a ser lido
 Retorno:
    (int) valor atual do registrador
*************************************************************************/
int ctl_ReadRegister(int registerToRead) {
   switch (registerToRead) {
      case REG_X:
         return (int)tst_getX();
      case REG_Y:
         return (int)tst_getY();
      case REG_Z:
         return (int)tst_getZ();
      case REG_LINHA:
         return tst_getCurrentLine();
      case REG_PIC0_STATE:
         return tst_getPicState(0).state;
      case REG_PIC0_CE:
         return tst_getPicState(0).controlEffort;
      case REG_PIC0_CEP:
         return tst_getPicState(0).controelEffortP;
      case REG_PIC0_CEI:
         return tst_getPicState(0).controlEffortI;
      case REG_PIC0_CED:
         return tst_getPicState(0).controlEffortD;
      case REG_PIC1_STATE:
         return tst_getPicState(1).state;
      case REG_PIC1_CE:
         return tst_getPicState(1).controlEffort;
      case REG_PIC1_CEP:
         return tst_getPicState(1).controelEffortP;
      case REG_PIC1_CEI: 
         return tst_getPicState(1).controlEffortI;
      case REG_PIC1_CED:
         return tst_getPicState(1).controlEffortD;
      default:
         printf("Unknown register to read: %d\n", registerToRead);
   } // switch
   return CTL_ERR;
} // ctl_ReadRegister

/************************************************************************
 ctl_WriteRegister
 Escreve o valor de um registrador. Notar que, quando for um registrador
 de controle (por exemplo, INICIAR) deve-se processar as acoes relativas
 a este registrador (no exemplo, iniciar o movimento)
 Parametros de entrada:
    (int) numero do registrador a ser escrito
    (int) valor a ser escrito
 Retorno:
    TRUE se escrita foi aceita, FALSE caso contrario.
*************************************************************************/
int ctl_WriteRegister(int registerToWrite, int value) {
  // TODO: implementar
  tcl_Data command;
  printf("Register %d Value %d\n", registerToWrite, value);
  switch(registerToWrite) {
  case REG_START:
	  printf("start program\n");
	  command.command = CMD_START;
	  xQueueSend(qControlCommands, &command, portMAX_DELAY);
	  break;
   case REG_CALIBRATE:
     printf("calibrate\n");
      command.command = CMD_CALIBRATE;
      xQueueSend(qControlCommands, &command, portMAX_DELAY);
      break;
   case REG_PARK:
      printf("park\n");
      command.command = CMD_PARK;
      xQueueSend(qControlCommands, &command, portMAX_DELAY);
      break;
  default:
	  printf("unknown register to write\n");
	  break;
  } //switch
  return true; //TRUE;
} // ctl_WriteRegister

/************************************************************************
 ctl_WriteProgram
 Escreve um programa. Notar que o programa foi informado como um byte[]
 logo compete neste caso ao controlador decodificar o programa e armazena-lo
 no DEVICE_MEMORY.
 Parametros de entrada:
    (byte[]) bytes que compoe o programa de movimentacao
 Retorno:
    TRUE se escrita foi aceita, FALSE caso contrario.
*************************************************************************/
int ctl_WriteProgram(int16_t* programRegisterData, uint16_t programSize) {
   // printf("ctl_WriteProgram called with size %d\r\n", programSize);
   tpr_Command cmd;
   int err = 0;
   int i = 0;
   tpr_reset(); // reset the program before writing new data
   while (i < programSize) {
      if (programRegisterData[i] == G00 || programRegisterData[i] == G01) {
         // G00 or G01 command
         if (i + 2 >= programSize) {
            printf("Invalid program data length for G00/G01\r\n");
            err = INVALID_PROGRAM_ERR;
            return err; 
         }
         cmd.code = programRegisterData[i];
         cmd.x_e = (float)programRegisterData[i + 1] / 10.0f; // convert to mm
         cmd.y_e = (float)programRegisterData[i + 2] / 10.0f; // convert to mm
         err = tpr_generateLinearSetPoints(&cmd);
         if (err) {
            printf("Error generating linear set points\r\n");
            return err; // return error if generation fails
         }
         i += 3; // advance to next command   
      } else if (programRegisterData[i] == G02 || programRegisterData[i] == G03) {
         // G02 or G03 command
         if (i + 4 >= programSize) {
            printf("Invalid program data length for G02/G03\r\n");
            err = INVALID_PROGRAM_ERR;
            return err; 
         }
         cmd.code = programRegisterData[i];
         cmd.x_e = (float)programRegisterData[i + 1] / 10.0f; // convert to mm
         cmd.y_e = (float)programRegisterData[i + 2] / 10.0f; // convert to mm
         cmd.x_c = (float)programRegisterData[i + 3] / 10.0f; // convert to mm
         cmd.y_c = (float)programRegisterData[i + 4] / 10.0f; // convert to mm
         err = tpr_generateCircularSetPoints(&cmd);
         if (err) {
            printf("Error generating circular set points\r\n");
            return err; // return error if generation fails
         }
         i += 5; // advance to next command   
      } else {
         printf("Invalid program data\r\n");
         err = INVALID_PROGRAM_ERR;
         return err; // return error if command is invalid
      }
   }
   return err; // return 0 if no error
} // ctl_WriteRegister
