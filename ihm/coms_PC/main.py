import serial
import struct
from antlr4 import *
from GcodeLexer import GcodeLexer
from GcodeParser import GcodeParser
from GcodeListener import GcodeListener

def compute_crc(data: bytes) -> bytes: # Cycle redundancy check , usado para poder verificar se houve algum problema durante a transmissão
    """Calcula o CRC-16 Modbus e retorna em little-endian."""
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return struct.pack('<H', crc)  # Little-endian

def build_modbus_fc21_rtu_request(unit_id, file_number, record_number, registers):
    function_code = 0x15  # FC21
    reference_type = 0x06
    record_length = len(registers)
    byte_count = 7 + 2 * record_length

    # Corpo do pacote (sem CRC)
    subreq_header = struct.pack('>BHHH', reference_type, file_number, record_number, record_length)
    data = b''.join(struct.pack('>H', reg) for reg in registers)
    payload = struct.pack('>BB', unit_id, function_code) + struct.pack('B', byte_count) + subreq_header + data

    # Adiciona o CRC em little-endian
    crc = compute_crc(payload)
    return payload + crc

def send_modbus_rtu_packet(port_name, packet):
    with serial.Serial(port=port_name, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1) as ser:
        ser.write(packet)
        response = ser.read(256)
        return response

def main():
    input_file = "example_triangle.gcode"
    port_name = "/dev/ttyUSB0"  # Linux/Mac: algo como /dev/ttyUSB0 | Windows: COM3, COM4 etc.
    unit_id = 1 # ID setado no slave (RASP Pi)
    file_number = 10
    start_record = 0  # Pode ser alterado conforme onde deseja iniciar

    # Leitura do G-code
    with open(input_file, 'r', encoding='utf-8') as f:
        input_data = f.read()
    input_stream = InputStream(input_data)

    # Análise sintática com ANTLR
    lexer = GcodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GcodeParser(token_stream)
    tree = parser.gcode()

    listener = GcodeListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Enviar cada linha como um registro separado
    for idx, regs in enumerate(listener.line_registers):
        packet = build_modbus_fc21_rtu_request(
            unit_id=unit_id,
            file_number=file_number,
            record_number=start_record + idx,
            registers=regs
        )
        response = send_modbus_rtu_packet(port_name, packet)
        print(f"Linha {idx+1} enviada. Resposta: {response.hex()}")

if __name__ == '__main__':
    main()