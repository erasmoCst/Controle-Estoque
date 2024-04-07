from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from controller.consulta_pedido import Consulta_Pedido

def preencher_tv(tree, cd_pedido=None):
    for i in tree.get_children():
        tree.delete(i)

    pedidos = Consulta_Pedido.lista_todos_pedidos() if not cd_pedido else Consulta_Pedido.consulta_pedido_por_codigo(cd_pedido)

    for pedido in pedidos['data']:
        tree.insert("", "end", values=(
            pedido.cd_pedido,
            pedido.cd_pessoa,
            pedido.in_atendido,
            pedido.dt_pedido.strftime("%d/%m/%Y"),
            pedido.dt_entregaprevista.strftime("%d/%m/%Y")
          ))
        
def lista_pedidos():
    lista_pedidos = Toplevel()
    lista_pedidos.title("Lista de Pedidos")
    lista_pedidos.geometry("1000x500")
    lista_pedidos.configure(background="#dde")
    
    # Código Pedido
    Label(lista_pedidos, text="Cód. Pedido:", background="#dde", anchor="w").grid(row=0, column=0, padx=10, pady=10)
    cd_pedido_entry = Entry(lista_pedidos)
    cd_pedido_entry.grid(row=0, column=1, padx=10)

    Button(lista_pedidos, text="Buscar Pedido", command=lambda:preencher_tv(tview, cd_pedido_entry.get())).grid(row=0, column=2, padx=10)

    tview = Treeview(lista_pedidos, columns=("cd_pedido", "cd_cliente", "in_atendido", "dt_pedido", "dt_entregaprevista"), show="headings")
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