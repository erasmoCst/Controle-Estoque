from tkinter import Button, Entry, Label, Toplevel, ttk, StringVar
from tkinter.messagebox import showinfo
from controller.consulta_pedido import Consulta_Pedido

def preencher_tv(tree, produtos_pedido=None):
    for i in tree.get_children():
        tree.delete(i)

    for item in produtos_pedido:
        tree.insert("","end", values=(
            item.cd_produto,
            item.nm_produto,
            "Ensacado" if item.tp_embalagemproduto == "E" else "A granel",
            item.qt_produto,
            item.dt_entregaprevista.strftime("%d/%m/%Y")
            ))

def detalhes_pedido(cd_pedido):
    detalhes_pedido = Toplevel()
    detalhes_pedido.title("Resumo Pedido")
    detalhes_pedido.geometry("720x550")
    detalhes_pedido.configure(background="#dde")
    
    dados_pedido = Consulta_Pedido.consulta_detalhes_pedido_por_codigo(cd_pedido)

    Label(detalhes_pedido, text=" --- Detalhes do Pedido ---", background='#dde', anchor="w").grid(row=0, column=0, pady=10)

    ## Pedido
    # Código Pedido
    cd_pedido_var = StringVar()
    cd_pedido_var.set(dados_pedido['data'][0].cd_pedido)
    Label(detalhes_pedido, text="Pedido", background='#dde', anchor="w").grid(row=1, column=0)
    cd_pedido_entry = Entry(detalhes_pedido, textvariable=cd_pedido_var, state="readonly")
    cd_pedido_entry.grid(row=2, column=0)

    # Data Pedido
    dt_pedido_var = StringVar()
    dt_pedido_var.set(dados_pedido['data'][0].dt_pedido.strftime("%d/%m/%Y"))
    Label(detalhes_pedido, text="Data Pedido", background='#dde', anchor="w").grid(row=1, column=1)
    dt_pedido_entry = Entry(detalhes_pedido, textvariable=dt_pedido_var, state="readonly")
    dt_pedido_entry.grid(row=2, column=1)

    ## Cliente
    # Código Cliente
    cd_cliente_var = StringVar()
    cd_cliente_var.set(dados_pedido['data'][0].cd_pessoa)
    Label(detalhes_pedido, text="Cód. Cliente", background='#dde', anchor="w").grid(row=1, column=2)
    cd_cliente_entry = Entry(detalhes_pedido, textvariable=cd_cliente_var, state="readonly")
    cd_cliente_entry.grid(row=2, column=2)
    
    # Nome Cliente
    nm_cliente_var = StringVar()
    nm_cliente_var.set(dados_pedido['data'][0].nm_pessoa)
    Label(detalhes_pedido, text="Nome", background='#dde', anchor="w").grid(row=1, column=3)
    nm_cliente_entry = Entry(detalhes_pedido, textvariable=nm_cliente_var, state="readonly")
    nm_cliente_entry.grid(row=2, column=3)

    ## Produtos
    Label(detalhes_pedido, text="Itens Pedido", background='#dde', anchor="w").grid(row=5, column=0)
    tview = ttk.Treeview(detalhes_pedido, columns=("cd_produto", "nm_produto", "tp_embalagem", "qt_produto", "dt_entregaprevista"), show='headings')
    tview.heading("cd_produto", text="Código")
    tview.heading("nm_produto", text="Nome")
    tview.heading("tp_embalagem", text="Embalagem")
    tview.heading("qt_produto", text="Qtd.")
    tview.heading("dt_entregaprevista", text="Data Entrega Prevista")

    tview.column("cd_produto", minwidth=0, width=50)
    tview.column("nm_produto", minwidth=0, width=150)
    tview.column("tp_embalagem", minwidth=0, width=100)
    tview.column("qt_produto", minwidth=0, width=50)
    tview.column("dt_entregaprevista", minwidth=0, width=100)

    tview.grid(row=6, column=0, columnspan=4, pady=10)

    preencher_tv(tview, dados_pedido['data'])

    def atender_pedido():
        Consulta_Pedido.baixa_estoque(cd_pedido, dados_pedido['data'])   
        showinfo("Atender Pedido", "Pedido atendido com sucesso!")
        detalhes_pedido.destroy()

    Button(detalhes_pedido, text="Atender Pedido", anchor="w", command=atender_pedido).grid(row=7, column=1, columnspan=2, pady=10)

    

    