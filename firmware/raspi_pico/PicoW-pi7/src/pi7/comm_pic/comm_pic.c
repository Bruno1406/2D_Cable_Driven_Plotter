/**
 * Modulo: Comunicacao MODBUS (simplificada)
 * Usa a Serial0 para comunicar-se
 * [jo:230927] usa UART0 e UART1 para comunicação
 */


#include <stdbool.h>
#include <stdio.h>
#include "drivers/uart/uart.h"

// FreeRTOS includes
#include "FreeRTOS.h"
#include "projdefs.h"
#include "task.h"

// Header files for PI7
#include "comm_pic.h"

void pic_init(void){

  // TODO: implementar
  
} // pic_init

void pic_sendToPIC(pic_TxData data) {
  uint8_t out1[4];
  uint8_t out0[4];
  out0[0] = ':';
  out0[1] = data.command; // comando
  out0[2] = data.setPointLeft & 0xFF; // setPoint LSB
  out0[3] = (data.setPointLeft >> 8); // setPoint MSB

  out1[0] = ':';
  out1[1] = data.command; // comando
  out1[2] = data.setPointRight & 0xFF; // setPoint LSB
  out1[3] = (data.setPointRight >> 8); // setPoint

  for(uint8_t i = 0; i < 4; i++) {
    UARTSend(0, out0+i,1); // send to UART0
    UARTSend(1, out1+i,1); // send to UART1
    vTaskDelay(5); // wait 1 ms between sends
  }


  // TODO: implementar

} // pic_sendToPIC

char pic_receiveCharFromPIC(uint8_t portNum) {

  uint16_t ch = UARTGetChar(portNum, false); // get character from UART
  return ch; // return the character received
} // pic_receiveFromPIC

void pic_receiveBufferFromPIC(uint8_t portNum, rx_buffer_t *rxBuffer) {
  // Receives a buffer of characters from the specified UART port
  UARTGetBuffer(portNum, rxBuffer);
} // pic_receiveBufferFromPIC
