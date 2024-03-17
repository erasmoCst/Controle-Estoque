from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import NUMERIC, SMALLINT, ForeignKey
from .models.fornecedor import Fornecedor
from .models.produto import Produto
from models.base import Base
from config.DBConnection import * 

class Produto_fonecedor (Base):
    __tablename__ = 'PRODUTO_FONECEDOR'
    cd_produto: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Produto.cd_produto), nullable=False, primary_key=True)
    cd_fornecedor:  Mapped[int] = mapped_column(SMALLINT, ForeignKey(Fornecedor.cd_fornecedor), nullable=False, primary_key=True)
    vl_produto: Mapped[float] = mapped_column(NUMERIC(7,2), nullable=False)
