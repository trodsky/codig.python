import tkinter as tk

def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

def clear():
    entry.delete(0, tk.END)

# Criar a janela principal
window = tk.Tk()
window.title("Calculadora")

# Entrada
entry = tk.Entry(window, width=16, font=('Arial', 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 16),
              command=lambda b=button: press(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botão de Limpar
tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 16), command=clear).grid(row=row_val, column=col_val)

# Executar o loop principal
window.mainloop()
