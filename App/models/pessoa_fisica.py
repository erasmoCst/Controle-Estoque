from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, CHAR, DATE, ForeignKey
from datetime import datetime
from models.endereco import Endereco
from models.municipio import Municipio
from models.base import Base
from models.pessoa import Pessoa
from config.DBConnection import * 

class Pessoa_Fisica (Base):
    __tablename__ = 'PESSOA_FISICA'
    cd_pessoa: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.cd_pessoa), nullable=False, primary_key=True)
    nr_cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True) 
    dt_nascimento: Mapped[datetime] = mapped_column(DATE, nullable=False)
    tp_genero: Mapped[str] = mapped_column(CHAR(1), nullable=False)

    @classmethod
    def verifica_CPF_existe(self, CPF):
        validaCPF = session.query(Pessoa_Fisica).filter_by(nr_cpf = CPF).one_or_none()

        if (validaCPF):
            return {'status': 0, 'data':"", 'mensagem': "O CPF já está cadastrado no sistema! Verifique os dados e tente novamente."}
        return {'status': 1, 'data':"", 'mensagem': "CPF válido para cadastro!"}
    
    @classmethod
    def busca_dados_cliente_CPF(self, CPF):
        dados_cliente = session.query(Pessoa.cd_pessoa,
                                      Pessoa.nm_pessoa, 
                                      Pessoa.nr_telefone, 
                                      Pessoa.nm_email,
                                      Pessoa_Fisica.nr_cpf,
                                      Pessoa_Fisica.dt_nascimento,
                                      Pessoa_Fisica.tp_genero,
                                      Endereco.nr_cep,
                                      Endereco.nm_logradouro,
                                      Endereco.nr_endereco,
                                      Endereco.nm_bairro,
                                      Endereco.ds_complemento,
                                      Municipio.nm_municipio,
                                      Municipio.nm_estado,
                                      Municipio.nm_pais).\
                        select_from(Pessoa_Fisica).\
                        join(Pessoa, Pessoa.cd_pessoa == Pessoa_Fisica.cd_pessoa).\
                        join(Endereco, Endereco.cd_endereco == Pessoa.cd_endereco).\
                        join(Municipio, Municipio.cd_municipio == Endereco.cd_municipio).\
                        filter(Pessoa_Fisica.nr_cpf == CPF).\
                        first()

        if dados_cliente:
            return {'status': 1, 'data': dados_cliente, 'mensagem': "Cliente encontrado!"}
        else:
            return {'status': 0, 'data': "", 'mensagem': "Cliente não encontrado!"}       