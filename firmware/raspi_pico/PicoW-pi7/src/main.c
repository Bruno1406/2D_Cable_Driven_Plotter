/**
 * Name        : main.c
 * Version     :
 * Description : main definition for FreeRTOS application
 */

/*
 * FreeRTOS includes
 */
#include "FreeRTOS.h"
#include "projdefs.h"
#include "task.h"
#include "queue.h"
#include "semphr.h"

// Raspberry PICO W includes
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
//#include <type.h>
#include "boards/pico_w.h"
#include "pico/error.h"
#include "pico/stdio.h"
#include "pico/stdio_usb.h"
#include "pico/stdlib.h"
#include "pico/multicore.h"

// Drivers for UART and LED
#include "drivers/ledonboard/leds.h"
#include "drivers/uart/uart.h"

// Header files for PI7
#include "pi7/comm_pic/comm_pic.h"
#include "pi7/comm_pc/modbus.h"
#include "pi7/command_interpreter/command_interpreter.h"
#include "pi7/trj_control/trj_control.h"
#include "pi7/trj_program/trj_program.h"
#include "pi7/trj_state/trj_state.h"

// PI7 DEFINES
#define CONTROL_Q_SIZE 1 // queue sizes
#define PIC_Q_SIZE 2
#define DEV_Q_SIZE 20
#define UART_BAUD 115200

/**
 * Time constants for FreeRTOS delays
 */
const portTickType DELAY_1SEC = 1000 / portTICK_RATE_MS;
const portTickType DELAY_500MS = 500 / portTICK_RATE_MS;
const portTickType DELAY_200MS = 200 / portTICK_RATE_MS;
const portTickType DELAY_100MS = 100 / portTICK_RATE_MS;
const portTickType DELAY_50MS = 50 / portTICK_RATE_MS;
const portTickType DELAY_30MS = 30 / portTICK_RATE_MS;
const portTickType DELAY_10MS = 10 / portTICK_RATE_MS;
const portTickType DELAY_5MS = 5 / portTICK_RATE_MS;
const portTickType DELAY_1MS = 1 / portTICK_RATE_MS;

//void __error__(char *pcFilename, unsigned long ulLine) {
//}

/**
 * Communication queues for data transfer between components
 */
QueueHandle_t qControlCommands;
QueueHandle_t qCommTxPIC;
QueueHandle_t qCommDev; // para testes

#define USERTASK_STACK_SIZE configMINIMAL_STACK_SIZE

void taskController(void *pvParameters) {
  while(1) {
    
    com_executeCommunication(); //internally, it calls Controller to process events
    vTaskDelay(DELAY_1MS); // [jo:230929] TODO: por que não tem vTaskDelay() ? -> não, tem espera na fila
  } //task loop
} // taskController

/**
 * taskNCProcessing: processes NC Program. It receives commands from Controller
 * via queue qControlCommands (start/pause/resume/abort)
 * Runs every 200ms (may generate up to 5 new setpoints per second to interpolate trajectory)
 * Note the use of vTaskDelayUntil instead of vTaskDelay; this will cause system to run every 200ms.
 */
//portTickType lastWakeTime;
void taskNCProcessing(void *pvParameters) {
  static portTickType lastWakeTime;
  tcl_Data data;
  lastWakeTime = xTaskGetTickCount();
  while(1) {
    data.command = NO_CMD;
    xQueueReceive(qControlCommands, &data, 0); //do not wait for command
    if (data.command != NO_CMD) {
      tcl_processCommand(data);
    }
    tcl_getSetpoint();
    vTaskDelayUntil(&lastWakeTime, DELAY_30MS);
  } //task loop
} // taskNCProcessing

/**
 * taskCommPIC: receive setpoints to send to PICs from queue qCommTxPIC
 * and send them following PIC protocol
 */
