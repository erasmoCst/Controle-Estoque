from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from controller.cadastro_pessoa import *
from config.DBConnection import *

#FUNCÕES DE "Cadastro de Cliente"

def cadastro_cliente_PF():
    # Função de cadastro de clientes
    cadastro_cliente = Toplevel()
    cadastro_cliente.title("Cadastro de Cliente Pessoa Física")
    cadastro_cliente.geometry("700x500")
    cadastro_cliente.configure(background="#dde")

    ## Dados Pessoais
    Label(cadastro_cliente, text=" -- Dados Pessoais --", background="#dde", anchor="w").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    
    # Nome do Cliente
    Label(cadastro_cliente, text="Nome do Cliente:", background="#dde", anchor="w").grid(row=2, column=0, sticky="w", padx=10)
    nm_cliente_entry = Entry(cadastro_cliente)
    nm_cliente_entry.grid(row=2, column=1, sticky="ew", columnspan=4)
    
    # Data Nascimento
    Label(cadastro_cliente, text="Data de Nascimento:", background="#dde", anchor="w").grid(row=3, column=0, sticky="w", padx=10, pady=10)
    dt_nascimento_entry = Entry(cadastro_cliente)
    dt_nascimento_entry.grid(row=3, column=1)
    
    # Número CPF
    Label(cadastro_cliente, text="CPF:", background="#dde", anchor="w").grid(row=3, column=2, sticky="w", padx=10, pady=10)
    nr_cpf_entry = Entry(cadastro_cliente)
    nr_cpf_entry.grid(row=3, column=3)

    # Gênero
    Label(cadastro_cliente, text="Gênero:", background="#dde", anchor="w").grid(row=4, column=0, sticky="w", padx=10)
    tp_genero_entry = StringVar(cadastro_cliente)
    tp_genero_entry.set("")
    tp_genero_options = ["","Masculino", "Feminino", "Outro"]
    tp_genero_dropdown = OptionMenu(cadastro_cliente, tp_genero_entry, *tp_genero_options)
    tp_genero_dropdown.grid(row=4, column=1, sticky="w")


    ## Dados do Contato
    Label(cadastro_cliente, text=" -- Dados de Contato --", background="#dde", anchor="w").grid(row=5, column=0,  sticky="w", padx=10, pady=10)
    
    # Número Telefone
    Label(cadastro_cliente, text="Telefone:", background="#dde").grid(row=6,column=0, padx=10, pady=5, sticky="w")
    nr_telefone_entry = Entry(cadastro_cliente)
    nr_telefone_entry.grid(row=6, column=1)

    # Email
    Label(cadastro_cliente, text="E-mail:", background="#dde").grid(row=6, column=2, padx=10, pady=5, sticky="w")
    nm_email_entry = Entry(cadastro_cliente)
    nm_email_entry.grid(row=6, column=3)


    ## Dados do Endereço do Cliente
    Label(cadastro_cliente, text=" -- Dados do Endereço --", background="#dde", anchor="w").grid(row=7, column=0, sticky="w", padx=10, pady=10)

    # Número CEP
    Label(cadastro_cliente, background="#dde", text="CEP:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
    nr_cep_entry = Entry(cadastro_cliente)
    nr_cep_entry.grid(row=8, column=1)

    # Nome Logradouro
    Label(cadastro_cliente, background="#dde", text="Logradouro:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
    nm_logradouro_entry = Entry(cadastro_cliente)
    nm_logradouro_entry.grid(row=9, column=1, sticky="ew", columnspan=4)

    # Número do Endereço
    Label(cadastro_cliente, background="#dde", text="Número:").grid(row=10, column=0, padx=10, pady=5, sticky="w")
    nr_endereco_entry = Entry(cadastro_cliente)
    nr_endereco_entry.grid(row=10, column=1)

    # Descrição Complmento
    Label(cadastro_cliente, background="#dde", text="Complemento:").grid(row=10, column=2, padx=10, pady=5, sticky="w")
    ds_complemento_entry = Entry(cadastro_cliente)
    ds_complemento_entry.grid(row=10, column=3)

    # Nome do Bairro
    Label(cadastro_cliente, background="#dde", text="Bairro:").grid(row=11, column=0, padx=10, pady=5, sticky="w")
    nm_bairro_entry = Entry(cadastro_cliente)
    nm_bairro_entry.grid(row=10+1, column=1)

    # Nome da Cidade
    Label(cadastro_cliente, background="#dde", text="Cidade:").grid(row=11, column=2, padx=10, pady=5, sticky="w")
    nm_cidade_entry = Entry(cadastro_cliente)
    nm_cidade_entry.grid(row=11, column=3)

    # Nome do Estado
    Label(cadastro_cliente, background="#dde", text="Estado:").grid(row=12, column=0, padx=11, pady=5, sticky="w")
    nm_estado_entry = Entry(cadastro_cliente)
    nm_estado_entry.grid(row=11+1, column=1)

    # Nome do País
    Label(cadastro_cliente, background="#dde", text="País:").grid(row=12, column=2, padx=10, pady=5, sticky="w")
    nm_pais_entry = Entry(cadastro_cliente)
    nm_pais_entry.grid(row=12, column=3)
    
    def submit_cadastro():
        response = Cadastro_Pessoa.cadastrar_PF(dados_PF = {'nr_cpf':nr_cpf_entry.get(),
                                                    'dt_nascimento':dt_nascimento_entry.get(),
                                                    'tp_genero':tp_genero_entry.get()},
                                dados_endereco = {'nr_cep': nr_cep_entry.get(),
                                                'nm_logradouro': nm_logradouro_entry.get(),
                                                'nr_endereco': nr_endereco_entry.get(),
                                                'ds_complemento': ds_complemento_entry.get(),
                                                'nm_bairro': nm_bairro_entry.get(),
                                                'nm_municipio': nm_cidade_entry.get(),
                                                'nm_estado': nm_estado_entry.get(),
                                                'nm_pais': nm_pais_entry.get()},
                                dados_pessoa = {'nm_cliente': nm_cliente_entry.get(),
                                                'nr_telefone': nr_telefone_entry.get(),
                                                'nm_email': nm_email_entry.get()})
        print(response)
        showinfo("Cliente", response['mensagem'])

    submit_button = Button(cadastro_cliente, text="Cadastrar Cliente",
                        command=submit_cadastro)
    submit_button.grid(row=14,column=1, columnspan=2, pady=20, sticky="ew")




def cadastro_cliente_PJ():
    # Função de cadastro de clientes
    cadastro_cliente = Toplevel()
    cadastro_cliente.title("Cadastro de Cliente Pessoa Jurídica")
    cadastro_cliente.geometry("700x500")
    cadastro_cliente.configure(background="#dde")

    ## Dados Pessoais
    Label(cadastro_cliente, text=" -- Dados da Empresa --", background="#dde", anchor="w").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    
    # Nome Fantasia
    Label(cadastro_cliente, text="Nome Fantasia:", background="#dde", anchor="w").grid(row=2, column=0, sticky="w", padx=10, pady=10)
    nm_fantasia_entry = Entry(cadastro_cliente)
    nm_fantasia_entry.grid(row=2, column=1)
    
    # Número CNPJ
    Label(cadastro_cliente, text="CNPJ:", background="#dde", anchor="w").grid(row=2, column=2, sticky="w", padx=10, pady=10)
    nr_cnpj_entry = Entry(cadastro_cliente)
    nr_cnpj_entry.grid(row=2, column=3)

    # Razão Social
    Label(cadastro_cliente, text="Razão Social:", background="#dde", anchor="w").grid(row=3, column=0, sticky="w", padx=10)
    nm_razao_social_entry = Entry(cadastro_cliente)
    nm_razao_social_entry.grid(row=3, column=1, sticky="ew", columnspan=4)
    

    ## Dados do Contato
    Label(cadastro_cliente, text=" -- Dados de Contato --", background="#dde", anchor="w").grid(row=5, column=0,  sticky="w", padx=10, pady=10)
    
    # Número Telefone
    Label(cadastro_cliente, text="Telefone:", background="#dde").grid(row=6,column=0, padx=10, pady=5, sticky="w")
    nr_telefone_entry = Entry(cadastro_cliente)
    nr_telefone_entry.grid(row=6, column=1)

    # Email
    Label(cadastro_cliente, text="E-mail:", background="#dde").grid(row=6, column=2, padx=10, pady=5, sticky="w")
    nm_email_entry = Entry(cadastro_cliente)
    nm_email_entry.grid(row=6, column=3)


    ## Dados do Endereço do Cliente
    Label(cadastro_cliente, text=" -- Dados do Endereço --", background="#dde", anchor="w").grid(row=7, column=0, sticky="w", padx=10, pady=10)

    # Número CEP
    Label(cadastro_cliente, background="#dde", text="CEP:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
    nr_cep_entry = Entry(cadastro_cliente)
    nr_cep_entry.grid(row=8, column=1)

    # Nome Logradouro
    Label(cadastro_cliente, background="#dde", text="Logradouro:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
    nm_logradouro_entry = Entry(cadastro_cliente)
    nm_logradouro_entry.grid(row=9, column=1, sticky="ew", columnspan=4)

    # Número do Endereço
    Label(cadastro_cliente, background="#dde", text="Número:").grid(row=10, column=0, padx=10, pady=5, sticky="w")
    nr_endereco_entry = Entry(cadastro_cliente)
    nr_endereco_entry.grid(row=10, column=1)

    # Descrição Complmento
    Label(cadastro_cliente, background="#dde", text="Complemento:").grid(row=10, column=2, padx=10, pady=5, sticky="w")
    ds_complemento_entry = Entry(cadastro_cliente)
    ds_complemento_entry.grid(row=10, column=3)

    # Nome do Bairro
    Label(cadastro_cliente, background="#dde", text="Bairro:").grid(row=11, column=0, padx=10, pady=5, sticky="w")
    nm_bairro_entry = Entry(cadastro_cliente)
    nm_bairro_entry.grid(row=10+1, column=1)

    # Nome da Cidade
    Label(cadastro_cliente, background="#dde", text="Cidade:").grid(row=11, column=2, padx=10, pady=5, sticky="w")
    nm_cidade_entry = Entry(cadastro_cliente)
    nm_cidade_entry.grid(row=11, column=3)

    # Nome do Estado
    Label(cadastro_cliente, background="#dde", text="Estado:").grid(row=12, column=0, padx=11, pady=5, sticky="w")
    nm_estado_entry = Entry(cadastro_cliente)
    nm_estado_entry.grid(row=11+1, column=1)

    # Nome do País
    Label(cadastro_cliente, background="#dde", text="País:").grid(row=12, column=2, padx=10, pady=5, sticky="w")
    nm_pais_entry = Entry(cadastro_cliente)
    nm_pais_entry.grid(row=12, column=3)
    
    def submit_cadastro():
        response = Cadastro_Pessoa.cadastrar_PJ(dados_PJ = {'nr_cnpj':nr_cnpj_entry.get(),
                                                            'nm_razao_social':nm_fantasia_entry.get()},
                                                dados_endereco = {'nr_cep': nr_cep_entry.get(),
                                                                  'nm_logradouro': nm_logradouro_entry.get(),
                                                                  'nr_endereco': nr_endereco_entry.get(),
                                                                  'ds_complemento': ds_complemento_entry.get(),
                                                                  'nm_bairro': nm_bairro_entry.get(),
                                                                  'nm_municipio': nm_cidade_entry.get(),
                                                                  'nm_estado': nm_estado_entry.get(),
                                                                  'nm_pais': nm_pais_entry.get()},
                                                dados_pessoa = {'nm_fantasia': nm_fantasia_entry.get(),
                                                                'nr_telefone': nr_telefone_entry.get(),
                                                                'nm_email': nm_email_entry.get()})
        print(response)
        showinfo("Cliente", response['mensagem'])

    submit_button = Button(cadastro_cliente, text="Cadastrar Cliente", command=submit_cadastro)
    submit_button.grid(row=14,column=1, columnspan=2, pady=20, sticky="ew")
