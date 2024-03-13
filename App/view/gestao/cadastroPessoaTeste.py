# from view.menuPrincipal import *

from models.DBClasses import Municipio, Cliente, Endereco, Pessoa
from config.DBConnection import session
from datetime import datetime

## Cadastro de Cliente
print(" --- DADOS PESSOAIS ---")
nome = input("Nome: ")
genero = input("Gênero: ")
CPF = input("CPF: ")
dataNascimento = datetime.strptime(input("Data Nascimento: "),"%d/%m/%Y")
telefone = input("Telefone: ")
email = input("Email: ")

print(nome)
print(genero)
print(CPF)
print(dataNascimento)
print(telefone)
print(email)

validaCPF = session.query(Cliente).filter_by(nr_cpf = CPF).one_or_none()

if (validaCPF):
    print(f"Cliente com CPF: {CPF} já cadastrado!")

else:
    print(" --- DADOS DO ENDEREÇO ---")
    cep = input("CEP: ")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    complemento = input("Complemento: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    pais = input("Pais: ")

    print(cep)
    print(logradouro)
    print(numero)
    print(cidade)
    print(estado)
    print(pais)
    
    municipio = session.query(Municipio).filter(Municipio.nm_municipio == cidade).one()
    print(municipio)
    print(municipio.cd_municipio)
    print(municipio.nm_municipio)

    if(municipio):
        endereco = Endereco.CadastraEndereco(cep, logradouro, numero, municipio.cd_municipio)
        # endereco = Endereco(nr_cep = cep, nm_logradouro = logradouro, nr_logradouro = numero, cd_municipio=municipio.cd_municipio)
        # session.add(endereco)
        # session.flush()
        pessoa = Pessoa(nm_pessoa = nome, cd_endereco = endereco.cd_endereco, nr_telefone = telefone, nm_email = email)
        
        try:
            session.add(pessoa)
            session.flush()
            cliente = Cliente(cd_cliente = pessoa.cd_pessoa, nr_cpf = CPF, dt_nascimento = dataNascimento, tp_genero = genero)
            session.commit()
        except:
            session.rollback()
    #except:
      #  print("Municipio não encontrado, Verifique o nome do município e tente novamente.")
        #return -1

    # pessoa = Pessoa(nm_pessoa = nome, dt_nascimento = dataNascimento, nr_telefone = telefone, nm_email = email)
    # Pessoa.add(pessoa)
# endereco1 = Endereco.add(endereco)
# app.config(menu=Barra_menu)
# app.mainloop()