void taskCommPIC(void *pvParameters) {
	pic_TxData setpoints;

  char buffer0[BUFSIZE]; // buffer for PIC 0
  char buffer1[BUFSIZE]; // buffer for PIC 1

  pic_RxData rxData0;
  pic_RxData rxData1;

  rx_buffer_t rxBuffer0 = {
    .buffer = buffer0,
    .size = 0
  }; // buffer for PIC 0
  rx_buffer_t rxBuffer1 = {
    .buffer = buffer1,
    .size = 0
  }; // buffer for PIC 1

  bool waitingForStart0 = true; // flag to indicate if waiting for start command from PIC 0
  bool waitingForStart1 = true; // flag to indicate if waiting for start command from PIC 1

  char current_message0[sizeof(pic_RxData)];
  char current_message1[sizeof(pic_RxData)];

  uint8_t index0 = 0; // index for current message from PIC 0
  uint8_t index1 = 0; // index for current message from PIC 1

	while(1) {
    if(xQueueReceive(qCommTxPIC, &setpoints, 0) == pdTRUE) {
      pic_sendToPIC(setpoints);
    }
    pic_receiveBufferFromPIC(0, &rxBuffer0); // receive data from PIC 0
    pic_receiveBufferFromPIC(1, &rxBuffer1); // receive data from PIC 1
    for (uint8_t i = 0; i < rxBuffer0.size; i++) {
      if (rxBuffer0.buffer[i] == ':' && waitingForStart0) {
        // start receiving data from PIC 0
        waitingForStart0 = false;
      } else if (!waitingForStart0) {
        // store received data in current_message0
        current_message0[index0++] = rxBuffer0.buffer[i];
        if (index0 >= sizeof(pic_RxData)) {
          // received a complete message from PIC 0
          index0 = 0; // reset index for next message
          waitingForStart0 = true; // reset flag for next message
          // parse received data into rxData0 struct
          rxData0.controlEffort = current_message0[1] << 8 | current_message0[0];
          rxData0.controelEffortP = current_message0[3] << 8 | current_message0[2];
          rxData0.controlEffortI = current_message0[5] << 8 | current_message0[4];
          rxData0.controlEffortD = current_message0[7] << 8 | current_message0[6];
          rxData0.state = current_message0[8]; // assuming state is the last byte
          // printf("Received from PIC 0: State=%d, ControlEffort=%d, P=%d, I=%d, D=%d\n",
          //        rxData0.state, rxData0.controlEffort, rxData0.controelEffortP,
          //        rxData0.controlEffortI, rxData0.controlEffortD);
          tst_setPicState(rxData0, 0); // set PIC 0 state in trajectory state
        }
      }
    }
    for (uint8_t i = 0; i < rxBuffer1.size; i++) {
      if (rxBuffer1.buffer[i] == ':' && waitingForStart1) {
        // start receiving data from PIC 1
        waitingForStart1 = false;
      } else if (!waitingForStart1) {
        // store received data in current_message1
        current_message1[index1++] = rxBuffer1.buffer[i];
        if (index1 >= sizeof(pic_RxData)) {
          // received a complete message from PIC 1
          index1 = 0; // reset index for next message
          waitingForStart1 = true; // reset flag for next message
          // parse received data into rxData1 struct
          memcpy(&rxData1, current_message1, sizeof(pic_RxData));
          // printf("Received from PIC 1: State=%d, ControlEffort=%d, P=%d, I=%d, D=%d\n",
          //        rxData1.state, rxData1.controlEffort, rxData1.controelEffortP,
          //        rxData1.controlEffortI, rxData1.controlEffortD);
          tst_setPicState(rxData1, 1); // set PIC 1 state in trajectory state
        }
      }
    }

    vTaskDelay(DELAY_1MS); // wait 200 ms before next iteration
  } //task loop
} // taskCommPIC

