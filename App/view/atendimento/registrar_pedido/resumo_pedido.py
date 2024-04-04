from tkinter import Button, Entry, Label, Toplevel, ttk, StringVar
from tkinter.messagebox import showinfo
from tkcalendar import DateEntry
from controller.cadastro_pedido import Pedido

def resumo_pedido(dados):
    resumo_pedido = Toplevel()
    resumo_pedido.title("Resumo Pedido")
    resumo_pedido.geometry("720x500")
    resumo_pedido.configure(background="#dde")

    Label(resumo_pedido, text=" --- Resumo do Pedido ---", background='#dde', anchor="w").grid(row=0, column=0, pady=10)

    ## Pedido
    # Código Pedido
    cd_pedido_var = StringVar()
    cd_pedido_var.set(dados['pedido']['dados_pedido'].cd_pedido)
    Label(resumo_pedido, text="Pedido", background='#dde', anchor="w").grid(row=1, column=0)
    cd_pedido_entry = Entry(resumo_pedido, textvariable=cd_pedido_var, state="readonly")
    cd_pedido_entry.grid(row=2, column=0)

    # Data Pedido
    dt_pedido_var = StringVar()
    dt_pedido_var.set(dados['pedido']['dados_pedido'].dt_pedido)
    Label(resumo_pedido, text="Data", background='#dde', anchor="w").grid(row=1, column=1)
    dt_pedido_entry = Entry(resumo_pedido, textvariable=dt_pedido_var, state="readonly")
    dt_pedido_entry.grid(row=2, column=1)

    ## Cliente
    # Código Cliente
    cd_cliente_var = StringVar()
    cd_cliente_var.set(dados['pedido']['dados_cliente'].cd_pessoa)
    Label(resumo_pedido, text="Cód. Cliente", background='#dde', anchor="w").grid(row=3, column=0)
    cd_cliente_entry = Entry(resumo_pedido, textvariable=cd_cliente_var, state="readonly")
    cd_cliente_entry.grid(row=4, column=0)
    
    # Nome Cliente
    nm_cliente_var = StringVar()
    nm_cliente_var.set(dados['pedido']['dados_cliente'].nm_pessoa)
    Label(resumo_pedido, text="Nome", background='#dde', anchor="w").grid(row=3, column=1)
    nm_cliente_entry = Entry(resumo_pedido, textvariable=nm_cliente_var, state="readonly")
    nm_cliente_entry.grid(row=4, column=1)

    # CPF Cliente
    cpf_cliente_var = StringVar()
    cpf_cliente_var.set(dados['pedido']['dados_cliente'].nr_cpf)
    Label(resumo_pedido, text="CPF", background='#dde', anchor="w").grid(row=3, column=2)
    cpf_cliente_entry = Entry(resumo_pedido, textvariable=cpf_cliente_var, state="readonly")
    cpf_cliente_entry.grid(row=4, column=2)
    
    ## Endereço
    # Logradouro
    nm_logradouro_var = StringVar()
    nm_logradouro_var.set(dados['pedido']['dados_cliente'].nm_logradouro)
    Label(resumo_pedido, text="Logradouro", background='#dde', anchor="w").grid(row=5, column=0)
    nm_logradouro_entry = Entry(resumo_pedido, textvariable=nm_logradouro_var, state="readonly")
    nm_logradouro_entry.grid(row=6, column=0)

    # Numero
    nr_endereco_var = StringVar()
    nr_endereco_var.set(dados['pedido']['dados_cliente'].nr_endereco)
    Label(resumo_pedido, text="Numero", background='#dde', anchor="w").grid(row=5, column=1)
    nr_endereco_entry = Entry(resumo_pedido, textvariable=nr_endereco_var, state="readonly")
    nr_endereco_entry.grid(row=6, column=1)
    
    # Bairro
    nm_bairro_var = StringVar()
    nm_bairro_var.set(dados['pedido']['dados_cliente'].nm_bairro)
    Label(resumo_pedido, text="Bairro", background='#dde', anchor="w").grid(row=5, column=2)
    nm_bairro_entry = Entry(resumo_pedido, textvariable=nm_bairro_var, state="readonly")
    nm_bairro_entry.grid(row=6, column=2)
    
    # Complemento
    ds_complemento_var = StringVar()
    ds_complemento_var.set(dados['pedido']['dados_cliente'].ds_complemento if dados['pedido']['dados_cliente'].ds_complemento else "")
    Label(resumo_pedido, text="Complemento", background='#dde', anchor="w").grid(row=5, column=3)
    ds_complemento_entry = Entry(resumo_pedido, textvariable=ds_complemento_var, state="readonly")
    ds_complemento_entry.grid(row=6, column=3)
    
    # Municipio
    nm_municipio_var = StringVar()
    nm_municipio_var.set(dados['pedido']['dados_cliente'].nm_municipio)
    Label(resumo_pedido, text="Cidade", background='#dde', anchor="w").grid(row=7, column=0)
    nm_municipio_entry = Entry(resumo_pedido, textvariable=nm_municipio_var, state="readonly")
    nm_municipio_entry.grid(row=8, column=0)
    
    # Estado
    nm_estado_var = StringVar()
    nm_estado_var.set(dados['pedido']['dados_cliente'].nm_estado)
    Label(resumo_pedido, text="Estado", background='#dde', anchor="w").grid(row=7, column=1)
    nm_estado_entry = Entry(resumo_pedido, textvariable=nm_estado_var, state="readonly")
    nm_estado_entry.grid(row=8, column=1)
    
    # País
    nm_pais_var = StringVar()
    nm_pais_var.set(dados['pedido']['dados_cliente'].nm_pais)
    Label(resumo_pedido, text="País", background='#dde', anchor="w").grid(row=7, column=2)
    nm_pais_entry = Entry(resumo_pedido, textvariable=nm_pais_var, state="readonly")
    nm_pais_entry.grid(row=8, column=2)
    
    ## Produtos
    tview = ttk.Treeview(resumo_pedido, columns=("cd", "nm", "emb", "qt", "vl_un", "vl_tt"), show='headings')
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

    tview.grid(row=9, column=0, columnspan=4, padx=10, pady=10)

    for item in dados['produtos']:
        tview.insert("", "end", values=(
            item['produto'].cd_produto,
            item['produto'].nm_produto,
            "Ensacado" if  item['produto'].tp_embalagemproduto == "E" else "A granel",
            item['qt_produto'],
            item['produto'].vl_produto,
            item['qt_produto']*item['produto'].vl_produto))
    
    Label(resumo_pedido, text="Data Entrega", background='#dde', anchor="w").grid(row=10, column=0)
    dt_entrega_entry = DateEntry(resumo_pedido, locale='pt_BR', date_pattern='dd/mm/yyyy', anchor="w")
    dt_entrega_entry.grid(row=10, column=1)

    Button(resumo_pedido, text="Finalizar Pedido", command=lambda: Pedido.finalizar_pedido(dados, dt_entrega_entry.get()), anchor="w").grid(row=10, column=3)

    showinfo("Pedido", "Pedido finalizado com sucesso!")