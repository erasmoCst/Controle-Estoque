from tkinter import Button, Entry, Label, Toplevel, ttk
from view.atendimento.registrar_pedido.busca_produto import busca_produto
from controller.produto import consulta_produto_estoque


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


def itens_pedido(pedido):
    itens_pedido = Toplevel()
    itens_pedido.title("Itens do Pedido")
    itens_pedido.geometry("1000x500")
    itens_pedido.configure(background="#dde")

    Label(itens_pedido, text=f"Pedido: {pedido['dados_pedido'].cd_pedido}", background='#dde', anchor="w").grid(row=0, column=0, pady=10)
    Label(itens_pedido, text=f"Cód. Cliente: {pedido['dados_cliente'].cd_pessoa}", background='#dde', anchor="w").grid(row=0, column=1, pady=10)
    Label(itens_pedido, text=f"Nome: {pedido['dados_cliente'].nm_pessoa}", background='#dde', anchor="w").grid(row=0, column=2, pady=10)
    Label(itens_pedido, text=f"Data: {pedido['dados_pedido'].dt_pedido}", background='#dde', anchor="w").grid(row=0, column=3, pady=10)
    Label(itens_pedido, text="Código Produto:", background='#dde', anchor="w").grid(row=1, column=0, padx=10)
    cd_produto_entry = Entry(itens_pedido)
    cd_produto_entry.grid(row=1, column=1, padx=10)
    
    def consultar_produto(cd_produto):
        produto = consulta_produto_estoque(cd_produto)
        if produto['status'] == "0":
            Label(itens_pedido, text=produto['mensagem'], background="#dde", anchor="w").grid(row=2, column=0, padx=10, pady=10)
        else:
            cd_produto_entry.delete(0, 'end')
            cd_produto_entry.insert(0, produto['data'].cd_produto)
            Label(itens_pedido, text=produto['data'].nm_produto, background="#dde", anchor="w").grid(row=2, column=0, padx=10)
            Label(itens_pedido, text="Código Produto:", background='#dde', anchor="w").grid(row=1, column=0, padx=10)
            Label(itens_pedido, text=f"Qtd. Estoque: {produto['data'].qt_produtoestoque}", background="#dde", anchor="w").grid(row=2, column=1)
            Button(itens_pedido, text="Adicionar ao Pedido", command=None).grid(row=3, column=2)
            
            Label(itens_pedido, text="Quantidade:", background='#dde', anchor="w").grid(row=3, column=0, padx=10)
            qt_estoque_entry = Entry(itens_pedido)
            qt_estoque_entry.grid(row=3, column=1, padx=10)
    
   

    Button(itens_pedido, text="Consultar Produto", command=lambda:consultar_produto(cd_produto_entry.get())).grid(row=1, column=2)
    
    def pesquisa_produto():
        busca_produto(atualizar_produto_selecionado)

    def atualizar_produto_selecionado(cd_produto):
        consultar_produto(cd_produto)

    Button(itens_pedido, text="Buscar Produto", command=pesquisa_produto).grid(row=1, column=3)

    tview = ttk.Treeview(itens_pedido, columns=("Código", "Nome", "Descrição", "Embalagem"), show='headings')
    tview.heading("Código", text="Código")
    tview.heading("Nome", text="Nome")
    tview.heading("Descrição", text="Descrição")
    tview.heading("Embalagem", text="Embalagem")

    tview.column("Código", minwidth=0, width=5)
    tview.column("Nome", minwidth=0, width=200)
    tview.column("Descrição", minwidth=0, width=420)
    tview.column("Embalagem", minwidth=0, width=10)
    tview.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

    # Preencher tview com os dados dos produtos
    # preencher_tv(tview) #Chama a função para preencher o treeview
