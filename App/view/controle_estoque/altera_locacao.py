from sqlite3 import IntegrityError
from tkinter import *
from tkinter import Toplevel
from tkinter import ttk
from tkinter.messagebox import showinfo
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
    produtos_estoque = session.query(Produto_Estoque, Produto.cd_produto, Produto.nm_produto, Estoque.cd_estoque, Estoque.nr_rua, Estoque.nr_prateleira, Estoque.nr_sequencia).\
    join(Produto, Produto_Estoque.cd_produto == Produto.cd_produto).\
    join(Estoque, Produto_Estoque.cd_estoque == Estoque.cd_estoque).\
    order_by(Produto_Estoque.cd_estoque).all()

    # Adicionando os dados ao TreeView
    for produto_estoque, cd_produto, nm_produto, cd_estoque, nr_rua, nr_prateleira, nr_sequencia in produtos_estoque:
        tree.insert("", "end", values=(cd_produto,nm_produto, cd_estoque, nr_rua, nr_prateleira, nr_sequencia))


# Funcao para abrir a janela de listas de produtos do estoque
def lista_prod_locacao():
    global codigo_prod_entry, codigo_estoque_entry
    
    # Função para mostra lista de produtos do estoque
    lista_prod_locacao = Toplevel()
    lista_prod_locacao.title("Alterar a locação de produtos")
    lista_prod_locacao.geometry("1000x450")
    lista_prod_locacao.configure(background="#dde")
    
    
    Label(lista_prod_locacao, text="Código do produto:", background="#dde", anchor="w").place(x=10, y=30, width=110, height=20)
    codigo_prod_entry = Entry(lista_prod_locacao)
    codigo_prod_entry.place(x=150, y=30, width=60, height=20)

    Label(lista_prod_locacao, text="NOVO ID-Estoque:", background="#dde", anchor="w").place(x=290, y=30, width=120, height=20)
    codigo_estoque_entry = Entry(lista_prod_locacao)
    codigo_estoque_entry.place(x=420, y=30, width=60, height=20)



    # Criacao da TreeView para exibir os prodts
    tview = ttk.Treeview(lista_prod_locacao, columns=("ID","Produto","ID-Estoque", "Rua", "Prateleira", "Sequencia"), show='headings')
    tview.heading("ID", text="ID")
    tview.heading("Produto", text="Produto")
    tview.heading("ID-Estoque", text="ID-Estoque")
    tview.heading("Rua", text="Rua")
    tview.heading("Prateleira", text="Prateleira")
    tview.heading("Sequencia", text="Sequencia")

    #Tam. colunas
    tview.column('ID', minwidth=0, width=5)
    tview.column('Produto', minwidth=0, width=150)
    tview.column('ID-Estoque', minwidth=0, width=30)
    tview.column('Rua', minwidth=0, width=5)
    tview.column('Prateleira', minwidth=0, width=20)
    tview.column('Sequencia', minwidth=0, width=25)


    # Ocultando a primeira coluna
    tview.column("#0", width=0, stretch=NO)
    # Preencher tview com os dados dos produtos
    preencher_tv(tview) #Chama a função

    #Posicionar o Tview na janela PADX = MARGEM DE FORA ,IPADX = DENTRO
    tview.pack(padx=0, ipadx=190,ipady=240,pady=120, anchor='n')  

    def alterar_locacao():
        cd_produto = codigo_prod_entry.get()
        cd_estoque = codigo_estoque_entry.get()

        # Recuperando o produto e o estoque
        produto = session.query(Produto).filter_by(cd_produto=cd_produto).first()
        estoque = session.query(Estoque).filter_by(cd_estoque=cd_estoque).first()

        if produto and estoque:
            # Verifica se já existe uma entrada na tabela Produto_Estoque
            entrada_produto_estoque = session.query(Produto_Estoque).filter_by(cd_produto=cd_produto).first()
            if entrada_produto_estoque:
                # Atualiza a entrada existente com o novo código de estoque
                entrada_produto_estoque.cd_estoque = cd_estoque
            else:
                # Cria uma nova entrada na tabela Produto_Estoque
                nova_entrada = Produto_Estoque(cd_produto=cd_produto, cd_estoque=cd_estoque)
                session.add(nova_entrada)

            try:
                session.commit()
                showinfo("Alteração de Locação", "Locação alterada com sucesso!")
            except IntegrityError:
                session.rollback()
                showinfo("Alteração de Locação", "Erro: Ocorreu uma violação de integridade. Verifique os dados inseridos.")
            except Exception as e:
                session.rollback()
                showinfo("Alteração de Locação", f"Erro inesperado:{str(e)}")
        else:
            showinfo("Alteração de Locação", "Produto ou estoque não encontrado.")

    Register = Button(lista_prod_locacao, text="Alterar locação", width=40, command=alterar_locacao)
    Register.place(x=150, y=60)

