from config.DBConnection import *  
from models.DBClasses import *
from tkinter import *
from sqlalchemy import select

app = Tk()
app.title("App Controle de Estoque")
app.geometry("500x300")

Barra_menu = Menu(app)
menu_atendimento = Menu(Barra_menu, tearoff=0)
menu_atendimento.add_command(label="Registrar Pedido",command= None)
menu_atendimento.add_command(label="Consultar Pedidos",command= None)
Barra_menu.add_cascade(label="Atendimento",menu=menu_atendimento)

menu_fechar = Menu(Barra_menu, tearoff=0)
menu_fechar.add_command(label="Fechar",command= app.quit)
Barra_menu.add_cascade(label="Sistema",menu=menu_fechar)

app.config(menu=Barra_menu)
app.mainloop()