from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, CHAR, DATE, ForeignKey
from datetime import datetime
from models.base import Base
from models.pessoa import Pessoa
from config.DBConnection import * 

class Pessoa_Fisica (Base):
    __tablename__ = 'PESSOA_FISICA'
    cd_cliente: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.cd_pessoa), nullable=False, primary_key=True)
    nr_cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True) 
    dt_nascimento: Mapped[datetime] = mapped_column(DATE, nullable=False)
    tp_genero: Mapped[str] = mapped_column(CHAR(1), nullable=False)

    @classmethod
    def verifica_CPF_existe(self, CPF):
        validaCPF = session.query(Pessoa_Fisica).filter_by(nr_cpf = CPF).one_or_none()

        if (validaCPF):
            return {'status': 0, 'data':"", 'mensagem': "O CPF já está cadastrado no sistema! Verifique os dados e tente novamente."}
        return {'status': 1, 'data':"", 'mensagem': "CPF válido para cadastro!"}
    




