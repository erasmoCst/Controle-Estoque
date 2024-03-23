from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
from tkinter import Toplevel, Label, Entry, Button, Tk

def consultar_pedido():    
    janela_consulta = Toplevel()
    janela_consulta.title("Consulta de Pedidos")
    janela_consulta.geometry("400x300")
    janela_consulta.configure(background="#dde")
    # Função para resgatar pedidos feitos PRODUTO_PEDIDO