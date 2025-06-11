import serial
import struct
from antlr4 import *
from GcodeLexer import GcodeLexer
from GcodeParser import GcodeParser
from GcodeListener import GcodeListener

def compute_lrc(data: bytes) -> bytes:
    """Calcula o LRC (Longitudinal Redundancy Check) para Modbus ASCII.""" #usado para poder verificar se houve algum problema durante a transmissão
    lrc = 0
    for b in data:
        lrc = (lrc + b) & 0xFF  # Soma os bytes, mantendo 8 bits
    lrc = ((-lrc) & 0xFF)  # Complemento de dois
    return bytes([lrc])

def to_ascii_hex(data: bytes) -> str:
    """Converte bytes binários em string ASCII hexadecimal."""
    return ''.join(f'{b:02X}' for b in data)

def build_modbus_fc21_ascii_request(unit_id, file_number, record_number, registers):
    function_code = 0x15  # Código da função 21 (Write File Record)
    reference_type = 0x06  # Tipo de referência Modbus
    record_length = len(registers)
    byte_count = 7 + 2 * record_length  # Cabeçalho (7) + 2 bytes por registrador

    # Monta sub-requisição com cabeçalho específico da função 21
    subreq_header = struct.pack('>BHHH', reference_type, file_number, record_number, record_length)
    data = b''.join(struct.pack('>H', reg) for reg in registers)  # Dados em 16 bits big-endian
    payload = struct.pack('>BB', unit_id, function_code) + struct.pack('B', byte_count) + subreq_header + data

    lrc = compute_lrc(payload)  # Calcula LRC da mensagem
    ascii_frame = ':' + to_ascii_hex(payload + lrc) + '\r\n'  # Monta frame ASCII completo
    return ascii_frame.encode('ascii')  # Converte para bytes ASCII para envio serial

def send_modbus_ascii_packet(port_name, packet):
    # Abre porta serial com configuração padrão Modbus ASCII
    with serial.Serial(port=port_name, baudrate=9600, bytesize=7, parity='E', stopbits=1, timeout=1) as ser:
        ser.write(packet)  # Envia o pacote ASCII
        response = ser.read_until(b'\r\n')  # Lê até o fim do frame ASCII
        return response.decode('ascii').strip()  # Retorna resposta como string limpa

def main():
    input_file = "example_triangle.gcode"
    port_name = "/dev/ttyUSB0" # Linux/Mac: algo como /dev/ttyUSB0 | Windows: COM3, COM4 etc.
    unit_id = 1  #ID setado no slave (RASP PI)
    file_number = 10
    start_record = 0  # Record inicial no arquivo Modbus

    # Lê o conteúdo do arquivo G-code
    with open(input_file, 'r', encoding='utf-8') as f:
        input_data = f.read()
    input_stream = InputStream(input_data)

    # Lexer e parser gerados por ANTLR
    lexer = GcodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GcodeParser(token_stream)
    tree = parser.gcode()

    # Caminha na árvore de análise para extrair registradores
    listener = GcodeListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Envia cada linha convertida para o escravo via ASCII
    for idx, regs in enumerate(listener.line_registers):
        packet = build_modbus_fc21_ascii_request(
            unit_id=unit_id,
            file_number=file_number,
            record_number=start_record + idx,
            registers=regs
        )
        response = send_modbus_ascii_packet(port_name, packet)
        print(f"Linha {idx+1} enviada. Resposta ASCII: {response}")

if __name__ == '__main__':
    main()