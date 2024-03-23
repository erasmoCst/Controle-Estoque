
from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from models.endereco import Endereco
from models.pessoa import Pessoa
from models.produto import Produto
from config.DBConnection import *

#FUNCÕES DE "ATENDIMENTO"

def abrir_janela_agendamento():
    # Função para abrir a janela de agendamento de entrega
    janela_agendamento = Toplevel()
    janela_agendamento.title("Agendamento de Entrega")
    janela_agendamento.geometry("400x300")
    janela_agendamento.configure(background="#dde")

def abrir_janela_resumo(codigo_prod, quantidade_prod):
    # Função para abrir a janela de resumo do pedido
    janela_resumo = Toplevel()
    janela_resumo.title("Resumo do Pedido")
    janela_resumo.geometry("400x300")
    janela_resumo.configure(background="#dde")

    # Resumo:
    Label(janela_resumo, text="Código do produto: " + codigo_prod).pack()
    Label(janela_resumo, text="Quantidade: " + quantidade_prod).pack()

# Variáveis globais para os campos de entrada (Para serem acessadas em quaisquer aprte do codigo)
codigo_prod_entry = None
quantidade_prod_entry = None
id_cliente_entry = None
dia_entrega_entry = None
hora_entrega_entry = None

def registrar_pedido():
    global codigo_prod_entry, quantidade_prod_entry, id_cliente_entry
    
    # Nova janela para o registro de pedido
    janela_reg_pedido = Toplevel()
    janela_reg_pedido.title("Registro de Pedido")
    janela_reg_pedido.geometry("400x300")
    janela_reg_pedido.configure(background="#dde")
    
    Label(janela_reg_pedido, text="Código do produto:", background="#dde", anchor="w").place(x=10, y=30, width=110, height=20)
    codigo_prod_entry = Entry(janela_reg_pedido)
    codigo_prod_entry.place(x=150, y=30, width=110, height=20)
    
    Label(janela_reg_pedido, text="Quantidade:", background="#dde", anchor="w").place(x=10, y=60, width=110, height=20)
    quantidade_prod_entry = Entry(janela_reg_pedido)
    quantidade_prod_entry.place(x=150, y=60, width=110, height=20)
    
    # Campo para o ID do cliente
    Label(janela_reg_pedido, text="ID do Cliente:", background="#dde", anchor="w").place(x=10, y=90, width=110, height=20)
    id_cliente_entry = Entry(janela_reg_pedido)
    id_cliente_entry.place(x=150, y=90, width=110, height=20)
    
    # Botão para continuar com o pedido
    Button(janela_reg_pedido, text="Continuar com o pedido", command=agendamento_entrega).place(x=10, y=130, width=150, height=30)

def agendamento_entrega():
    codProduto = codigo_prod_entry.get()
    qtdProduto = quantidade_prod_entry.get()
    idCliente  = id_cliente_entry.get()

    # Implementar a função para abstrair as informações do resumo, nome do cliente, produto, valor, data e hora.
    cliente = session.query(Pessoa).filter_by(cd_pessoa = idCliente).one()
    produto = session.query(Produto).filter_by(cd_produto = codProduto).one()
    cidade = session.query(Endereco).filter_by(cd_endereco = cliente.cd_municipio).one()
    print(cliente, produto, qtdProduto)
    global dia_entrega_entry, hora_entrega_entry

    # Obter o código do produto, quantidade e ID do cliente inseridos pelo usuário
    codigo_prod = codigo_prod_entry.get()
    quantidade_prod = quantidade_prod_entry.get()
    id_cliente = id_cliente_entry.get()
    
    # Janela de agendamento de entrega
    janela_agendamento_entrega = Toplevel()
    janela_agendamento_entrega.title("Agendamento de Entrega")
    janela_agendamento_entrega.geometry("400x300")
    janela_agendamento_entrega.configure(background="#dde")
    
    Label(janela_agendamento_entrega, text=f"Cliente: {cidade.nm_logradouro}", background="#dde", anchor="w").place(x=10, y=20, width=110, height=20)
    
    # Campos para dia e hora de entrega
    Label(janela_agendamento_entrega, text="Dia de Entrega:", background="#dde", anchor="w").place(x=10, y=60, width=110, height=20)
    dia_entrega_entry = Entry(janela_agendamento_entrega)
    dia_entrega_entry.place(x=150, y=60, width=110, height=20)
    
    Label(janela_agendamento_entrega, text="Hora de Entrega:", background="#dde", anchor="w").place(x=10, y=90, width=110, height=20)
    hora_entrega_entry = Entry(janela_agendamento_entrega)
    hora_entrega_entry.place(x=150, y=90, width=110, height=20)
    
    # Botões para exibir o resumo do pedido e finalizar pedido
    Button(janela_agendamento_entrega, text="Mostrar Resumo do Pedido", command=resumo_pedido).place(x=10, y=180, width=150, height=30)
    Button(janela_agendamento_entrega, text="Finalizar Pedido", command=finalizar_pedido).place(x=180, y=180, width=150, height=30)

def resumo_pedido():
    # print(param1, param2)
    # Implementar a função para abstrair as informações do resumo, nome do cliente, produto, valor, data e hora.
    # municipios = session.query(Municipio).all()
    # for municipio in municipios:
    #     print(municipio.cd_municipio, municipio.nm_municipio, municipio.nm_estado, municipio.nm_pais)

    pass

def finalizar_pedido():
    # Criar um lógica para concluir o pedido no banco de dados
     
    pass
