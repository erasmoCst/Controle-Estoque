from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, NUMERIC, SMALLINT, ForeignKey
from models.pedido import Pedido
from models.produto import Produto
from models.base import Base
from config.DBConnection import * 

class Produto_pedido (Base):
    __tablename__ = 'PRODUTO_PEDIDO'
    cd_pedido: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pedido.cd_pedido),  nullable=False, primary_key=True)
    cd_produto: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Produto.cd_produto), nullable=False, primary_key=True)
    qt_produto: Mapped[float] = mapped_column(NUMERIC(7,2), nullable=False)
