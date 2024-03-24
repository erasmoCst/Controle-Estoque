from tkinter import *
from tkinter import Toplevel
from tkinter import ttk
from models.estoque import Estoque
from models.produto import Produto
from models.produto_estoque import Produto_Estoque
from config.DBConnection import *

# Função para preencher o treeview 
def preencher_tv(tree):
    # for para limpar os dados do treeview, necessario em casos de buscas
    for i in tree.get_children():
        tree.delete(i)

    # Consultar os produtos do estoque do Banco de dados
    produtos_estoque = session.query(Produto_Estoque, Produto.nm_produto, Estoque.cd_estoque, Estoque.nr_rua, Estoque.nr_prateleira, Estoque.nr_sequencia).\
    join(Produto, Produto_Estoque.cd_produto == Produto.cd_produto).\
    join(Estoque, Produto_Estoque.cd_estoque == Estoque.cd_estoque).\
    order_by(Produto_Estoque.cd_produto).all()

    # Adicionando os dados ao TreeView
    for produto_estoque, nm_produto, cd_estoque, nr_rua, nr_prateleira, nr_sequencia in produtos_estoque:
        tree.insert("", "end", values=(nm_produto, cd_estoque, nr_rua, nr_prateleira, nr_sequencia, produto_estoque.nr_lote, produto_estoque.qt_produtoestoque, produto_estoque.dt_validade, produto_estoque.dt_produtoestoque))


# Funcao para abrir a janela de listas de produtos do estoque
def lista_produtos_estoque():
    # Funcção para  a janela de lista de produtos do estoque
    lista_produtos_estoque = Toplevel()
    lista_produtos_estoque.title("Produtos em estoque")
    lista_produtos_estoque.geometry("1000x450")
    lista_produtos_estoque.configure(background="#dde")


    # Criacao da TreeView para exibir os prodts
    tview = ttk.Treeview(lista_produtos_estoque, columns=("Produto","ID-Estoque", "Rua", "Prateleira", "Sequencia","Lote", "Quantidade","Vencimento", "Dt Registro"), show='headings')
    tview.heading("Produto", text="Produto")
    tview.heading("ID-Estoque", text="ID-Estoque")
    tview.heading("Rua", text="Rua")
    tview.heading("Prateleira", text="Prateleira")
    tview.heading("Sequencia", text="Sequencia")
    tview.heading("Lote", text="Lote")
    tview.heading("Quantidade", text="Quantidade")
    tview.heading("Vencimento", text="Vencimento")
    tview.heading("Dt Registro", text="Dt Registro")

    #Tam. colunas
    tview.column('Produto', minwidth=0, width=150)
    tview.column('ID-Estoque', minwidth=0, width=30)
    tview.column('Rua', minwidth=0, width=5)
    tview.column('Prateleira', minwidth=0, width=20)
    tview.column('Sequencia', minwidth=0, width=25)
    tview.column('Lote', minwidth=0, width=15)
    tview.column('Quantidade', minwidth=0, width=30)
    tview.column('Vencimento', minwidth=0, width=35)
    tview.column('Dt Registro', minwidth=0, width=35)

    # Ocultando a primeira coluna
    tview.column("#0", width=0, stretch=NO)
    tview.column("#2", width=0, stretch=NO)
    # Preencher tview com os dados dos produtos
    preencher_tv(tview) #Chama a função

    #Posicionar o Tview na janela PADX = MARGEM DE FORA ,IPADX = DENTRO
    tview.pack(padx=5, ipadx=180,ipady=240,pady=50, anchor='center')


   


    