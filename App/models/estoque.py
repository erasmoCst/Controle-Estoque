from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import  CHAR, SMALLINT
from models.base import Base
from config.DBConnection import * 

class Estoque (Base):
    __tablename__ = 'ESTOQUE'
    cd_estoque: Mapped[int] = mapped_column(SMALLINT, nullable=False, primary_key=True) 
    nr_rua: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    nr_prateleira: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    nr_sequencia: Mapped[str] = mapped_column(CHAR(1), nullable=False) 
