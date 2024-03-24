from tkinter import Button, Entry, Label, Toplevel, ttk


    # Função para preencher o treeview 
def preencher_tv(tree):
    # for para limpar os dados do treeview, necessario em casos de buscas
    for i in tree.get_children():
        tree.delete(i)

    # Consultar os produtos do Banco de dados
    produtos = "teste"

    # adicionar os dados do produtos no TreeV  ordem alfab.
    # for produto in produtos:
    #     tree.insert("","end", values=(produto.cd_produto,produto.nm_produto, produto.ds_produto, produto.tp_embalagemproduto))


def itens_pedido(dados_cliente):
    itens_pedido = Toplevel()
    itens_pedido.title("Itens do Pedido")
    itens_pedido.geometry("700x500")
    itens_pedido.configure(background="#dde")

    Label(itens_pedido, text=f"Cód. Cliente: {dados_cliente.cd_pessoa}", background='#dde', anchor="w").grid(row=0, column=1, pady=10)
    Label(itens_pedido, text=f"Nome do Cliente: {dados_cliente.nm_pessoa}", background='#dde', anchor="w").grid(row=0, column=2, pady=10)

    Label(itens_pedido, text="Código produto:", background='#dde', anchor="w").grid(row=1, column=0)
    id_entry = Entry(itens_pedido)
    id_entry.grid(row=1, column=1)

    Label(itens_pedido, text="Quantidade:", background='#dde', anchor="w").grid(row=1, column=2)
    qt_prod_entry  = Entry(itens_pedido)
    qt_prod_entry.grid(row=1, column=3)

    def adicionar_produto():
        pass
    
    Button(itens_pedido, text="Adicionar ao Pedido", command=None).grid(row=2, column=0, padx=10, pady=10)

    # Criacao da TreeView para exibir os prodts
    tview = ttk.Treeview(itens_pedido, columns=("ID","Nome", "Descrição", "Embalagem"), show='headings')
    tview.heading("ID", text="ID")
    tview.heading("Nome", text="Nome")
    tview.heading("Descrição", text="Descrição")
    tview.heading("Embalagem", text="Embalagem")
    #Tam. colunas
    tview.column('ID', minwidth=0, width=5)
    tview.column('Nome', minwidth=0, width=200)
    tview.column('Descrição', minwidth=0, width=420)
    tview.column('Embalagem', minwidth=0, width=10)
    # Ocultando a primeira coluna
    # tview.column("#0", width=0, stretch=NO)

    # Preencher tview com os dados dos produtos
    preencher_tv(tview) #Chama a função

    #Posicionar o Tview na janela PADX = MARGEM DE FORA ,IPADX = DENTRO
    # tview.pack(padx=0, ipadx=130,ipady=240,pady=120, anchor="w")

    