void taskBlinkLed(void *lpParameters) {
  // uint16_t ch = NO_CHAR;  // [jo:231005] teste console DEV_MODE
  // uint16_t response = NO_CHAR; // [jo:231005] teste console DEV_MODE
	// while(1) {
	// 	// led_invert();
  //   ch = getchar_timeout_us(5);
   
  //   if(ch != 0xfe && ch != NO_CHAR) { // [jo:231005] modbus só pela serial USB
  //     printf("Sending char: %c\n", ch);
  //     UARTSend(0, (uint8_t*)&ch, 1); // [jo:231004] teste
  //   }
  //   response = UARTGetChar(0, false); // [jo:231004] teste
  //   if(response != NO_CHAR) {
  //     printf("Received: %c\n", response); // [jo:231005] teste console DEV_MODE
  //   } 
	// 	vTaskDelay(DELAY_500MS); // wait 500 ms
  //   //printf("LED toggled\n"); // [jo:231005] teste console DEV_MODE
  //   //printf("Received char: %c\n", ch); // [jo:231005] teste console DEV_MODE
  //   //printf("Response char: %c\n", response); // [jo:231005] teste console DEV_MODE
	// } // task loop
  char* msg = ":200"; 
  char start;
  while(1) {
    led_invert(); // toggle led state
    // start = getchar_timeout_us(1000); // wait for 1 second for input
    // if(start == 's' || start == 'S') {
    // printf("Sending %s \n", msg);
    // UARTSend(0, (uint8_t*)msg, 4); // send to UART0
    // }
     // wait 1 second
    vTaskDelay(DELAY_500MS); // wait 500 ms
  }
} //taskBlinkLed

static void setupHardware(void) {

	// init onboard led
	led_init();

  // inicializa stdin, stdout e stderr no USB c/ default baud rate de 115200
  stdio_usb_init();

  // inicializa UARTs para comunicação com os PICs
  UARTInit(0, UART_BAUD); // UART0
  UARTInit(1, UART_BAUD); // UART1

	printf("Hardware setup completed.\n");
} // setupHardware

static void initComponents(void) {

  // communication between tasks
  qControlCommands = xQueueCreate(CONTROL_Q_SIZE, sizeof(tpr_setPoint));
  qCommTxPIC = xQueueCreate(PIC_Q_SIZE, sizeof(pic_TxData));
  qCommDev = xQueueCreate(DEV_Q_SIZE, sizeof(char));

  // init components
  com_init(); // communication PC
  pic_init(); // communication PIC
  ctl_init(); // commant interpreter
  tcl_init(); // trajectory control
  tst_init(); // trajectory state
  tpr_init(); // trajectory program

} // initComponents

/**
 * Program entry point 
 */

// test data for ReadRegister: read reg 1 (CoordY)
uint8_t msgReadRegister[] = {0x3a, 0x00, 0x00, 0x30, 0x33, 0x00, 0x00, 0x30, 0x31, 0x33, 0x3c, 0x0d, 0x0a};
// test data for WriteRegister: write reg 0 (START NC PROGRAM)
uint8_t msgWriteRegister[] = {0x3a, 0x30, 0x31, 0x30, 0x36, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x30, 0x0d, 0x0a};

int main(void) {
	int i;
	char ch;

  // // Define task handles
  TaskHandle_t handleLed; // [jo:230929] no pico w o cyw43 precisa rodar sempre num único core

	// //MB+ init Console(debug)
	// printf("nao apague esta linha\n");

	// init hardware
	setupHardware();

	// init components
	initComponents(); // init Modbus

	// /* 
	//  * Start the tasks defined within this file/specific to this demo. 
	//  */
	xTaskCreate( taskBlinkLed, "BlinkLed", USERTASK_STACK_SIZE, NULL, tskIDLE_PRIORITY, &handleLed);
	xTaskCreate( taskController, "Controller", USERTASK_STACK_SIZE, NULL, 1, NULL );
	xTaskCreate( taskNCProcessing, "NCProcessing", USERTASK_STACK_SIZE, NULL, 1, NULL );
	xTaskCreate( taskCommPIC, "CommPIC", USERTASK_STACK_SIZE, NULL, tskIDLE_PRIORITY, NULL );

  // /* 
	//  * Start the scheduler. 
	//  */
	vTaskStartScheduler();


	/* 
	 * Will only get here if there was insufficient memory to create the idle task. 
	 */
	return 1;
} // main