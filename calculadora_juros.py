import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funções de cálculo de juros
def calcular_juros_simples(principal, taxa_de_juros, tempo):
    return principal * (1 + (taxa_de_juros / 100) * tempo)

def calcular_juros_compostos(principal, taxa_de_juros, tempo):
    return principal * ((1 + (taxa_de_juros / 100)) ** tempo)

# Função que lida com a submissão dos dados e plotagem do gráfico
def calcular_e_plotar():
    try:
        p = float(principal_entry.get())
        r = float(taxa_de_juros_entry.get())
        t = int(tempo_entry.get())

        if p < 0 or r < 0 or t < 0:
            raise ValueError("Os valores devem ser positivos.")

        tempos = np.arange(t + 1)
        montantes_simples = [calcular_juros_simples(p, r, ano) for ano in tempos]
        montantes_compostos = [calcular_juros_compostos(p, r, ano) for ano in tempos]

        # Limpar gráfico anterior
        ax.clear()
        ax.plot(tempos, montantes_simples, label='Juros Simples')
        ax.plot(tempos, montantes_compostos, label='Juros Compostos')
        ax.set_title('Crescimento do Investimento ao Longo do Tempo')
        ax.set_xlabel('Tempo (anos)')
        ax.set_ylabel('Montante')
        ax.legend()
        canvas.draw()
    except ValueError as e:
        messagebox.showerror("Erro de entrada", f"Por favor, insira valores válidos. \n{e}")

def resetar_campos():
    principal_entry.delete(0, tk.END)
    taxa_de_juros_entry.delete(0, tk.END)
    tempo_entry.delete(0, tk.END)
    ax.clear()
    canvas.draw()

# Interface gráfica
app = tk.Tk()
app.title("Calculadora de Juros com Gráficos")

# Estilo
style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10))

# Widgets para entrada de dados
ttk.Label(app, text="Principal:").grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
principal_entry = ttk.Entry(app)
principal_entry.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(app, text="Taxa de Juros (%):").grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
taxa_de_juros_entry = ttk.Entry(app)
taxa_de_juros_entry.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(app, text="Tempo (anos):").grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
tempo_entry = ttk.Entry(app)
tempo_entry.grid(column=1, row=2, padx=10, pady=5)

# Botões para calcular e resetar
frame_buttons = ttk.Frame(app)
frame_buttons.grid(column=0, row=3, columnspan=2, pady=10)

calcular_button = ttk.Button(frame_buttons, text="Calcular e Plotar", command=calcular_e_plotar)
calcular_button.grid(column=0, row=0, padx=5)

resetar_button = ttk.Button(frame_buttons, text="Resetar", command=resetar_campos)
resetar_button.grid(column=1, row=0, padx=5)

# Área de gráfico
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=app)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

app.mainloop()
