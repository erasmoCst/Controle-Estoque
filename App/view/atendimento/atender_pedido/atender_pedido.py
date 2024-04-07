from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from view.atendimento.atender_pedido.detalhar_pedido import detalhes_pedido
from controller.consulta_pedido import Consulta_Pedido

def preencher_tv(tree, cd_pedido=None, cd_cliente=None):
    for i in tree.get_children():
        tree.delete(i)

    if not cd_pedido and not cd_cliente:
         pedidos = Consulta_Pedido.consulta_pedidos_nao_atendidos() 
    elif cd_cliente:
        pedidos = Consulta_Pedido.consulta_pedido_por_codigo_cliente(cd_cliente)
    else:
       pedidos = Consulta_Pedido.consulta_pedido_nao_atendido_por_codigo(cd_pedido)
    
    for pedido in pedidos['data']:
        tree.insert("", "end", values=(
            pedido.cd_pedido,
            pedido.cd_pessoa,
            pedido.in_atendido,
            pedido.dt_pedido.strftime("%d/%m/%Y"),
            pedido.dt_entregaprevista.strftime("%d/%m/%Y")
          ))
        
def atender_pedido():
    atender_pedido = Toplevel()
    atender_pedido.title("Atendimento de Pedidos")
    atender_pedido.geometry("1000x500")
    atender_pedido.configure(background="#dde")
    
    # Código Pedido
    Label(atender_pedido, text="Cód. Pedido:", background="#dde", anchor="w").grid(row=0, column=0, padx=10, pady=10)
    cd_pedido_entry = Entry(atender_pedido)
    cd_pedido_entry.grid(row=1, column=0, padx=10)

    Label(atender_pedido, text="Cód. Cliente:", background="#dde", anchor="w").grid(row=0, column=1, padx=10, pady=10)
    cd_cliente_entry = Entry(atender_pedido)
    cd_cliente_entry.grid(row=1, column=1, padx=10)

    Button(atender_pedido, text="Buscar Pedido", command=lambda:preencher_tv(tview, cd_pedido_entry.get())).grid(row=1, column=2, padx=10)

    tview = Treeview(atender_pedido, columns=("cd_pedido", "cd_cliente", "in_atendido", "dt_pedido", "dt_entregaprevista"), show="headings")
    tview.heading("cd_pedido", text="Cód. Pedido")
    tview.heading("cd_cliente", text="Cód. Cliente")
    tview.heading("in_atendido", text="Atendido")
    tview.heading("dt_pedido", text="Data Pedido")
    tview.heading("dt_entregaprevista", text="Data Entrega Prevista")

    tview.column("cd_pedido", minwidth=0, width=50)
    tview.column("cd_cliente", minwidth=0, width=50)
    tview.column("in_atendido", minwidth=0, width=50)
    tview.column("dt_pedido", minwidth=0, width=100)
    tview.column("dt_entregaprevista", minwidth=0, width=100)

    tview.grid(row=2, column=0, columnspan=4, pady=10)

    preencher_tv(tview)

    def seleciona_produto():
        item = tview.selection()[0]
        detalhes_pedido(tview.item(item, option='values')[0])
        
    Button(atender_pedido, text="Detalhar Pedido",anchor="w", command=seleciona_produto).grid(row=3, column=1, columnspan=2, padx=10)
