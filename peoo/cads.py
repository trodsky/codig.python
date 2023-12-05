import tkinter as tk
from tkinter import messagebox
import datetime

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    data_nascimento = entry_data_nascimento.get()

    if not nome or not email or not senha or not data_nascimento:
        messagebox.showwarning("Cadastro", "Por favor, preencha todos os campos.")
        return


    dados_usuario = f"Nome: {nome}\nE-mail: {email}\nSenha: {senha}\nData de Nascimento: {data_nascimento}\n"

    with open("cadastros.txt", "a") as arquivo:
        arquivo.write(dados_usuario)
        arquivo.write("\n")

    messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")

janela = tk.Tk()
janela.title("Cadastro de Usuário")

tk.Label(janela, text="Nome:").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="E-mail:").pack()
entry_email = tk.Entry(janela)
entry_email.pack()

tk.Label(janela, text="Senha:").pack()
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

tk.Label(janela, text="Data de Nascimento:").pack()
entry_data_nascimento = tk.Entry(janela)
entry_data_nascimento.pack()


botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar)
botao_cadastrar.pack()


janela.mainloop()
