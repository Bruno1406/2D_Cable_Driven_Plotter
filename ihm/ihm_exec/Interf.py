import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Variáveis globais
dados_grafico = []
rodando = False
pausado = False

def abrir_arquivo():
    caminho = filedialog.askopenfilename()
    if caminho:
        print(f"Arquivo selecionado: {caminho}")

def send():
    print("Sinal SEND enviado.")

def start():
    global rodando, pausado
    rodando = True
    pausado = False
    print("Sinal START enviado.")

def pause():
    global pausado
    pausado = True
    print("Sinal PAUSE enviado.")

def abort():
    global rodando
    rodando = False
    print("Sinal ABORT enviado.")

def atualizar_grafico():
    if rodando and not pausado:
        novo_valor = random.randint(0, 10)
        dados_grafico.append(novo_valor)
        if len(dados_grafico) > 50:
            dados_grafico.pop(0)
        linha.set_ydata(dados_grafico + [None] * (50 - len(dados_grafico)))
        canvas.draw()
    janela.after(500, atualizar_grafico)

# Janela principal
janela = tk.Tk()
janela.title("Interface IHM")
janela.geometry("1000x600")

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

# Gráfico com matplotlib
fig, ax = plt.subplots()
ax.set_title("Dados recebidos")
ax.set_xlim(0, 50)
ax.set_ylim(0, 10)
ax.grid(True)
linha, = ax.plot([None]*50, lw=2)

canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Atualiza o gráfico a cada 500ms
janela.after(500, atualizar_grafico)

# Inicia a interface
janela.mainloop()