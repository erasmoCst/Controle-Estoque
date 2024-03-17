from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, ForeignKey
from models.endereco import Endereco
from models.base import Base
from config.DBConnection import * 


class Pessoa (Base):
    __tablename__ = 'PESSOA'
    cd_pessoa: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True)
    nm_pessoa: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    cd_endereco: Mapped[int] = mapped_column(INTEGER, ForeignKey(Endereco.cd_endereco), nullable=False) 
    nr_telefone: Mapped[str] = mapped_column(VARCHAR(15), nullable=False)
    nm_email: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    
    def CadastraPessoa():
        pass