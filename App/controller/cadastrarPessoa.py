from datetime import datetime
from config.DBConnection import session
from models.DBClasses import Municipio, Cliente, Endereco, Pessoa

def cadastrar_cliente(dados_cliente, dados_endereco, dados_pessoa):
    print(dados_cliente, dados_endereco, dados_pessoa)

    print(Cliente.verifica_CPF_existe(dados_cliente['nr_cpf']))
    #pass


# ## Cadastro de Cliente
# print(" --- DADOS PESSOAIS ---")
# nome = input("Nome: ")
# genero = input("Gênero: ")
# CPF = input("CPF: ")
# dataNascimento = datetime.strptime(input("Data Nascimento: "),"%d/%m/%Y")
# telefone = input("Telefone: ")
# email = input("Email: ")

# print(nome)
# print(genero)
# print(CPF)
# print(dataNascimento)
# print(telefone)
# print(email)

# validaCPF = session.query(Cliente).filter_by(nr_cpf = CPF).one_or_none()

# if (validaCPF):
#     print(f"Cliente com CPF: {CPF} já cadastrado!")

# else:
#     print(" --- DADOS DO ENDEREÇO ---")
#     cep = input("CEP: ")
#     logradouro = input("Logradouro: ")
#     numero = input("Número: ")
#     bairro = input("Bairro: ")
#     complemento = input("Complemento: ")
#     cidade = input("Cidade: ")
#     estado = input("Estado: ")
#     pais = input("Pais: ")

#     print(cep)
#     print(logradouro)
#     print(numero)
#     print(cidade)
#     print(estado)
#     print(pais)
    
#     municipio = session.query(Municipio).filter(Municipio.nm_municipio == cidade).one()
#     print(municipio)
#     print(municipio.cd_municipio)
#     print(municipio.nm_municipio)

#     if(municipio):
#         endereco = Endereco.CadastraEndereco(cep, logradouro, numero, municipio.cd_municipio)
#         # endereco = Endereco(nr_cep = cep, nm_logradouro = logradouro, nr_logradouro = numero, cd_municipio=municipio.cd_municipio)
#         # session.add(endereco)
#         # session.flush()
#         pessoa = Pessoa(nm_pessoa = nome, cd_endereco = endereco.cd_endereco, nr_telefone = telefone, nm_email = email)
        
#         try:
#             session.add(pessoa)
#             session.flush()
#             cliente = Cliente(cd_cliente = pessoa.cd_pessoa, nr_cpf = CPF, dt_nascimento = dataNascimento, tp_genero = genero)
#             session.commit()
#         except:
#             session.rollback()



def cadastrar_pessoa(endereco: Endereco, pessoa: Pessoa):
    try:
        endereco.add()
        
        return 1
    except:
        session.rollback()
        return 0
