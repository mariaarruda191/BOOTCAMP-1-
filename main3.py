
# Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
import tkinter as tk
from tkinter import messagebox

def calcular(operacao):
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())

        if operacao == '+':
            resultado.set(a + b)
        elif operacao == '-':
            resultado.set(a - b)
        elif operacao == '*':
            resultado.set(a * b)
        elif operacao == '/':
            if b == 0:
                resultado.set("Erro")
                messagebox.showerror("Erro", "Divisão por zero não é permitida.")
            else:
                resultado.set(a / b)
    except ValueError:
        resultado.set("Erro")
        messagebox.showerror("Erro", "Por favor, insira números válidos.")
        
        janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x250")
janela.resizable(False, False)

tk.Label(janela, text="Número 1:").pack(pady=5)
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Número 2:").pack(pady=5)
entrada2 = tk.Entry(janela)
entrada2.pack()

resultado = tk.StringVar()
tk.Label(janela, text="Resultado:").pack(pady=5)
tk.Label(janela, textvariable=resultado, font=("Arial", 14), fg="blue").pack()

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="+", width=5, command=lambda: calcular('+')).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="-", width=5, command=lambda: calcular('-')).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="*", width=5, command=lambda: calcular('*')).grid(row=0, column=2, padx=5)
tk.Button(frame_botoes, text="/", width=5, command=lambda: calcular('/')).grid(row=0, column=3, padx=5)
janela.mainloop()