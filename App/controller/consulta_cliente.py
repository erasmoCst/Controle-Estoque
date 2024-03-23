from models.pessoa_fisica import Pessoa_Fisica
from models.pessoa_juridica import Pessoa_Juridica


class Consulta_Cliente ():
    def consulta_PF(cpf_cnpj):
        return (Pessoa_Fisica.busca_dados_cliente_CPF(cpf_cnpj))
        

    def consulta_PJ(cpf_cnpj):
        return (Pessoa_Juridica.busca_dados_cliente_CPF(cpf_cnpj))
