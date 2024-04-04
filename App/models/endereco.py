from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, CHAR, SMALLINT, VARCHAR, ForeignKey
from models.municipio import Municipio
from models.base import Base
from config.DBConnection import * 

class Endereco (Base):
    __tablename__ = 'ENDERECO'
    cd_endereco: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True)
    nr_cep: Mapped[str] = mapped_column(CHAR(8), nullable=False)
    nm_logradouro: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    nr_endereco: Mapped[str] = mapped_column(VARCHAR(5), nullable=False)
    nm_bairro: Mapped[str] = mapped_column(VARCHAR(25), nullable=False)
    ds_complemento: Mapped[str] = mapped_column(VARCHAR(100))
    cd_municipio: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Municipio.cd_municipio), nullable=False)

    @classmethod
    def persiste_endereco(self, nr_cep, nm_logradouro, nr_endereco, nm_bairro, ds_complemento, cd_municipio):
        try:
            novoEndereco = Endereco(nr_cep=nr_cep, 
                                    nm_logradouro=nm_logradouro, 
                                    nr_endereco=nr_endereco, 
                                    nm_bairro=nm_bairro, 
                                    ds_complemento=ds_complemento, 
                                    cd_municipio=cd_municipio)
            session.add(novoEndereco)
            session.flush()

            return {'status': 1, 'data': novoEndereco, 'mensagem': "Endereço cadastrado com sucesso!"}
        except Exception as e: 
            session.rollback()
            return {'status': 0, 'data': e, 'mensagem': "Erro ao cadastrar endereço!"}

