from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, CHAR, VARCHAR, ForeignKey
from models.pessoa import Pessoa
from models.base import Base
from config.DBConnection import * 

class Pessoa_Juridica (Base):
    __tablename__ = 'PESSOA_JURIDICA'
    cd_fornecedor: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.cd_pessoa), nullable=False, primary_key=True)
    nr_cnpj: Mapped[str] = mapped_column(CHAR(14), nullable=False, unique=True)
    nm_razaosocial: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)
