import tkinter as tk
from tkinter import filedialog
from antlr4 import *
from ihm.Grammar_antlr.GcodeLexer import GcodeLexer
from ihm.Grammar_antlr.GcodeParser import GcodeParser
from ihm.Grammar_antlr.GcodeListener import GcodeListener
import ihm.ihm_exec.modbus_ascii as modbus
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

unit_id = 1 #ID setado no slave, pode ser qualquer valor
file_number = 0
start_record = 0
port_name = "/dev/ttyACM0"

  # Linux/Mac: algo como /dev/ttyUSB0 | Windows: COM3, COM4 etc.

gcode_registers = []

rodando = False
pausado = False
pontos_grafico = []


gcode_text = ""  # variável global para armazenar o texto do G-code

def abrir_arquivo():
    global gcode_registers, gcode_text
    caminho = filedialog.askopenfilename(filetypes=[("G-code files", "*.gcode")])
    if caminho:
        print(f"Arquivo selecionado: {caminho}")
        with open(caminho, 'r', encoding='utf-8') as f:
            gcode_text = f.read()
        print("Conteúdo do G-code:")
        print(gcode_text)  # imprime o conteúdo do arquivo
        
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

def start():
    global rodando, pausado
    rodando = True
    pausado = False
    packet = modbus.build_fc6_write_single(unit_id, 0, 1) #Considerei que caso valor 1 
    response = modbus.send_ascii_packet(port_name, packet)
    print(f"Start: {response}")

def pause():
    global pausado
    pausado = True
    packet = modbus.build_fc6_write_single(unit_id, 2, 1) #Considerei que caso valor 1 no registrador 2 a máquina pausa, mas pode voltar a funcionar e terminar o processo
    response = modbus.send_ascii_packet(port_name, packet) 
    print(f"Pause: {response}")

def abort():
    global rodando
    rodando = False
    packet = modbus.build_fc6_write_single(unit_id, 3, 1) #Considerei que caso valor 1 no registrador 3 a maquina para e não pode continuar a ler de novo
    response = modbus.send_ascii_packet(port_name, packet)
    print(f"Abort: {response}")

# Janela principal
janela = tk.Tk()
janela.title("Interface IHM")
janela.geometry("1000x600")

# Gráfico com matplotlib
fig, ax = plt.subplots()
ax.set_title("Dados recebidos")
ax.set_xlim(0, 50)
ax.set_ylim(0, 10)
ax.grid(True)
linha, = ax.plot([None]*50, lw=2)

canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def atualizar():
    global pontos_grafico
    if rodando and not pausado:
        # Monta o pacote Modbus para leitura dos registradores 4 e 5
        packet = modbus.build_fc3_read_registers(unit_id, 4, 2)
        response = modbus.send_ascii_packet(port_name, packet)
        print(f"Leitura R4-R5: {response}")

        if response.startswith(':') and len(response) >= 11:
            try:
                raw_data_hex = response[1:-4]
                data_hex = raw_data_hex[6:]

                if len(data_hex) == 8:
                    x_hex = data_hex[0:4]
                    y_hex = data_hex[4:8]

                    x = int(x_hex, 16)
                    y = int(y_hex, 16)

                    novo_ponto = (x, y)

                    # Evita adicionar pontos consecutivos iguais
                    if not pontos_grafico or pontos_grafico[-1] != novo_ponto:
                        pontos_grafico.append(novo_ponto)
                        print(f"Ponto adicionado: x={x}, y={y}")

                        if len(pontos_grafico) > 100:
                            pontos_grafico.pop(0)

                    # Atualiza o gráfico
                    x_vals = [p[0] for p in pontos_grafico]
                    y_vals = [p[1] for p in pontos_grafico]
                    linha.set_data(x_vals, y_vals)

                    ax.relim()
                    ax.autoscale_view()

                    canvas.draw()
            except Exception as e:
                print(f"Erro ao processar resposta: {e}")

# Frame horizontal para os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

# Estilo dos botões
estilo = {"width": 15, "height": 3, "font": ("Arial", 12)}

# Botões lado a lado
tk.Button(frame_botoes, text="Open", command=abrir_arquivo, **estilo).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botoes, text="Send", command=send, **estilo).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botoes, text="Start", command=start, **estilo).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botoes, text="Pause", command=pause, **estilo).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botoes, text="Abort", command=abort, **estilo).pack(side=tk.LEFT, padx=10)

# Atualiza o gráfico a cada 500ms
janela.after(500, atualizar)

# Inicia a interface
janela.mainloop()