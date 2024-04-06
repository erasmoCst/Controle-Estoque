from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from sqlalchemy.exc import IntegrityError

from models.pessoa_juridica import Pessoa_Juridica
from models.pessoa_fisica import Pessoa_Fisica
from models.pessoa import Pessoa
from config.DBConnection import *

def preencher_tv_pessoa_fisica(tree):
        for i in tree.get_children():
            tree.delete(i)

        pessoas = session.query(Pessoa_Fisica, Pessoa_Fisica.cd_pessoa_fisica, Pessoa_Fisica.nr_cpf, Pessoa_Fisica.dt_nascimento, Pessoa_Fisica.tp_genero, Pessoa.nm_pessoa, Pessoa.nr_telefone, Pessoa.nm_email).\
            join(Pessoa, Pessoa_Fisica.cd_pessoa_fisica == Pessoa.cd_pessoa).\
            order_by(Pessoa_Fisica.cd_pessoa_fisica).all()

        for pessoa in pessoas:
            tree.insert("", "end", values=(pessoa.cd_pessoa_fisica, pessoa.nm_pessoa, pessoa.nr_telefone, pessoa.nm_email))

def remover_cliente_fisico():
    remover_cliente_fisico = Toplevel()
    remover_cliente_fisico.title("Remover Cliente Pessoa Fisica")
    remover_cliente_fisico.geometry("1000x500")
    remover_cliente_fisico.configure(background="#dde")

    Label(remover_cliente_fisico, text="Matricula(ID) Cliente:", background="#dde").place(x=10, y=30)
    codigo_entry = Entry(remover_cliente_fisico)
    codigo_entry.place(x=150, y=30)


    def remover_cliente_fisico_bd():
        codigo = int(codigo_entry.get())
        pessoa = session.query(Pessoa_Fisica).filter_by(cd_pessoa_fisica=codigo).first()
        if pessoa:
            try:
                session.delete(pessoa)
                session.commit()
                showinfo("Remover Cliente", "Cliente removido com sucesso!")
            except Exception as e:
                session.rollback()
                showinfo("Remover Cliente", f"Erro inesperado: {str(e)}")
        else:
            showinfo("Remover Cliente", "Cliente não encontrado.")

    remover_button = Button(remover_cliente_fisico, text="Remover", command=remover_cliente_fisico_bd)
    remover_button.place(x=150, y=60)
    
    tview = ttk.Treeview(remover_cliente_fisico, columns=("Matricula","Nome", "Telefone", "E-mail"), show='headings')
    tview.heading("Matricula", text="Matricula")
    tview.heading("Nome", text="Nome")
    tview.heading("Telefone", text="Telefone")
    tview.heading("E-mail", text="E-mail")

    tview.column('Matricula', minwidth=0, width=35)
    tview.column('Nome', minwidth=0, width=150)
    tview.column('Telefone', minwidth=0, width=35)
    tview.column('E-mail', minwidth=0, width=50)

    tview.pack(padx=10, ipadx=250,ipady=280,pady=100, anchor='n')

    preencher_tv_pessoa_fisica(tview)

def preencher_tv_pessoa_juridica(tree):
    for i in tree.get_children():
        tree.delete(i)

    # Consulta os dados do Banco de dados
    pessoas = session.query(Pessoa_Juridica, Pessoa_Juridica.cd_pessoa_juridica, Pessoa_Juridica.nr_cnpj, Pessoa_Juridica.nm_razaosocial, Pessoa.nm_pessoa, Pessoa.nr_telefone, Pessoa.nm_email).\
          join(Pessoa, Pessoa_Juridica.cd_pessoa_juridica == Pessoa.cd_pessoa).\
          order_by(Pessoa_Juridica.cd_pessoa_juridica).all()

    for pessoa in pessoas:
        tree.insert("", "end", values=(pessoa.cd_pessoa_juridica, pessoa.nm_pessoa, pessoa.nr_telefone, pessoa.nm_email, pessoa.nm_razaosocial))

def remover_cliente_juridico():
    # Função para a remoção de produto
    remover_cliente_juridico = Toplevel()
    remover_cliente_juridico.title("Remover Cliente Pessoa Juridica")
    remover_cliente_juridico.geometry("1000x500")
    remover_cliente_juridico.configure(background="#dde")

    Label(remover_cliente_juridico, text="Matricula(ID) Cliente:", background="#dde").place(x=10, y=30)
    codigo_entry = Entry(remover_cliente_juridico)
    codigo_entry.place(x=150, y=30)

    def remover_cliente_juridico_bd():
        codigo = int(codigo_entry.get())
        pessoa = session.query(Pessoa_Juridica).filter_by(cd_pessoa_juridica=codigo).first()
        if pessoa:
            try:
                session.delete(pessoa)
                session.commit()
                showinfo("Remover Cliente", "Cliente removido com sucesso!")
            except Exception as e:
                session.rollback()
                showinfo("Remover Cliente", f"Erro inesperado: {str(e)}")
        else:
            showinfo("Remover Cliente", "Cliente não encontrado.")

    remover_button = Button(remover_cliente_juridico, text="Remover", command=remover_cliente_juridico_bd)
    remover_button.place(x=150, y=60)

    
    tview = ttk.Treeview(remover_cliente_juridico, columns=("Matricula","Nome", "Telefone", "E-mail", "Razão social"), show='headings')
    tview.heading("Matricula", text="Matricula")
    tview.heading("Nome", text="Nome")
    tview.heading("Telefone", text="Telefone")
    tview.heading("E-mail", text="E-mail")
    tview.heading("Razão social", text="Razão social")

    tview.column('Matricula', minwidth=0, width=35)
    tview.column('Nome', minwidth=0, width=150)
    tview.column('Telefone', minwidth=0, width=35)
    tview.column('E-mail', minwidth=0, width=50)
    tview.column('Razão social', minwidth=0, width=60)

    tview.pack(padx=10, ipadx=250,ipady=280,pady=100, anchor='n')

    preencher_tv_pessoa_juridica(tview)