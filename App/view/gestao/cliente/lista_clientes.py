from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from tkinter import ttk

from models.pessoa_fisica import Pessoa_Fisica
from models.pessoa_juridica import Pessoa_Juridica
from models.pessoa import Pessoa

from config.DBConnection import *

def preencher_tv(tree):

    for i in tree.get_children():
        tree.delete(i)
        

    # Consulta os dados do Banco de dados
    pessoas = session.query(Pessoa, Pessoa.cd_pessoa, Pessoa.nm_pessoa, Pessoa.nr_telefone, Pessoa.nm_email).\
              order_by(Pessoa.nm_pessoa).all()

    # Adiciona os dados ao TreeView
    for pessoa in pessoas:
        tree.insert("", "end", values=(pessoa.Pessoa.cd_pessoa, pessoa.Pessoa.nm_pessoa, pessoa.Pessoa.nr_telefone, pessoa.Pessoa.nm_email))

def preencher_tv_pessoa_fisica(tree):
    for i in tree.get_children():
        tree.delete(i)

    # Consulta os dados do Banco de dados
    pessoas = session.query(Pessoa_Fisica, Pessoa_Fisica.cd_pessoa_fisica, Pessoa_Fisica.nr_cpf, Pessoa_Fisica.dt_nascimento, Pessoa_Fisica.tp_genero, Pessoa.nm_pessoa, Pessoa.nr_telefone, Pessoa.nm_email).\
          join(Pessoa, Pessoa_Fisica.cd_pessoa_fisica == Pessoa.cd_pessoa).\
          order_by(Pessoa_Fisica.cd_pessoa_fisica).all()

    # Adiciona os dados ao TreeView
    for pessoa in pessoas:
        tree.insert("", "end", values=(pessoa.cd_pessoa_fisica, pessoa.nm_pessoa, pessoa.nr_telefone, pessoa.nm_email))
    
def preencher_tv_pessoa_juridica(tree):
    for i in tree.get_children():
        tree.delete(i)

    # Consulta os dados do Banco de dados
    pessoas = session.query(Pessoa_Juridica, Pessoa_Juridica.cd_pessoa_juridica, Pessoa_Juridica.nr_cnpj, Pessoa_Juridica.nm_razaosocial, Pessoa.nm_pessoa, Pessoa.nr_telefone, Pessoa.nm_email).\
          join(Pessoa, Pessoa_Juridica.cd_pessoa_juridica == Pessoa.cd_pessoa).\
          order_by(Pessoa_Juridica.cd_pessoa_juridica).all()

    # Adiciona os dados ao TreeView
    for pessoa in pessoas:
        tree.insert("", "end", values=(pessoa.cd_pessoa_juridica, pessoa.nm_pessoa, pessoa.nr_telefone, pessoa.nm_email))
    

# Funcao para abrir a janela de listas de produtos
def lista_pessoas():

    # Função para abrir a janela de lista de produtos
    lista_pessoas = Toplevel()
    lista_pessoas.title("Lista de Clientes")
    lista_pessoas.geometry("1000x450")
    lista_pessoas.configure(background="#dde")

    def on_cliente_select(event):
        tipo_cliente = tp_cliente.get()
        if tipo_cliente == "Fisica":
            preencher_tv_pessoa_fisica(tview)
        elif tipo_cliente == "Juridica":
            preencher_tv_pessoa_juridica(tview)

    Label(lista_pessoas, text="Tipo de Cliente:", background="#dde", font=("Helvetica", 14)).place(x=10, y=30, width=200, height=20)
    tp_cliente = StringVar(lista_pessoas)
    tp_cliente.set("Selecione")  
    tp_cliente_options = ["Fisica", "Juridica"]
    tp_cliente_dropdown = OptionMenu(lista_pessoas, tp_cliente, *tp_cliente_options, command=on_cliente_select)
    tp_cliente_dropdown.place(x=10, y= 70)

    tview = ttk.Treeview(lista_pessoas, columns=("Matricula","Nome", "Telefone", "E-mail"), show='headings')
    tview.heading("Matricula", text="Matricula")
    tview.heading("Nome", text="Nome")
    tview.heading("Telefone", text="Telefone")
    tview.heading("E-mail", text="E-mail")

    tview.column('Matricula', minwidth=0, width=35)
    tview.column('Nome', minwidth=0, width=150)
    tview.column('Telefone', minwidth=0, width=35)
    tview.column('E-mail', minwidth=0, width=50)

    tview.pack(padx=10, ipadx=250,ipady=280,pady=80, anchor='n')
   
