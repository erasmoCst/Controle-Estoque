from tkinter import Button, Entry, Label, Toplevel, ttk
from view.atendimento.registrar_pedido.resumo_pedido import resumo_pedido
from view.atendimento.registrar_pedido.busca_produto import busca_produto
from controller.produto import consulta_produto_estoque
from tkinter.messagebox import showerror
from decimal import Decimal

def preencher_tv(tree, produtos_pedido=None):
    for i in tree.get_children():
        tree.delete(i)

    for item in produtos_pedido:
        tree.insert("","end", values=(
            item['produto'].cd_produto,
            item['produto'].nm_produto,
            "Ensacado" if item['produto'].tp_embalagemproduto == "E" else "A granel",
            item['qt_produto'],
            item['produto'].vl_produto,
            item['qt_produto'] * item['produto'].vl_produto))
        
def remover_tv(tree, produtos_pedido, produto=None):
    for i in tree.get_children():
        tree.delete(i)

    if produto:
        produtos_pedido.remove(produto)

    preencher_tv(tree, produtos_pedido)

def itens_pedido(pedido):
    itens_pedido = Toplevel()
    itens_pedido.title("Itens do Pedido")
    itens_pedido.geometry("720x500")
    itens_pedido.configure(background="#dde")
    (pedido['dados_pedido'])
    produtos_pedido = []

    Label(itens_pedido, text=f"Pedido: {pedido['dados_pedido'].cd_pedido}", background='#dde', anchor="w").grid(row=0, column=0, pady=10)
    Label(itens_pedido, text=f"Cód. Cliente: {pedido['dados_cliente'].cd_pessoa}", background='#dde', anchor="w").grid(row=0, column=1, pady=10)
    Label(itens_pedido, text=f"Nome: {pedido['dados_cliente'].nm_pessoa}", background='#dde', anchor="w").grid(row=0, column=2, pady=10)
    Label(itens_pedido, text=f"Data: {pedido['dados_pedido'].dt_pedido}", background='#dde', anchor="w").grid(row=0, column=3, pady=10)
    Label(itens_pedido, text="Código Produto:", background='#dde', anchor="w").grid(row=1, column=0, padx=10)
    cd_produto_entry = Entry(itens_pedido)
    cd_produto_entry.grid(row=1, column=1, padx=10)
    
    def adicionar_produto_pedido(produto, qt_produto):
        if produto.qt_produtoestoque < qt_produto:
            showerror("Erro", "Quantidade solicitada maior que a quantidade em estoque!")
        else: 
            produtos_pedido.append({'produto': produto, 'qt_produto': qt_produto})
            preencher_tv(tview, produtos_pedido) 

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
            Label(itens_pedido, text="Quantidade:", background='#dde', anchor="w").grid(row=3, column=0, padx=10)
            qt_produto_pedido_entry = Entry(itens_pedido)
            qt_produto_pedido_entry.grid(row=3, column=1, padx=10)
            Button(itens_pedido, 
                   text="Adicionar ao Pedido", 
                   command=lambda:adicionar_produto_pedido(produto['data'], Decimal(qt_produto_pedido_entry.get()))).\
                   grid(row=3, column=2)
    
    Button(itens_pedido, text="Consultar Produto", command=lambda:consultar_produto(cd_produto_entry.get())).grid(row=1, column=2)
    
    def pesquisa_produto():
        busca_produto(atualizar_produto_selecionado)

    def atualizar_produto_selecionado(cd_produto):
        consultar_produto(cd_produto)

    def remover_produto():
        item = tview.selection()[0]
        remover_tv(tview, produtos_pedido, produtos_pedido[tview.index(item)])
        # produtos_pedido.\
        #     remove({'produto': 
        #             {'cd_produto': tview.item(item, option='values')[0]}, 
        #             'qt_produto': tview.item(item, option='values')[3]})
        # tview.delete(item)

    Button(itens_pedido, text="Buscar Produto", command=pesquisa_produto).grid(row=1, column=3)
    Button(itens_pedido, text="Remover Produto", command=remover_produto).grid(row=5, column=0, pady=10)
    Button(itens_pedido, text="Finalizar Pedido", command=lambda: resumo_pedido({'pedido': pedido, 'produtos': produtos_pedido}), anchor="w").grid(row=5, column=1, columnspan=2, padx=10, pady=10)

    tview = ttk.Treeview(itens_pedido, columns=("cd", "nm", "emb", "qt", "vl_un", "vl_tt"), show='headings')
    tview.heading("cd", text="Código")
    tview.heading("nm", text="Nome")
    tview.heading("emb", text="Embalagem")
    tview.heading("qt", text="Qtd.")
    tview.heading("vl_un", text="Vlr. Unit")
    tview.heading("vl_tt", text="Vlr. Total")

    tview.column("cd", minwidth=0, width=50)
    tview.column("nm", minwidth=0, width=150)
    tview.column("emb", minwidth=0, width=100)
    tview.column("qt", minwidth=0, width=50)
    tview.column("vl_un", minwidth=0, width=100)
    tview.column("vl_tt",  minwidth=0, width=100)

    tview.grid(row=4, column=0, columnspan=4, padx=10, pady=10)
