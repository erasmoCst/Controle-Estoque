from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, CHAR, DATE, ForeignKey, func
from models.pessoa import Pessoa
from models.base import Base
from datetime import datetime
from config.DBConnection import * 

class Pedido (Base):
    __tablename__ = 'PEDIDO'
    cd_pedido: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True)
    cd_pessoa: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.cd_pessoa), nullable=False) 
    tp_pedido: Mapped[str] = mapped_column(CHAR(1), nullable=False)
    dt_pedido: Mapped[datetime] = mapped_column(DATE, nullable=False, server_default=func.sysdate())
    dt_entrega: Mapped[datetime] = mapped_column(DATE, nullable=False)