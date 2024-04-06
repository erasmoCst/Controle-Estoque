from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from tkinter import messagebox
from controller.cadastro_pessoa import Cadastro_Pessoa
from controller.cadastro_pedido import Cadastro_Pedido
from view.atendimento.registrar_pedido.itens_pedido import itens_pedido
from controller.consulta_cliente import Consulta_Cliente
from config.DBConnection import *

def atualiza_pessoa_fisica():
    atualizaPF = Toplevel()
    atualizaPF.title("Atualização de Cliente Pessoa Física")
    atualizaPF.geometry("700x500")
    atualizaPF.configure(background="#dde")
    
    Label(atualizaPF, text="CPF do Cliente:", background="#dde", anchor="w").grid(row=0, column=0, padx=10, pady=10)
    cpf_cliente_entry = Entry(atualizaPF)
    cpf_cliente_entry.grid(row=0, column=1)

    def consultar_cliente():
        cpf = cpf_cliente_entry.get()
        tamanho = len(cpf)

        if cpf == "":
            Label(atualizaPF, text="Por favor, preencha o campo CPF do cliente.", background="#dde", foreground='#ff0000', anchor="w").grid(row=1, column=0, sticky="w")
        elif (tamanho < 11 or tamanho > 14) or (tamanho > 11 and tamanho < 14) or not cpf.isnumeric():
            Label(atualizaPF, text="CPF inválido.", background="#dde", foreground='#ff0000', anchor="w").grid(row=1, column=0, sticky="w")
        else:
            if tamanho == 11:
                dados_cliente = Consulta_Cliente.consulta_PF(cpf)

                if not dados_cliente['status']:
                    messagebox.showerror("Erro", dados_cliente['mensagem'])
                else:
                    Label(atualizaPF, text="-- Dados do Cliente --", background="#dde", anchor="w").grid(row=1, column=0, sticky="w", padx=10)

                    # Nome do Cliente
                    Label(atualizaPF, text="Nome do Cliente:", background="#dde", anchor="w").grid(row=2, column=0, sticky="w", padx=10)
                    nm_cliente_entry = Entry(atualizaPF)
                    nm_cliente_entry.insert(0, dados_cliente['data'].nm_pessoa)
                    nm_cliente_entry.grid(row=2, column=1, sticky="ew", columnspan=4)
                    
                    # Data Nascimento
                    Label(atualizaPF, text="Data de Nascimento:", background="#dde", anchor="w").grid(row=3, column=0, sticky="w", padx=10, pady=10)
                    dt_nascimento_entry = Entry(atualizaPF)
                    dt_nascimento_entry.insert(0, dados_cliente['data'].dt_nascimento.strftime("%d/%m/%Y"))
                    dt_nascimento_entry.grid(row=3, column=1)

                    # Gênero
                    Label(atualizaPF, text="Gênero:", background="#dde", anchor="w").grid(row=4, column=0, sticky="w", padx=10)
                    tp_genero_entry = StringVar(atualizaPF)
                    tp_genero_entry.set("")
                    tp_genero_options = ["","Masculino", "Feminino", "Outro"]
                    tp_genero_dropdown = OptionMenu(atualizaPF, tp_genero_entry, *tp_genero_options)
                    if dados_cliente['data'].tp_genero == "M": tp_genero_entry.set("Masculino")
                    elif dados_cliente['data'].tp_genero == "F": tp_genero_entry.set("Feminino")
                    elif dados_cliente['data'].tp_genero == "O": tp_genero_entry.set("Outro")
                    tp_genero_dropdown.grid(row=4, column=1, sticky="w")

                    # Número Telefone
                    Label(atualizaPF, text="Telefone:", background="#dde").grid(row=6,column=0, padx=10, pady=5, sticky="w")
                    nr_telefone_entry = Entry(atualizaPF)
                    nr_telefone_entry.insert(0, dados_cliente['data'].nr_telefone)
                    nr_telefone_entry.grid(row=6, column=1)

                    # Email
                    Label(atualizaPF, text="E-mail:", background="#dde").grid(row=6, column=2, padx=10, pady=5, sticky="w")
                    nm_email_entry = Entry(atualizaPF)
                    nm_email_entry.insert(0, dados_cliente['data'].nm_email)
                    nm_email_entry.grid(row=6, column=3)

                    # Número CEP
                    Label(atualizaPF, background="#dde", text="CEP:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
                    nr_cep_entry = Entry(atualizaPF)
                    nr_cep_entry.insert(0, dados_cliente['data'].nr_cep)
                    nr_cep_entry.grid(row=8, column=1)

                    # Nome Logradouro
                    Label(atualizaPF, background="#dde", text="Logradouro:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
                    nm_logradouro_entry = Entry(atualizaPF)
                    nm_logradouro_entry.insert(0, dados_cliente['data'].nm_logradouro)
                    nm_logradouro_entry.grid(row=9, column=1, sticky="ew", columnspan=4)

                    # Número do Endereço
                    Label(atualizaPF, background="#dde", text="Número:").grid(row=10, column=0, padx=10, pady=5, sticky="w")
                    nr_endereco_entry = Entry(atualizaPF)
                    nr_endereco_entry.insert(0, dados_cliente['data'].nr_endereco)
                    nr_endereco_entry.grid(row=10, column=1)

                    # Descrição Complmento
                    Label(atualizaPF, background="#dde", text="Complemento:").grid(row=10, column=2, padx=10, pady=5, sticky="w")
                    ds_complemento_entry = Entry(atualizaPF)
                    if dados_cliente['data'].ds_complemento: ds_complemento_entry.insert(0, dados_cliente['data'].ds_complemento)
                    ds_complemento_entry.grid(row=10, column=3)

                    # Nome do Bairro
                    Label(atualizaPF, background="#dde", text="Bairro:").grid(row=11, column=0, padx=10, pady=5, sticky="w")
                    nm_bairro_entry = Entry(atualizaPF)
                    nm_bairro_entry.insert(0, dados_cliente['data'].nm_bairro)
                    nm_bairro_entry.grid(row=10+1, column=1)

                    # Nome da Cidade
                    Label(atualizaPF, background="#dde", text="Cidade:").grid(row=11, column=2, padx=10, pady=5, sticky="w")
                    nm_cidade_entry = Entry(atualizaPF)
                    nm_cidade_entry.insert(0, dados_cliente['data'].nm_municipio)
                    nm_cidade_entry.grid(row=11, column=3)

                    # Nome do Estado
                    Label(atualizaPF, background="#dde", text="Estado:").grid(row=12, column=0, padx=11, pady=5, sticky="w")
                    nm_estado_entry = Entry(atualizaPF)
                    nm_estado_entry.insert(0, dados_cliente['data'].nm_estado)
                    nm_estado_entry.grid(row=12, column=1)

                    # Nome do País
                    Label(atualizaPF, background="#dde", text="País:").grid(row=12, column=2, padx=10, pady=5, sticky="w")
                    nm_pais_entry = Entry(atualizaPF)
                    nm_pais_entry.insert(0, dados_cliente['data'].nm_pais)
                    nm_pais_entry.grid(row=12, column=3)

                    def atualiza_dados_cliente():
                        response = Cadastro_Pessoa.atualizar_PF(
                            {
                                'cd_pessoa': dados_cliente['data'].cd_pessoa,
                                'nr_cpf': dados_cliente['data'].nr_cpf,
                                'dt_nascimento': dt_nascimento_entry.get(),
                                'tp_genero': tp_genero_entry.get()
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
                                'nm_cliente': nm_cliente_entry.get(), 
                                'nr_telefone': nr_telefone_entry.get(), 
                                'nm_email': nm_email_entry.get()
                            }
                        )
                            
                        if not response['status']:
                            messagebox.showerror("Erro", response['mensagem'])  
                        else: 
                            messagebox.showinfo("Sucesso", response['mensagem'])
                            atualizaPF.destroy()
                        
                    Button(atualizaPF, text="Atualizar dados cliente", command=atualiza_dados_cliente).grid(row=14, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

    Button(atualizaPF, text="Consultar Cliente", command=consultar_cliente).grid(row=0, column=2, padx=10, pady=10)
