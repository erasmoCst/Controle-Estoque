
from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from tkinter import messagebox
from controller.consulta_cliente import Consulta_Cliente
from models.endereco import Endereco
from models.pessoa import Pessoa
from models.produto import Produto
from config.DBConnection import *

#FUNCÕES DE "ATENDIMENTO"

# def abrir_janela_agendamento():
#     # Função para abrir a janela de agendamento de entrega
#     janela_agendamento = Toplevel()
#     janela_agendamento.title("Agendamento de Entrega")
#     janela_agendamento.geometry("400x300")
#     janela_agendamento.configure(background="#dde")

# def abrir_janela_resumo(codigo_prod, quantidade_prod):
#     # Função para abrir a janela de resumo do pedido
#     janela_resumo = Toplevel()
#     janela_resumo.title("Resumo do Pedido")
#     janela_resumo.geometry("400x300")
#     janela_resumo.configure(background="#dde")

#     # Resumo:
#     Label(janela_resumo, text="Código do produto: " + codigo_prod).pack()
#     Label(janela_resumo, text="Quantidade: " + quantidade_prod).pack()

# # # Variáveis globais para os campos de entrada (Para serem acessadas em quaisquer aprte do codigo)
# codigo_prod_entry = None
# quantidade_prod_entry = None
# id_cliente_entry = None
# dia_entrega_entry = None
# hora_entrega_entry = None

