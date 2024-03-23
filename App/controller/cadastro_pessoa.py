
from models.base import Base
from models.pessoa_juridica import Pessoa_Juridica
from models.endereco import Endereco
from models.municipio import Municipio
from models.pessoa_fisica import Pessoa_Fisica
from models.pessoa import Pessoa

class Cadastro_Pessoa ():
    def cadastrar_PF(dados_PF, dados_endereco, dados_pessoa):
        valida_CPF = Pessoa_Fisica.verifica_CPF_existe(dados_PF['nr_cpf'])

        if(not valida_CPF['status']):
            Base.rollback()
            return valida_CPF
        else:
            municipio = Municipio.get_cd_municipio(dados_endereco['nm_municipio'], 
                                                    dados_endereco['nm_estado'], 
                                                    dados_endereco['nm_pais'])
            if(not municipio['status']):
                Base.rollback()
                return municipio
            else:
                try:
                    endereco = Endereco.persiste_endereco(dados_endereco['nr_cep'], 
                                                        dados_endereco['nm_logradouro'], 
                                                        dados_endereco['nr_endereco'],
                                                        dados_endereco['nm_bairro'], 
                                                        dados_endereco['ds_complemento'], 
                                                        municipio['data'])
                    if(not endereco['status']):
                        Base.rollback()
                        return endereco
                    else:
                        pessoa = Pessoa.persiste_pessoa(dados_pessoa['nm_cliente'], 
                                                        dados_pessoa['nr_telefone'], 
                                                        dados_pessoa['nm_email'],
                                                        endereco['data'].cd_endereco)
                        if(not pessoa['status']):
                            Base.rollback()
                            return pessoa
                        else:
                            return {'status': 1, 'mensagem': "Cliente PF cadastrado com sucesso!"}
                except  :
                    return {'status': 0, 'data': "", 'mensagem': "Erro ao cadastrar Cliente PF!"}
    
    def cadastrar_PJ(dados_PJ, dados_endereco, dados_pessoa):
        valida_CNPJ = Pessoa_Juridica.verifica_CNPJ_existe(dados_PJ['nr_cnpj'])
        valida_razao_social = Pessoa_Juridica.verifica_razao_social_existe(dados_PJ['nm_razao_social'])
        
        if(not valida_CNPJ['status']):
            Base.rollback()
            return valida_CNPJ
        elif(not valida_razao_social['status']):
            Base.rollback()
            return valida_razao_social
        else:
            municipio = Municipio.get_cd_municipio(dados_endereco['nm_municipio'], 
                                                    dados_endereco['nm_estado'], 
                                                    dados_endereco['nm_pais'])
            if(not municipio['status']):
                Base.rollback()
                return municipio
            
            else:
                try:
                    endereco = Endereco.persiste_endereco(dados_endereco['nr_cep'], 
                                                        dados_endereco['nm_logradouro'], 
                                                        dados_endereco['nr_endereco'],
                                                        dados_endereco['nm_bairro'], 
                                                        dados_endereco['ds_complemento'], 
                                                        municipio['data'])
                    if(not endereco['status']):
                        Base.rollback()
                        return endereco
                    else:
                        try:
                            pessoa = Pessoa.persiste_pessoa(dados_pessoa['nm_fantasia'], 
                                                            dados_pessoa['nr_telefone'], 
                                                            dados_pessoa['nm_email'],
                                                            endereco['data'].cd_endereco)
                            if(not pessoa['status']):
                                print("pessoa['status']",pessoa['status'])
                                return pessoa
                            else:
                                Base.commit()
                                return {'status': 1, 'mensagem': "Cliente PJ cadastrado com sucesso!"}
                        except:
                            Base.rollback()
                            return {'status': 0, 'data': "", 'mensagem': "Erro ao cadastrar Pessoa!"}
                except:
                    Base.rollback()
                    return {'status': 0, 'data': "", 'mensagem': "Erro ao cadastrar Endereço!"}