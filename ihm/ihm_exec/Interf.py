import tkinter as tk
from tkinter import filedialog
from antlr4 import *
from ihm.Grammar_antlr.GcodeLexer import GcodeLexer
from ihm.Grammar_antlr.GcodeParser import GcodeParser
from ihm.Grammar_antlr.GcodeListener import GcodeListener
import ihm.ihm_exec.modbus_ascii as modbus
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque

unit_id = 1
file_number = 0
start_record = 0
calibrate_record = 1
park_record = 2
port_name = "/dev/ttyACM0"

gcode_registers = []
rodando = False
pausado = False

# --- OTIMIZAÇÃO: Usar deque para gerenciar os pontos do gráfico ---
# Deque é mais rápido para adicionar/remover itens dos extremos.
# Definimos o tamanho máximo para a janela de 30 segundos (30s / 0.05s = 600 pontos)
MAX_PONTOS = 100 
pontos_ce = deque(maxlen=MAX_PONTOS)
pontos_cep = deque(maxlen=MAX_PONTOS)
pontos_cei = deque(maxlen=MAX_PONTOS)
pontos_ced = deque(maxlen=MAX_PONTOS)
# ------------------------------------------------------------------

# Registradores de Leitura Modbus
REG_X = 0
REG_Y = 1
REG_Z = 2
REG_LINHA = 3
REG_PIC0_STATE = 4
REG_PIC0_CE = 5
REG_PIC0_CEP = 6
REG_PIC0_CEI = 7
REG_PIC0_CED = 8
REG_PIC1_STATE = 9
REG_PIC1_CE = 10
REG_PIC1_CEP = 11
REG_PIC1_CEI = 12
REG_PIC1_CED = 13

gcode_text = ""  # variável global para armazenar o texto do G-code

def abrir_arquivo():
    global gcode_registers, gcode_text
    caminho = filedialog.askopenfilename(filetypes=[("G-code files", "*.gcode")])
    if caminho:
        print(f"Arquivo selecionado: {caminho}")
        with open(caminho, 'r', encoding='utf-8') as f:
            gcode_text = f.read()
        print("Conteúdo do G-code:")
        print(gcode_text)
        
        input_stream = InputStream(gcode_text)
        lexer = GcodeLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = GcodeParser(token_stream)
        tree = parser.gcode()
        listener = GcodeListener()
        ParseTreeWalker().walk(listener, tree)
        gcode_registers = listener.line_registers
        print(gcode_registers)
        print("G-code processado.")

def send():
    packet = modbus.build_fc21_write_file(unit_id, file_number, start_record, gcode_registers)
    response = modbus.send_ascii_packet(port_name, packet)
    print(f"Linha: {response}")
    
def pause():
    global pausado
    pausado = True
    packet = modbus.build_fc6_write_single(unit_id, 2, 1)
    response = modbus.send_ascii_packet(port_name, packet) 
    print(f"Pause: {response}")

def abort():
    global rodando
    rodando = False
    packet = modbus.build_fc6_write_single(unit_id, 3, 1)
    response = modbus.send_ascii_packet(port_name, packet)
    print(f"Abort: {response}")

def on_closing():
    """Função chamada quando o usuário fecha a janela."""
    global rodando
    print("Fechando a aplicação...")
    rodando = False  # Garante que o loop de atualização pare
    janela.destroy() # Destrói a janela e encerra o mainloop

def start():
    global rodando, pausado
    rodando = True
    pausado = False
    # Limpa os dados antigos do gráfico ao iniciar
    pontos_ce.clear()
    pontos_cep.clear()
    pontos_cei.clear()
    pontos_ced.clear()
    packet = modbus.build_fc6_write_single(unit_id, start_record, 1)
    response = modbus.send_ascii_packet(port_name, packet)
    print(f"Start: {response}")
    atualizar()

def calibrate():
    global rodando, pausado
    rodando = True
    pausado = False
    packet = modbus.build_fc6_write_single(unit_id, calibrate_record, 1)
    response = modbus.send_ascii_packet(port_name, packet)
    print(f"Calibrate: {response}")

def park():
    global rodando, pausado
    rodando = True
    pausado = False
    packet = modbus.build_fc6_write_single(unit_id, park_record, 1)
    response = modbus.send_ascii_packet(port_name, packet)
    print(f"Park: {response}")

# Função para converter valor hexadecimal de 16 bits com sinal
def hex_to_signed_int(hex_str):
    val = int(hex_str, 16)
    if (val & 0x8000): # Verifica o bit de sinal
        val -= 0x10000 # Converte para negativo
    return val

# Janela principal
janela = tk.Tk()
janela.title("Interface IHM - Calibração de Controlador")
janela.geometry("1000x600")

