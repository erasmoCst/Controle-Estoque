from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter.ttk import *


def preencher_tv(tree, pedidos=None):
    for i in tree.get_children():
        tree.delete(i)

    pedidos = lista_pedidos()

    for pedido in pedidos['data']:
        tree.insert("", "end", values=(
            pedido.cd_pedido,
            pedido.cd_pessoa,
            pedido.nm_peddoa,
            pedido.dt_pedido,
            pedido.dt_entregaprevista,
          ))
        
def atender_pedido():
    atender_pedido.title("Atender Pedido")
    atender_pedido.geometry("800x500")
    atender_pedido.configure(background="#dde")
    atender_pedido.mainloop()
    
    # Código Pedido
    Label(atender_pedido, text="Cód. Pedido:", background="#dde", anchor="w").grid(row=1, column=0, sticky="w", padx=10)
    cd_pedido_entry = Entry(atender_pedido)
    cd_pedido_entry.grid(row=0, column=0)

