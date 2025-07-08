#ifndef __COMM_PIC_H
#define __COMM_PIC_H

/** struct for communication between TrajectoryControl
 *  and communication to PIC
 */

//#include "hardware/uart.h"
#include <stdint.h>
#include "uart.h"

typedef struct {
	uint8_t command;
	uint16_t setPointLeft;
	uint16_t setPointRight;
} pic_TxData;

// __attribute__((packed)) // ensure no padding bytes are added
typedef struct {
	int16_t controlEffort;
	int16_t controelEffortP;
	int16_t controlEffortI;
	int16_t controlEffortD;
	uint8_t state;

} pic_RxData;

void pic_init(void);
void pic_sendToPIC(pic_TxData data);
char pic_receiveCharFromPIC(uint8_t portNum);
void pic_receiveBufferFromPIC(uint8_t portNum, rx_buffer_t *rxBuffer);

#endif
