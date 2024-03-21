
from models.pessoa_juridica import Pessoa_Juridica
from models.endereco import Endereco
from models.municipio import Municipio
from models.pessoa_fisica import Pessoa_Fisica
from models.pessoa import Pessoa

class Cadastro_Pessoa ():
    def cadastrar_PF(dados_PF, dados_endereco, dados_pessoa):
        valida_CPF = Pessoa_Fisica.verifica_CPF_existe(dados_PF['nr_cpf'])
        if(not valida_CPF['status']):
            return valida_CPF['mensagem']
        else:
            municipio = Municipio.get_cd_municipio(dados_endereco['nm_municipio'], 
                                                    dados_endereco['nm_estado'], 
                                                    dados_endereco['nm_pais'])
            if(not municipio['status']):
                print("municipio['status']", municipio['status'])
                return municipio['mensagem']
            else:
                try:
                    endereco = Endereco.persiste_endereco(dados_endereco['nr_cep'], 
                                                        dados_endereco['nm_logradouro'], 
                                                        dados_endereco['nr_endereco'],
                                                        dados_endereco['nm_bairro'], 
                                                        dados_endereco['ds_complemento'], 
                                                        municipio['data'])
                    if(not endereco['status']):
                        print("endereco['status']:", endereco['status'])
                        return endereco['mensagem']
                    else:
                        pessoa = Pessoa.persiste_pessoa(dados_pessoa['nm_cliente'], 
                                                        dados_pessoa['nr_telefone'], 
                                                        dados_pessoa['nm_email'],
                                                        endereco['data'].cd_endereco)
                        if(not pessoa['status']):
                            print("pessoa['status']",pessoa['status'])
                            return pessoa['mensagem']
                        else:
                            return {'status': 1, 'mensagem': "Cliente PF cadastrado com sucesso!"}
                except  :
                    return {'status': 0, 'data': "", 'mensagem': "Erro ao cadastrar Cliente PF!"}
    
    def cadastrar_PJ(dados_PJ, dados_endereco, dados_pessoa):
        valida_CNPJ = Pessoa_Juridica.verifica_CNPJ_existe(dados_PJ['nr_cnpj'])
        valida_razao_social = Pessoa_Juridica.verifica_razao_social_existe(dados_PJ['nm_razao_social'])
        
        if(not valida_CNPJ['status']):
            return valida_CNPJ['mensagem']
        elif(not valida_razao_social['status']):
            return valida_razao_social['mensagem']
        else:
            municipio = Municipio.get_cd_municipio(dados_endereco['nm_municipio'], 
                                                    dados_endereco['nm_estado'], 
                                                    dados_endereco['nm_pais'])
            if(not municipio['status']):
                print("municipio['status']", municipio['status'])
                return municipio['mensagem']
            
            else:
                try:
                    endereco = Endereco.persiste_endereco(dados_endereco['nr_cep'], 
                                                        dados_endereco['nm_logradouro'], 
                                                        dados_endereco['nr_endereco'],
                                                        dados_endereco['nm_bairro'], 
                                                        dados_endereco['ds_complemento'], 
                                                        municipio['data'])
                    if(not endereco['status']):
                        print("endereco['status']:", endereco['status'])
                        return endereco['mensagem']
                    else:
                        try:
                            pessoa = Pessoa.persiste_pessoa(dados_pessoa['nm_cliente'], 
                                                            dados_pessoa['nr_telefone'], 
                                                            dados_pessoa['nm_email'],
                                                            endereco['data'].cd_endereco)
                            if(not pessoa['status']):
                                print("pessoa['status']",pessoa['status'])
                                return pessoa['mensagem']
                            else:
                                return {'status': 1, 'mensagem': "Cliente PJ cadastrado com sucesso!"}
                        except:
                            return {'status': 0, 'data': "", 'mensagem': "Erro ao cadastrar Pessoa!"}
                except  :
                    return {'status': 0, 'data': "", 'mensagem': "Erro ao cadastrar Endereço!"}