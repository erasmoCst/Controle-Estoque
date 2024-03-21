from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, CHAR, VARCHAR, ForeignKey
from models.pessoa import Pessoa
from models.base import Base
from config.DBConnection import * 

class Pessoa_Juridica (Base):
    __tablename__ = 'PESSOA_JURIDICA'
    cd_pessoa: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.cd_pessoa), nullable=False, primary_key=True)
    nr_cnpj: Mapped[str] = mapped_column(CHAR(14), nullable=False, unique=True)
    nm_razaosocial: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)

    @classmethod
    def verifica_CNPJ_existe(self, CNPJ):
        valida_CNPJ = session.query(Pessoa_Juridica).filter_by(nr_cnpj = CNPJ).one_or_none()
        
        if(valida_CNPJ):
            return {'status': 0, 'data':"", 'mensagem': "O CNPJ já está cadastrado no sistema! Verifique os dados e tente novamente."}
        return {'status': 1, 'data':"", 'mensagem': "CNPJ válido para cadastro!"}
    
    @classmethod
    def verifica_razao_social_existe(self, razao_social):
        valida_razao_social = session.query(Pessoa_Juridica).filter_by(nm_razaosocial = razao_social).one_or_none()
        
        if(valida_razao_social):
            return {'status': 0, 'data':"", 'mensagem': "A Razão Social já está cadastrada no sistema! Verifique os dados e tente novamente."}
        return {'status': 1, 'data':"", 'mensagem': "Razão Social válida para cadastro!"}
    