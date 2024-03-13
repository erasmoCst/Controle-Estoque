from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from models.DBClasses import Pessoa

from config.DBConnection import *
from tkinter.messagebox import showinfo

from sqlalchemy.exc import IntegrityError

#FUNCÕES DE "Cadastro de pessoa"

def cadastro_pessoa():
    # Função de cadastro de pessoa
    cadastro_pessoa = Toplevel()
    cadastro_pessoa.title("Cadastro de Pessoa")
    cadastro_pessoa.geometry("700x500")
    cadastro_pessoa.configure(background="#dde")

    # Campo Nome
    Label(cadastro_pessoa, text="Nome:", background="#dde", anchor="w").place(x=10, y=30, width=110, height=20)
    nome_entry = Entry(cadastro_pessoa)
    nome_entry.place(x=150, y=30, width=110, height=20)
    
    #Campo Endereço
    Label(cadastro_pessoa, text="Dados do Endereço:", background="#dde", anchor="w").grid(row=0, column=0, columnspan=3, sticky="w", padx=10, pady=10)

    # Criar um Label e Entry para "Logradouro"
    Label(cadastro_pessoa, background="#dde", text="Logradouro:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    endereco_entry = Entry(cadastro_pessoa)
    endereco_entry.grid(row=1, column=1, columnspan=4, padx=10, pady=5, sticky="w")

    # Criar um Label e Entry para "Número"
    Label(cadastro_pessoa, background="#dde", text="Número:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    numero_endereco_entry = Entry(cadastro_pessoa)  # Definir o tamanho do Entry para 10 caracteres
    numero_endereco_entry.grid(row=2, column=1, padx=10, pady=5)

    # Criar um Label e Entry para "Complemento"
    Label(cadastro_pessoa, background="#dde", text="Complemento:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
    complemento_endereco_entry = Entry(cadastro_pessoa)  # Definir o tamanho do Entry para 10 caracteres
    complemento_endereco_entry.grid(row=2, column=3, padx=10, pady=5)

    #Campo Telefone
    Label(cadastro_pessoa, text="Telefone:", background="#dde", anchor="w").place(x=10, y=90, width=110, height=20)
    telefone_entry = Entry(cadastro_pessoa)
    telefone_entry.place(x=150, y=90, width=110, height=20)

    #Campo E-mail
    Label(cadastro_pessoa, text="E-mail:", background="#dde", anchor="w").place(x=10, y=120, width=110, height=20)
    email_entry = Entry(cadastro_pessoa)
    email_entry.place(x=150, y=120, width=110, height=20)

    def registro_pessoa_BD():
    
        # dados do usuário
        pessoa_nome = nome_entry.get()
        pessoa_endereco = endereco_entry.get()
        pessoa_telefone = telefone_entry.get()
        pessoa_email = email_entry.get()

        # 
        nova_pessoa = session.execute(
            text("INSERT INTO PESSOA(nm_pessoa, cd_endereco, nr_telefone,nm_email) VALUES (?, ?, ?, ?)"),
            (pessoa_nome, pessoa_endereco, pessoa_telefone, pessoa_email)
        )

        
        Pessoa(nova_pessoa)
        session.commit()

        # mensagem de confirmação para o usuário
        Message.info(title="Informação de registro", message="Registro concluído.")
        

    Register = Button(cadastro_pessoa, text="Registrar", width=30, command=registro_pessoa_BD)
    Register.place(x=100, y=225)