def registrar_pedido():
    # Registro de pedido
    registra_pedido = Toplevel()
    registra_pedido.title("Registro de Pedido")
    registra_pedido.geometry("700x500")
    registra_pedido.configure(background="#dde")
    
    Label(registra_pedido, text="CPF/CNPJ do Cliente:", background="#dde", anchor="w").grid(row=0, column=0, padx=10, pady=10)
    cpf_cnpj_cliente_entry = Entry(registra_pedido)
    cpf_cnpj_cliente_entry.grid(row=0, column=1)

    def consultar_cliente():
        # Função para consultar o cliente
        cpf_cnpj = cpf_cnpj_cliente_entry.get()
        tamanho = len(cpf_cnpj)

        if cpf_cnpj == "":
            Label(registra_pedido, text="Por favor, preencha o campo CPF/CNPJ do cliente.", background="#dde", foreground='#ff0000', anchor="w").grid(row=1, column=0, sticky="w")
        elif (tamanho < 11 or tamanho > 14) or (tamanho > 11 and tamanho < 14) or not cpf_cnpj.isnumeric():
            Label(registra_pedido, text="CPF/CNPJ inválido.", background="#dde", foreground='#ff0000', anchor="w").grid(row=1, column=0, sticky="w")
        else:
            if tamanho == 11:
                response = Consulta_Cliente.consulta_PF(cpf_cnpj)
                print(response)
                if not response['status']:
                    messagebox.showerror("Erro", response['mensagem'])
                else:
                    Label(registra_pedido, text="-- Dados do Cliente --", background="#dde", anchor="w").grid(row=1, column=0, sticky="w", padx=10)

                    # Nome do Cliente
                    Label(registra_pedido, text="Nome do Cliente:", background="#dde", anchor="w").grid(row=2, column=0, sticky="w", padx=10)
                    nm_cliente_entry = Entry(registra_pedido)
                    nm_cliente_entry.insert(0, response['data'].nm_pessoa)
                    nm_cliente_entry.grid(row=2, column=1, sticky="ew", columnspan=4)
                    
                    # Data Nascimento
                    Label(registra_pedido, text="Data de Nascimento:", background="#dde", anchor="w").grid(row=3, column=0, sticky="w", padx=10, pady=10)
                    dt_nascimento_entry = Entry(registra_pedido)
                    dt_nascimento_entry.insert(0, response['data'].dt_nascimento.strftime("%d/%m/%Y"))
                    dt_nascimento_entry.grid(row=3, column=1)

                    # Gênero
                    Label(registra_pedido, text="Gênero:", background="#dde", anchor="w").grid(row=4, column=0, sticky="w", padx=10)
                    tp_genero_entry = StringVar(registra_pedido)
                    tp_genero_entry.set("")
                    tp_genero_options = ["","Masculino", "Feminino", "Outro"]
                    tp_genero_dropdown = OptionMenu(registra_pedido, tp_genero_entry, *tp_genero_options)
                    if response['data'].tp_genero == "M": tp_genero_entry.set("Masculino")
                    elif response['data'].tp_genero == "F": tp_genero_entry.set("Feminino")
                    elif response['data'].tp_genero == "O": tp_genero_entry.set("Outro")
                    tp_genero_dropdown.grid(row=4, column=1, sticky="w")

                    # Número Telefone
                    Label(registra_pedido, text="Telefone:", background="#dde").grid(row=6,column=0, padx=10, pady=5, sticky="w")
                    nr_telefone_entry = Entry(registra_pedido)
                    nr_telefone_entry.insert(0, response['data'].nr_telefone)
                    nr_telefone_entry.grid(row=6, column=1)

                    # Email
                    Label(registra_pedido, text="E-mail:", background="#dde").grid(row=6, column=2, padx=10, pady=5, sticky="w")
                    nm_email_entry = Entry(registra_pedido)
                    nm_email_entry.insert(0, response['data'].nm_email)
                    nm_email_entry.grid(row=6, column=3)

                    # Número CEP
                    Label(registra_pedido, background="#dde", text="CEP:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
                    nr_cep_entry = Entry(registra_pedido)
                    nr_cep_entry.insert(0, response['data'].nr_cep)
                    nr_cep_entry.grid(row=8, column=1)

                    # Nome Logradouro
                    Label(registra_pedido, background="#dde", text="Logradouro:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
                    nm_logradouro_entry = Entry(registra_pedido)
                    nm_logradouro_entry.insert(0, response['data'].nm_logradouro)
                    nm_logradouro_entry.grid(row=9, column=1, sticky="ew", columnspan=4)

                    # Número do Endereço
                    Label(registra_pedido, background="#dde", text="Número:").grid(row=10, column=0, padx=10, pady=5, sticky="w")
                    nr_endereco_entry = Entry(registra_pedido)
                    nr_endereco_entry.insert(0, response['data'].nr_endereco)
                    nr_endereco_entry.grid(row=10, column=1)

                    # Descrição Complmento
                    Label(registra_pedido, background="#dde", text="Complemento:").grid(row=10, column=2, padx=10, pady=5, sticky="w")
                    ds_complemento_entry = Entry(registra_pedido)
                    if response['data'].ds_complemento: ds_complemento_entry.insert(0, response['data'].ds_complemento)
                    ds_complemento_entry.grid(row=10, column=3)

                    # Nome do Bairro
                    Label(registra_pedido, background="#dde", text="Bairro:").grid(row=11, column=0, padx=10, pady=5, sticky="w")
                    nm_bairro_entry = Entry(registra_pedido)
                    nm_bairro_entry.insert(0, response['data'].nm_bairro)
                    nm_bairro_entry.grid(row=10+1, column=1)

                    # Nome da Cidade
                    Label(registra_pedido, background="#dde", text="Cidade:").grid(row=11, column=2, padx=10, pady=5, sticky="w")
                    nm_cidade_entry = Entry(registra_pedido)
                    nm_cidade_entry.insert(0, response['data'].nm_municipio)
                    nm_cidade_entry.grid(row=11, column=3)

                    # Nome do Estado
                    Label(registra_pedido, background="#dde", text="Estado:").grid(row=12, column=0, padx=11, pady=5, sticky="w")
                    nm_estado_entry = Entry(registra_pedido)
                    nm_estado_entry.insert(0, response['data'].nm_estado)
                    nm_estado_entry.grid(row=11+1, column=1)

                    # Nome do País
                    Label(registra_pedido, background="#dde", text="País:").grid(row=12, column=2, padx=10, pady=5, sticky="w")
                    nm_pais_entry = Entry(registra_pedido)
                    nm_pais_entry.insert(0, response['data'].nm_pais)
                    nm_pais_entry.grid(row=12, column=3)

                    Button(registra_pedido, text="Atualizar dados cliente", command=None).grid(row=14, column=0, padx=10, pady=10, sticky="ew")


                    Button(registra_pedido, text="Continuar Pedido", command=None).grid(row=14, column=2, columnspan=4, padx=10, pady=10)
            else:
                response = Consulta_Cliente.consulta_PJ(cpf_cnpj)
                print(response)
                if not response['status']:
                    messagebox.showerror("Erro", response['mensagem'])
                else:
                    Label(registra_pedido, text="-- Dados do Cliente --", background="#dde", anchor="w").grid(row=1, column=0, sticky="w", padx=10)

                    # Nome Fantasia
                    Label(registra_pedido, text="Nome Fantasia:", background="#dde", anchor="w").grid(row=2, column=0, sticky="w", padx=10, pady=10)
                    nm_fantasia_entry = Entry(registra_pedido)
                    nm_fantasia_entry.insert(0, response['data'].nm_pessoa)
                    nm_fantasia_entry.grid(row=2, column=1)

                    # Razão Social
                    Label(registra_pedido, text="Razão Social:", background="#dde", anchor="w").grid(row=3, column=0, sticky="w", padx=10)
                    nm_razao_social_entry = Entry(registra_pedido)
                    nm_razao_social_entry.insert(0, response['data'].nm_razaosocial)
                    nm_razao_social_entry.grid(row=3, column=1, sticky="ew", columnspan=4)

                    # Número Telefone
                    Label(registra_pedido, text="Telefone:", background="#dde").grid(row=6,column=0, padx=10, pady=5, sticky="w")
                    nr_telefone_entry = Entry(registra_pedido)
                    nr_telefone_entry.insert(0, response['data'].nr_telefone)
                    nr_telefone_entry.grid(row=6, column=1)

                    # Email
                    Label(registra_pedido, text="E-mail:", background="#dde").grid(row=6, column=2, padx=10, pady=5, sticky="w")
                    nm_email_entry = Entry(registra_pedido)
                    nm_email_entry.insert(0, response['data'].nm_email)
                    nm_email_entry.grid(row=6, column=3)

                    # Número CEP
                    Label(registra_pedido, background="#dde", text="CEP:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
                    nr_cep_entry = Entry(registra_pedido)
                    nr_cep_entry.insert(0, response['data'].nr_cep)
                    nr_cep_entry.grid(row=8, column=1)

                    # Nome Logradouro
                    Label(registra_pedido, background="#dde", text="Logradouro:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
                    nm_logradouro_entry = Entry(registra_pedido)
                    nm_logradouro_entry.insert(0, response['data'].nm_logradouro)
                    nm_logradouro_entry.grid(row=9, column=1, sticky="ew", columnspan=4)

                    # Número do Endereço
                    Label(registra_pedido, background="#dde", text="Número:").grid(row=10, column=0, padx=10, pady=5, sticky="w")
                    nr_endereco_entry = Entry(registra_pedido)
                    nr_endereco_entry.insert(0, response['data'].nr_endereco)
                    nr_endereco_entry.grid(row=10, column=1)

                    # Descrição Complmento
                    Label(registra_pedido, background="#dde", text="Complemento:").grid(row=10, column=2, padx=10, pady=5, sticky="w")
                    ds_complemento_entry = Entry(registra_pedido)
                    if response['data'].ds_complemento: ds_complemento_entry.insert(0, response['data'].ds_complemento)
                    ds_complemento_entry.grid(row=10, column=3)

                    # Nome do Bairro
                    Label(registra_pedido, background="#dde", text="Bairro:").grid(row=11, column=0, padx=10, pady=5, sticky="w")
                    nm_bairro_entry = Entry(registra_pedido)
                    nm_bairro_entry.insert(0, response['data'].nm_bairro)
                    nm_bairro_entry.grid(row=10+1, column=1)

                    # Nome da Cidade
                    Label(registra_pedido, background="#dde", text="Cidade:").grid(row=11, column=2, padx=10, pady=5, sticky="w")
                    nm_cidade_entry = Entry(registra_pedido)
                    nm_cidade_entry.insert(0, response['data'].nm_municipio)
                    nm_cidade_entry.grid(row=11, column=3)

                    # Nome do Estado
                    Label(registra_pedido, background="#dde", text="Estado:").grid(row=12, column=0, padx=11, pady=5, sticky="w")
                    nm_estado_entry = Entry(registra_pedido)
                    nm_estado_entry.insert(0, response['data'].nm_estado)
                    nm_estado_entry.grid(row=11+1, column=1)

                    # Nome do País
                    Label(registra_pedido, background="#dde", text="País:").grid(row=12, column=2, padx=10, pady=5, sticky="w")
                    nm_pais_entry = Entry(registra_pedido)
                    nm_pais_entry.insert(0, response['data'].nm_pais)
                    nm_pais_entry.grid(row=12, column=3)

                    Button(registra_pedido, text="Atualizar dados cliente", command=None).grid(row=14, column=0, padx=10, pady=10, sticky="ew")


                    Button(registra_pedido, text="Continuar Pedido", command=None).grid(row=14, column=2, columnspan=4, padx=10, pady=10)

    Button(registra_pedido, text="Consultar Cliente", command=consultar_cliente).grid(row=0, column=2, padx=10, pady=10)


    # 
    
    # Label(registra_pedido, text="", background="#dde").grid(row=1, column=1, columnspan=3, pady=10)

    # Label(registra_pedido, text="Selecione os Produtos:", background="#dde", anchor="w").grid(row=2, column=0, padx=10, pady=10)
    # nm_produto_entry = Entry(registra_pedido)
    # nm_produto_entry.grid(row=3, column=0, columnspan=4, sticky="ew" ,padx=10, pady=10)
    
    # Button(registra_pedido, text="Buscar Produto", command=None).grid(row=2, column=1, padx=10, pady=10)
