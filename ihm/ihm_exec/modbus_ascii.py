import serial
import struct

def compute_lrc(ascii_str: str) -> bytes:
    """Compute LRC over ASCII characters, e.g., 'FAA23E80'."""
    lrc = 0
    for c in ascii_str:
        lrc = (lrc + ord(c)) & 0xFF  # ord() gives ASCII value (like a C char)
    lrc = ((-lrc) & 0xFF)
    return bytes([lrc])

def to_ascii_hex(data: bytes) -> str:
    """Converte bytes binários em string ASCII hexadecimal."""
    return ''.join(f'{b:02X}' for b in data)

def build_fc21_write_file(unit_id, file_number, record_number, registers):
    """Constrói quadro ASCII Modbus FC21 (Write File Record)."""
    function_code = 0x15
    reference_type = 0x06
    record_length = len(registers)
    byte_count = 9 + 2 * record_length

    subreq_header = struct.pack('>BHHH', reference_type, file_number, record_number, record_length)
    data = b''.join(struct.pack('>h', reg) for reg in registers)
    payload = to_ascii_hex(struct.pack('>BB', unit_id, function_code) + struct.pack('B', byte_count) + subreq_header + data)
    lrc = to_ascii_hex(compute_lrc(payload))
    ascii_frame = ':' + payload + lrc + '\r\n'
    return ascii_frame.encode('ascii')

def build_fc6_write_single(unit_id, register_address, value): #Nesse código envia o registrador que quero escrever e qual o valor dele
    """Constrói quadro ASCII Modbus FC6 (Write Single Register)."""
    function_code = 0x06
    payload = to_ascii_hex(struct.pack('>B B H H', unit_id, function_code, register_address, value))

    lrc = to_ascii_hex(compute_lrc(payload))
    ascii_frame = ':' + (payload + lrc) + '\r\n'
    return ascii_frame.encode('ascii')

def build_fc3_read_registers(unit_id, start_address, quantity=1): #Nesse codigo envio o registrador que começo a ler no slave 
                                                                  #e quantos registradores a partir dele eu leio também 
    """Constrói quadro ASCII Modbus FC3 (Read Holding Registers)."""
    function_code = 0x03
    payload = to_ascii_hex(struct.pack('>B B H H', unit_id, function_code, start_address, quantity))

    lrc = to_ascii_hex(compute_lrc(payload))
    ascii_frame = ':' + (payload + lrc) + '\r\n'
    return ascii_frame.encode('ascii')

def send_ascii_packet(port_name, packet):
    """Envia pacote ASCII pela serial e retorna resposta."""
    with serial.Serial(port=port_name, baudrate=115200, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=20) as ser:
        ser.write(packet)
        response = ser.read_until(b'/r/n')  # Lê até encontrar o final do pacote
        print(f"Resposta recebida: {response.decode('ascii').strip()}")
        return response.decode('ascii').strip()

if __name__ == "__main__":
    # TESTES
    unit_id = 1
    file_number = 0
    record_number = 0
    registers = [0, 2300, 4000, 2, 2300, 4000, -800, 0]
    print(len(registers))
    packet = build_fc21_write_file(unit_id, file_number, record_number, registers)
    print(f'PACOTE TESTE: {packet}') 
    response = send_ascii_packet('/dev/ttyACM0', packet)  # Ajuste o nome da porta conforme necessário
    print(f"Resposta:\n {response}")