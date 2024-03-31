from tkinter import Button, Entry, Label, Toplevel, ttk
from controller.produto import consulta_todos_produtos_por_nome, lista_produtos

def preencher_tv(tree, nm_produto=None):
    for i in tree.get_children():
        tree.delete(i)

    produtos = lista_produtos() if not nm_produto else consulta_todos_produtos_por_nome(nm_produto)

    for produto in produtos['data']:
        tree.insert("", "end", values=(
            produto.cd_produto,
            produto.nm_produto,
            produto.ds_produto,
            "Ensacado" if produto.tp_embalagemproduto == "E" else "A granel"))


def busca_produto():
    busca_produto = Toplevel()
    busca_produto.title("Busca de Produtos")
    busca_produto.geometry("1000x500")
    busca_produto.configure(background="#dde")

    Label(busca_produto, text="Código Produto:", background="#dde", anchor="w").grid(row=0, column=0, padx=10)
    cd_produto_entry = Entry(busca_produto)
    cd_produto_entry.grid(row=1, column=0, padx=10)

    Label(busca_produto, text="Nome Produto:", background="#dde", anchor="w").grid(row=0, column=2, padx=10)
    nm_produto_entry = Entry(busca_produto)
    nm_produto_entry.grid(row=1, column=2, padx=10)

    tview = ttk.Treeview(busca_produto, columns=("ID", "Nome", "Descrição", "Embalagem"), show="headings")
    tview.heading("ID", text="ID")
    tview.heading("Nome", text="Nome")
    tview.heading("Descrição", text="Descrição")
    tview.heading("Embalagem", text="Embalagem")

    tview.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    preencher_tv(tview)

    Button(busca_produto, text="Consultar Código", command=None).grid(row=1, column=1)
    Button(busca_produto, text="Consultar Nome", command=lambda: preencher_tv(tview, nm_produto_entry.get())).grid(row=1, column=3)