# Configuração do Gráfico
fig, ax = plt.subplots()
ax.set_title("Esforço de Controle (PIC 0)")
ax.set_xlabel("Amostras (últimos 30 segundos)")
ax.set_ylabel("Valor")
ax.grid(True)
linha_ce, = ax.plot([], lw=2, label='CE Total')
linha_cep, = ax.plot([], lw=1, linestyle='--', label='CEP')
linha_cei, = ax.plot([], lw=1, linestyle='--', label='CEI')
linha_ced, = ax.plot([], lw=1, linestyle='--', label='CED')
ax.legend()
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def extrair_valor_da_resposta(response):
    """Função auxiliar para extrair o valor de uma resposta Modbus FC03 para um registrador."""
    # --- CORREÇÃO PRINCIPAL ---
    # Resposta para 1 registrador (2 bytes) tem 4 caracteres hex. Ex: :010302ABCDLRC
    # O comprimento total da string é 13.
    if response.startswith(':') and len(response) >= 13:
        data_hex = response[7:11]  # CORRETO: Extrai 4 caracteres de dados
        return hex_to_signed_int(data_hex)
    return None

def atualizar():
    if rodando and not pausado:
        try:
            # --- NOVO: Validação dos dados lendo o estado primeiro ---
            packet_state = modbus.build_fc3_read_registers(unit_id, REG_PIC0_STATE, 1)
            response_state = modbus.send_ascii_packet(port_name, packet_state)
            state = extrair_valor_da_resposta(response_state)

            if state != 49: # 49 é o código ASCII para '1'
                print(f"Dados inválidos recebidos. Estado={state} (esperado 49). Descartando amostra.")
                # Agenda a próxima chamada e interrompe a execução atual
                janela.after(100, atualizar)
                return 
            
            # Se o estado for válido, prossiga com a leitura dos outros dados
            packet_ce = modbus.build_fc3_read_registers(unit_id, REG_PIC0_CE, 1)
            response_ce = modbus.send_ascii_packet(port_name, packet_ce)
            ce = extrair_valor_da_resposta(response_ce)
            
            packet_cep = modbus.build_fc3_read_registers(unit_id, REG_PIC0_CEP, 1)
            response_cep = modbus.send_ascii_packet(port_name, packet_cep)
            cep = extrair_valor_da_resposta(response_cep)

            packet_cei = modbus.build_fc3_read_registers(unit_id, REG_PIC0_CEI, 1)
            response_cei = modbus.send_ascii_packet(port_name, packet_cei)
            cei = extrair_valor_da_resposta(response_cei)

            packet_ced = modbus.build_fc3_read_registers(unit_id, REG_PIC0_CED, 1)
            response_ced = modbus.send_ascii_packet(port_name, packet_ced)
            ced = extrair_valor_da_resposta(response_ced)
            
            if all(v is not None for v in [ce, cep, cei, ced]):
                print(f"Valores lidos: CE={ce}, CEP={cep}, CEI={cei}, CED={ced}")

                # Adiciona os novos pontos. O deque remove o mais antigo automaticamente.
                pontos_ce.append(ce)
                pontos_cep.append(cep)
                pontos_cei.append(cei)
                pontos_ced.append(ced)

                # Atualiza o gráfico
                eixo_x = range(len(pontos_ce))
                linha_ce.set_data(eixo_x, list(pontos_ce))
                linha_cep.set_data(eixo_x, list(pontos_cep))
                linha_cei.set_data(eixo_x, list(pontos_cei))
                linha_ced.set_data(eixo_x, list(pontos_ced))

                # Ajusta os limites do eixo X para o número de pontos
                ax.set_xlim(0, MAX_PONTOS)
                
                # Ajusta os limites do eixo Y dinamicamente (autoscale)
                ax.relim()
                ax.autoscale_view(scalex=False, scaley=True) # Autoscala apenas o eixo Y
                
                canvas.draw()
            else:
                print("Falha ao ler um ou mais registradores do PIC0.")

        except Exception as e:
            print(f"Erro durante a comunicação Modbus: {e}")

    # Agenda a próxima atualização
    janela.after(100, atualizar)

# --- Frame e Botões (sem alterações) ---
# --- Botões ---
# Frame principal que conterá as duas linhas de botões
frame_container = tk.Frame(janela)
frame_container.pack(pady=10)

# Primeira linha de botões
frame_botoes_1 = tk.Frame(frame_container)
frame_botoes_1.pack()

# Segunda linha de botões
frame_botoes_2 = tk.Frame(frame_container)
frame_botoes_2.pack(pady=5) # Adiciona um pequeno espaço entre as linhas

estilo = {"width": 15, "height": 2, "font": ("Arial", 12)}

# Adiciona os 4 botões de setup/calibração na primeira linha
tk.Button(frame_botoes_1, text="Open", command=abrir_arquivo, **estilo).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botoes_1, text="Send", command=send, **estilo).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botoes_1, text="Calibrate", command=calibrate, **estilo).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botoes_1, text="Park", command=park, **estilo).pack(side=tk.LEFT, padx=10)

# Adiciona os 3 botões de controle na segunda linha
tk.Button(frame_botoes_2, text="Start", command=start, **estilo).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botoes_2, text="Pause", command=pause, **estilo).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botoes_2, text="Abort", command=abort, **estilo).pack(side=tk.LEFT, padx=10)

janela.protocol("WM_DELETE_WINDOW", on_closing)
janela.mainloop()