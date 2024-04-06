from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from tkinter import messagebox
from controller.cadastro_pessoa import Cadastro_Pessoa
from controller.cadastro_pedido import Cadastro_Pedido
from view.atendimento.registrar_pedido.itens_pedido import itens_pedido
from controller.consulta_cliente import Consulta_Cliente
from config.DBConnection import *

def atualiza_pessoa_juridica():
    atualizaPJ = Toplevel()
    atualizaPJ.title("Atualização de Cliente Pessoa Jurídica")
    atualizaPJ.geometry("700x500")
    atualizaPJ.configure(background="#dde")
    
    Label(atualizaPJ, text="CNPJ do Cliente:", background="#dde", anchor="w").grid(row=0, column=0, padx=10, pady=10)
    cnpj_cliente_entry = Entry(atualizaPJ)
    cnpj_cliente_entry.grid(row=0, column=1)

    def consultar_cliente():
        cnpj = cnpj_cliente_entry.get()
        tamanho = len(cnpj)

        if cnpj == "":
            Label(atualizaPJ, text="Por favor, preencha o campo CNPJ do cliente.", background="#dde", foreground='#ff0000', anchor="w").grid(row=1, column=0, sticky="w")
        elif (tamanho > 14) or tamanho < 14 or not cnpj.isnumeric():
            Label(atualizaPJ, text="CNPJ inválido.", background="#dde", foreground='#ff0000', anchor="w").grid(row=1, column=0, sticky="w")
        else:
            if tamanho == 14:
                dados_cliente = Consulta_Cliente.consulta_PJ(cnpj)
                if not dados_cliente['status']:
                    messagebox.showerror("Erro", dados_cliente['mensagem'])
                else:
                    Label(atualizaPJ, text="-- Dados do Cliente --", background="#dde", anchor="w").grid(row=1, column=0, sticky="w", padx=10)

                    # Nome Fantasia
                    Label(atualizaPJ, text="Nome Fantasia:", background="#dde", anchor="w").grid(row=2, column=0, sticky="w", padx=10, pady=10)
                    nm_fantasia_entry = Entry(atualizaPJ)
                    nm_fantasia_entry.insert(0, dados_cliente['data'].nm_pessoa)
                    nm_fantasia_entry.grid(row=2, column=1)

                    # Razão Social
                    Label(atualizaPJ, text="Razão Social:", background="#dde", anchor="w").grid(row=3, column=0, sticky="w", padx=10)
                    nm_razao_social_entry = Entry(atualizaPJ)
                    nm_razao_social_entry.insert(0, dados_cliente['data'].nm_razaosocial)
                    nm_razao_social_entry.grid(row=3, column=1, sticky="ew", columnspan=4)

                    # Número Telefone
                    Label(atualizaPJ, text="Telefone:", background="#dde").grid(row=6,column=0, padx=10, pady=5, sticky="w")
                    nr_telefone_entry = Entry(atualizaPJ)
                    nr_telefone_entry.insert(0, dados_cliente['data'].nr_telefone)
                    nr_telefone_entry.grid(row=6, column=1)

                    # Email
                    Label(atualizaPJ, text="E-mail:", background="#dde").grid(row=6, column=2, padx=10, pady=5, sticky="w")
                    nm_email_entry = Entry(atualizaPJ)
                    nm_email_entry.insert(0, dados_cliente['data'].nm_email)
                    nm_email_entry.grid(row=6, column=3)

                    # Número CEP
                    Label(atualizaPJ, background="#dde", text="CEP:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
                    nr_cep_entry = Entry(atualizaPJ)
                    nr_cep_entry.insert(0, dados_cliente['data'].nr_cep)
                    nr_cep_entry.grid(row=8, column=1)

                    # Nome Logradouro
                    Label(atualizaPJ, background="#dde", text="Logradouro:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
                    nm_logradouro_entry = Entry(atualizaPJ)
                    nm_logradouro_entry.insert(0, dados_cliente['data'].nm_logradouro)
                    nm_logradouro_entry.grid(row=9, column=1, sticky="ew", columnspan=4)

                    # Número do Endereço
                    Label(atualizaPJ, background="#dde", text="Número:").grid(row=10, column=0, padx=10, pady=5, sticky="w")
                    nr_endereco_entry = Entry(atualizaPJ)
                    nr_endereco_entry.insert(0, dados_cliente['data'].nr_endereco)
                    nr_endereco_entry.grid(row=10, column=1)

                    # Descrição Complmento
                    Label(atualizaPJ, background="#dde", text="Complemento:").grid(row=10, column=2, padx=10, pady=5, sticky="w")
                    ds_complemento_entry = Entry(atualizaPJ)
                    if dados_cliente['data'].ds_complemento: ds_complemento_entry.insert(0, dados_cliente['data'].ds_complemento)
                    ds_complemento_entry.grid(row=10, column=3)

                    # Nome do Bairro
                    Label(atualizaPJ, background="#dde", text="Bairro:").grid(row=11, column=0, padx=10, pady=5, sticky="w")
                    nm_bairro_entry = Entry(atualizaPJ)
                    nm_bairro_entry.insert(0, dados_cliente['data'].nm_bairro)
                    nm_bairro_entry.grid(row=10+1, column=1)

                    # Nome da Cidade
                    Label(atualizaPJ, background="#dde", text="Cidade:").grid(row=11, column=2, padx=10, pady=5, sticky="w")
                    nm_cidade_entry = Entry(atualizaPJ)
                    nm_cidade_entry.insert(0, dados_cliente['data'].nm_municipio)
                    nm_cidade_entry.grid(row=11, column=3)

                    # Nome do Estado
                    Label(atualizaPJ, background="#dde", text="Estado:").grid(row=12, column=0, padx=11, pady=5, sticky="w")
                    nm_estado_entry = Entry(atualizaPJ)
                    nm_estado_entry.insert(0, dados_cliente['data'].nm_estado)
                    nm_estado_entry.grid(row=11+1, column=1)

                    # Nome do País
                    Label(atualizaPJ, background="#dde", text="País:").grid(row=12, column=2, padx=10, pady=5, sticky="w")
                    nm_pais_entry = Entry(atualizaPJ)
                    nm_pais_entry.insert(0, dados_cliente['data'].nm_pais)
                    nm_pais_entry.grid(row=12, column=3)

                    def atualiza_dados_cliente():
                        response = Cadastro_Pessoa.atualizar_PJ(
                            {
                                'cd_pessoa': dados_cliente['data'].cd_pessoa,
                                'nr_cnpj': dados_cliente['data'].nr_cnpj,
                                'nm_razao_social': nm_razao_social_entry.get()
                            },
                            {
                                'cd_endereco': dados_cliente['data'].cd_endereco,
                                'nm_logradouro': nm_logradouro_entry.get(),
                                'nr_endereco': nr_endereco_entry.get(),
                                'nm_bairro': nm_bairro_entry.get(),
                                'ds_complemento': ds_complemento_entry.get(),
                                'nr_cep': nr_cep_entry.get(),
                                'nm_municipio': nm_cidade_entry.get(),
                                'nm_estado': nm_estado_entry.get(),
                                'nm_pais': nm_pais_entry.get()
                            },
                            {
                                'cd_pessoa': dados_cliente['data'].cd_pessoa, 
                                'nm_fantasia': nm_fantasia_entry.get(),
                                'nr_telefone': nr_telefone_entry.get(), 
                                'nm_email': nm_email_entry.get()
                            }
                        )
                            
                        if not response['status']:
                            messagebox.showerror("Erro", response['mensagem'])  
                        else: 
                            messagebox.showinfo("Sucesso", response['mensagem'])
                            atualizaPJ.destroy()
                        
                    Button(atualizaPJ, text="Atualizar dados cliente", command=atualiza_dados_cliente).grid(row=14, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

    Button(atualizaPJ, text="Consultar Cliente", command=consultar_cliente).grid(row=0, column=2, padx=10, pady=10)
