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


def itens_pedido(dados_cliente):
    itens_pedido = Toplevel()
    itens_pedido.title("Itens do Pedido")
    itens_pedido.geometry("1000x500")
    itens_pedido.configure(background="#dde")

    Label(itens_pedido, text=f"Cód. Cliente: {dados_cliente.cd_pessoa}", background='#dde', anchor="w").grid(row=0, column=1, pady=10)
    Label(itens_pedido, text=f"Nome do Cliente: {dados_cliente.nm_pessoa}", background='#dde', anchor="w").grid(row=0, column=2, pady=10)

    def consultar_produto():
        produto = consulta_produto_estoque(cd_produto_entry.get())
        if produto['status'] == "0":
            Label(itens_pedido, text=produto['mensagem'], background="#dde", anchor="w").grid(row=2, column=0, padx=10, pady=10)
        else:
            Label(itens_pedido, text=f"Produto: {produto['data'].nm_produto}", background="#dde", anchor="w").grid(row=2, column=0, padx=10, pady=10)
            Label(itens_pedido, text=f"Qtd. Estoque: {produto['data'].qt_produtoestoque}", background="#dde", anchor="w").grid(row=2, column=2, pady=10)
            Button(itens_pedido, text="Adicionar ao Pedido", command=None).grid(row=2, column=3, pady=10)
            

    Label(itens_pedido, text="Código Produto:", background='#dde', anchor="w").grid(row=1, column=0, padx=10)
    cd_produto_entry = Entry(itens_pedido)
    cd_produto_entry.grid(row=1, column=1, padx=10)
    
    Button(itens_pedido, text="Consultar Produto", command=consultar_produto).grid(row=1, column=2)
    
    produto_selecionado = {'cd_produto': '', 'nm_produto': ''}

    def pesquisa_produto():
        busca_produto(atualizar_produto_selecionado)

    def atualizar_produto_selecionado(cd_produto, nm_produto):
        produto_selecionado['cd_produto'] = cd_produto
        produto_selecionado['nm_produto'] = nm_produto
        cd_produto_entry.insert(0, cd_produto)
        # nm_bairro_entry.insert(0, nm_produto)

        print(f"Código do Produto: {cd_produto}")
        print(f"Nome do Produto: {nm_produto}")

    Button(itens_pedido, text="Buscar Produto", command=pesquisa_produto).grid(row=1, column=3)
    # itens_pedido.grab_set()  # Torna a janela de itens_pedido a principal

    tview = ttk.Treeview(itens_pedido, columns=("Código","Nome", "Descrição", "Embalagem"), show='headings')
    tview.heading("Código", text="Código")
    tview.heading("Nome", text="Nome")
    tview.heading("Descrição", text="Descrição")
    tview.heading("Embalagem", text="Embalagem")
    #Tam. colunas
    tview.column("Código", minwidth=0, width=5)
    tview.column("Nome", minwidth=0, width=200)
    tview.column("Descrição", minwidth=0, width=420)
    tview.column("Embalagem", minwidth=0, width=10)
    tview.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    # Preencher tview com os dados dos produtos
    # preencher_tv(tview) #Chama a função para preencher o treeview





# ##




# from tkinter import Button, Entry, Label, Toplevel, ttk
# from view.atendimento.registrar_pedido.busca_produto import busca_produto

# def itens_pedido(dados_cliente):
#     itens_pedido = Toplevel()
#     itens_pedido.title("Itens do Pedido")
#     itens_pedido.geometry("1000x500")
#     itens_pedido.configure(background="#dde")

#     produto_selecionado = {'cd_produto': '', 'nm_produto': ''}

#     def pesquisa_produto():
#         busca_produto(produto_selecionado, atualizar_produto_selecionado)

#     def atualizar_produto_selecionado(cd_produto, nm_produto):
#         produto_selecionado['cd_produto'] = cd_produto
#         produto_selecionado['nm_produto'] = nm_produto
#         print(f"Código do Produto: {cd_produto}")
#         print(f"Nome do Produto: {nm_produto}")

#     Button(itens_pedido, text="Buscar Produto", command=pesquisa_produto).grid(row=1, column=3)
#     itens_pedido.grab_set()  # Torna a janela de itens_pedido a principal

# # Teste
# # itens_pedido(None)
