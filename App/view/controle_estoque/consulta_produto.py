from tkinter import messagebox, ttk
from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from config.DBConnection import *
from models.produto_estoque import Produto_Estoque, Estoque, Produto


    
def consultar_produto_estoque():
    global codigo_prod_entry

    janela_consulta_produto = Toplevel()
    janela_consulta_produto.title("Consultar Produto")
    janela_consulta_produto.geometry("900x400")
    janela_consulta_produto.configure(background="#dde")

    Label(janela_consulta_produto, text="Código do produto:", background="#dde", anchor="w").place(x=10, y=30, width=110, height=20)
    codigo_prod_entry = Entry(janela_consulta_produto)
    codigo_prod_entry.place(x=150, y=30, width=60, height=20)

    ## Treeview
    tview = ttk.Treeview(janela_consulta_produto, columns=("ID", "Nome", "Quantidade", "Rua", "Prateleira", "Sequência", "Embalagem", "Lote", "Valor unid", "Valor total"), show="headings")
    tview.heading("ID", text="ID")
    tview.heading("Nome", text="Nome")
    tview.heading("Quantidade", text="Quantidade")
    tview.heading("Rua", text="Rua")
    tview.heading("Prateleira", text="Prateleira")
    tview.heading("Sequência", text="Sequência")
    tview.heading("Embalagem", text="Embalagem")
    tview.heading("Lote", text="Lote")
    tview.heading("Valor unid", text="Valor unid")
    tview.heading("Valor total", text="Valor total")

    tview.column('ID', minwidth=0, width=5)
    tview.column('Nome', minwidth=0, width=200)
    tview.column('Quantidade', minwidth=0, width=35)
    tview.column('Rua', minwidth=0, width=10)
    tview.column('Prateleira', minwidth=0, width=20)
    tview.column('Sequência', minwidth=0, width=25)
    tview.column('Embalagem', minwidth=0, width=35)
    tview.column('Lote', minwidth=0, width=30)
    tview.column('Valor unid', minwidth=0, width=30)
    tview.column('Valor total', minwidth=0, width=30)

    # Ocultando a primeira coluna
    tview.column("#0", width=0, stretch=NO)

    tview.pack(padx=0, ipadx=190,ipady=240,pady=120, anchor='n')    

    def buscar_produto():
        cd_produto = codigo_prod_entry.get()

        for i in tview.get_children():
            tview.delete(i)
        
           # Realizar a consulta utilizando JOIN entre Produto, Produto_estoque e Estoque
        resultado = session.query(Produto, Produto_Estoque, Estoque).\
            join(Produto_Estoque, Produto.cd_produto == Produto_Estoque.cd_produto).\
            join(Estoque, Produto_Estoque.cd_estoque == Estoque.cd_estoque).\
            filter(Produto.cd_produto == cd_produto).first()

        if resultado:
            produto, produto_estoque, estoque = resultado
            # Calcular o valor total do estoque
            valor_total = produto.vl_produto * produto_estoque.qt_produtoestoque
            # Adicionar os dados ao Treeview
            tview.insert("", "end", values=(produto.cd_produto, produto.nm_produto, produto_estoque.qt_produtoestoque, estoque.nr_rua, estoque.nr_prateleira, estoque.nr_sequencia, produto.tp_embalagemproduto, produto_estoque.nr_lote, produto.vl_produto, valor_total))
        else:
            # Se o produto não for encontrado, exibir uma mensagem
            messagebox.showinfo("Aviso", "Produto não encontrado no estoque.")

        if resultado:
            produto, produto_estoque = resultado
            # Adicionar os dados ao Treeview
            tview.insert("", "end", values=(produto.cd_produto, produto.nm_produto, produto_estoque.qt_produtoestoque, produto_estoque.cd_estoque.nr_rua, produto_estoque.cd_estoque.nr_prateleira, produto_estoque.cd_estoque.nr_sequencia, produto.tp_embalagemproduto,produto_estoque.nr_lote, produto.vl_produto))
        else:
            # Se o produto não for encontrado, exibir uma mensagem
            messagebox.showinfo("Aviso", "Produto não encontrado no estoque.")

    def on_buscar_produto():
        cd_produto = codigo_prod_entry.get()
        if cd_produto:
            buscar_produto()
        else:
            messagebox.showinfo("Aviso", "Por favor, insira um código de produto válido.")

    btn_buscar = Button(janela_consulta_produto, text="Buscar Produto", command=on_buscar_produto)
    btn_buscar.place(x=300, y=30)

    janela_consulta_produto.mainloop()


