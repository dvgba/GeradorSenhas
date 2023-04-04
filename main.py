import random
import string
import tkinter as tk 
from tkinter import ttk
from ttkbootstrap import Style

class GeradorSenhaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.style = Style()
        self.style.theme_use('yeti')
        self.title('Gerador de Senhas')
        self.geometry('400x200')
        self.resizable(False, False)

        self.lbl_comprimento = ttk.Label(self, text='Comprimento: ')
        self.lbl_comprimento.pack(pady=5)
        self.ent_comprimento = ttk.Entry(self, width=30)
        self.ent_comprimento.pack(pady=5)

        self.btn_gerar = ttk.Button(self, text='Gerar Senha', command=self.abrir_dialogo_nome)
        self.btn_gerar.pack(pady=10)

        self.txt_senha = tk.Text(self, height=1, width=30)
        self.txt_senha.pack(pady=10)

    def abrir_dialogo_nome(self):
        self.nome = tk.StringVar()
        self.nome_dialogo = tk.Toplevel()
        tk.Label(self.nome_dialogo, text="Digite um nome para a senha:").pack()
        tk.Entry(self.nome_dialogo, textvariable=self.nome).pack()
        tk.Button(self.nome_dialogo, text="Salvar", command=self.salvar_senha_dialogo).pack()

    def salvar_senha_dialogo(self):
        nome = self.nome.get()
        senha = self.gerar_senha(int(self.ent_comprimento.get()))
        self.salvar_senha(nome, senha)
        self.nome_dialogo.destroy()

    def gerar_senha(self, comprimento):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for i in range(comprimento))
        self.txt_senha.delete('1.0', tk.END)
        self.txt_senha.insert(tk.END, senha)
        return senha

    def salvar_senha(self, nome, senha):
        with open("senhas.txt", "a") as f:
            f.write(f"{nome}: {senha}\n")

if __name__ == '__main__':
  app = GeradorSenhaApp()
  app.mainloop()
      
