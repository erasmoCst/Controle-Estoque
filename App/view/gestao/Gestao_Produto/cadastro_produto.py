from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from models.produto import Produto
from config.DBConnection import *
from tkinter.messagebox import showinfo
from sqlalchemy.exc import IntegrityError


def cadastro_produto():
    # Funcção para o cadastro de produto
    cadastro_produto = Toplevel()
    cadastro_produto.title("Cadastro de Produto")
    cadastro_produto.geometry("560x300")
    cadastro_produto.configure(background="#dde")

    # Campo do nome do produto
    # Texto
    Label(cadastro_produto, text="Nome do Produto:", background="#dde", anchor="w").place(x=10, y=30, width=110, height=20)
    # Campo de preenchimento (entrada)
    nome_produto_entry = Entry(cadastro_produto) 
    nome_produto_entry.place(x=150, y= 30, width=110, height=20)           

    # Campo do Tipo de Embalagem
    # Texto
    Label(cadastro_produto, text="Tipo de Embalagem:", background="#dde", anchor="w").place(x= 10, y= 60, width=110, height=20) 
    # Campo de preenchimento (entrada)
    embalagem_var = StringVar(cadastro_produto)
    embalagem_var.set("Selecione")  # Valor padrão
    embalagem_options = ["Granel", "Ensacado"]
    embalagem_dropdown = OptionMenu(cadastro_produto, embalagem_var, *embalagem_options)
    embalagem_dropdown.place(x=150, y= 60)

    # Campo para Descricao do Produto
    #Texto
    Label(cadastro_produto, text="Descrição do Produto:", background="#dde",anchor="w").place(x=10, y= 90, width=120, height=20)
    ds_produto_entry = Entry(cadastro_produto)
    ds_produto_entry.place(x=150, y= 90, width=400, height=20)

    def registro_produto_BD():
        #Obter os valores dos campos de entrada
        nome_produto = nome_produto_entry.get()
        if(embalagem_var.get() == "Granel"): 
            tipo_embalagem = "G"
        else:
            tipo_embalagem = "E"
        descricao_produto = ds_produto_entry.get()

        #Criar uma nova instancia de produto
        novo_produto = Produto(nm_produto = nome_produto, tp_embalagemproduto = tipo_embalagem, ds_produto = descricao_produto)

        # Realizando a insercão dos dados coletados no BANCO DE DADOS
        try:
            session.add(novo_produto)
            session.commit()
            showinfo("Cadastro de Produto", "Cadastro realizado com sucesso!")
        except IntegrityError:
            session.rollback()
            showinfo("Cadastro de Produto", "Erro: Ocorreu uma violação de integridade. Verifique os dados inseridos.")
        except Exception as e:
            session.rollback()
            showinfo("Cadastro de Produto", f"Erro inesperado:{str (e)}")

        # Limpar os campos de entrada após a inserção
        nome_produto_entry.get(0, END)
        embalagem_var.get(0, END)
        ds_produto_entry(0, END)
    
        # Botao para inserir os dados
    Register = Button(cadastro_produto, text="Registrar", width=30, command=registro_produto_BD)
    Register.place(x=150, y=225)