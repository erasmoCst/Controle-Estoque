from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, CHAR, DATE, NUMERIC, SMALLINT, ForeignKey, func
from .models.estoque import Estoque
from .models.pedido import Pedido
from .models.produto import Produto
from models.base import Base
from datetime import datetime
from config.DBConnection import * 

class Transacao (Base):
    __tablename__ = 'TRANSACAO'
    cd_transacao: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True)
    cd_estoque: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Estoque.cd_estoque), nullable=False)
    cd_produto: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Produto.cd_produto), nullable=False)
    cd_pedido: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pedido.cd_pedido), nullable=False)
    tp_transacao: Mapped[str] = mapped_column(CHAR(1), nullable=False)
    qt_produto: Mapped[float] = mapped_column(NUMERIC(7,2), nullable=False)
    dt_transacao: Mapped[datetime] = mapped_column(DATE, nullable=False, server_default=func.sysdate()) 
