from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DATE, NUMERIC, SMALLINT, VARCHAR, ForeignKey
from models.estoque import Estoque
from models.produto import Produto
from models.base import Base
from datetime import datetime
from config.DBConnection import * 

class Produto_estoque (Base):
    __tablename__ = 'PRODUTO_ESTOQUE'
    cd_produto: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Produto.cd_produto), nullable=False, primary_key=True)
    cd_estoque: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Estoque.cd_estoque), nullable=False, primary_key=True) 
    nr_lote: Mapped[str] = mapped_column(VARCHAR(10), nullable=False)
    qt_produtoestoque : Mapped[float] = mapped_column(NUMERIC(7,2), nullable=False) 
    dt_validade: Mapped[datetime.date] = mapped_column(DATE, nullable=False)
    dt_produtoestoque: Mapped[datetime] = mapped_column(DATE, nullable=False)