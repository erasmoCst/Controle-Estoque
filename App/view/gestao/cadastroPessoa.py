from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from App.models.DBClasses import Pessoa

from config.DBConnection import *
from tkinter.messagebox import showinfo

from sqlalchemy.exc import IntegrityError

#FUNCÕES DE "Cadastro de pessoa"

def cadastro_pessoa():
    # Função de cadastro de pessoa
    cadastro_pessoa = Toplevel()
    cadastro_pessoa.title("Cadastro de Pessoa")
    cadastro_pessoa.geometry("400x300")
    cadastro_pessoa.configure(background="#dde")

    # Campo Nome
    Label(cadastro_pessoa, text="Nome:", background="#dde", anchor="w").place(x=10, y=30, width=110, height=20)
    nome_entry = Entry(cadastro_pessoa)
    nome_entry.place(x=150, y=30, width=110, height=20)
    
    #Campo Endereço
    Label(cadastro_pessoa, text="Endereço:", background="#dde", anchor="w").place(x=10, y=60, width=110, height=20)
    endereco_entry = Entry(cadastro_pessoa)
    endereco_entry.place(x=150, y=60, width=110, height=20)
    
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