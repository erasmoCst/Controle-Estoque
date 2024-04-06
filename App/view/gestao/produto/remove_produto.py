from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from sqlalchemy.exc import IntegrityError
from models.produto import Produto
from config.DBConnection import *

def remover_produto():
    # Função para a remoção de produto
    remocao_produto = Toplevel()
    remocao_produto.title("Remover Produto")
    remocao_produto.geometry("1000x500")
    remocao_produto.configure(background="#dde")

    # Label e Entry para inserir o código do produto a ser removido
    Label(remocao_produto, text="Código do Produto:", background="#dde").place(x=10, y=30)
    codigo_entry = Entry(remocao_produto)
    codigo_entry.place(x=150, y=30)

    # Função para remover o produto do banco de dados
    def remover_produto_bd():
        codigo = int(codigo_entry.get())
        produto = session.query(Produto).filter_by(cd_produto=codigo).first()
        if produto:
            try:
                session.delete(produto)
                session.commit()
                showinfo("Remover Produto", "Produto removido com sucesso!")
            except Exception as e:
                session.rollback()
                showinfo("Remover Produto", f"Erro inesperado: {str(e)}")
        else:
            showinfo("Remover Produto", "Produto não encontrado.")

    # Botão para remover o produto
    remover_button = Button(remocao_produto, text="Remover", command=remover_produto_bd)
    remover_button.place(x=150, y=60)

    # Label e Treeview para exibir todos os produtos cadastrados
    Label(remocao_produto, text="Produtos Cadastrados:", background="#dde").place(x=10, y=100)
    tree = ttk.Treeview(remocao_produto, columns=("ID", "Nome", "Descrição", "Embalagem", "Valor"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Descrição", text="Descrição")
    tree.heading("Embalagem", text="Embalagem")
    tree.heading("Valor", text="Valor")

    tree.column("ID", minwidth= 0, width=20)
    tree.column("Nome", minwidth= 0, width=200)
    tree.column("Descrição", minwidth= 0, width=350)
    tree.column("Embalagem", minwidth= 0, width=20)
    tree.column("Valor", minwidth= 0, width=15)

    tree.pack(padx=50, ipadx=190,ipady=240,pady=120, anchor='n') 

    # Populando a Treeview com os produtos cadastrados no banco de dados
    produtos = session.query(Produto).all()
    for produto in produtos:
        tree.insert("", "end", values=(produto.cd_produto, produto.nm_produto, produto.ds_produto, produto.tp_embalagemproduto, produto.vl_produto))
        