from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, CHAR, DATE, ForeignKey, func
from models.pessoa import Pessoa
from models.base import Base
from datetime import datetime, timedelta
from config.DBConnection import * 

class Pedido (Base):
    __tablename__ = 'PEDIDO'
    cd_pedido: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True)
    cd_pessoa: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.cd_pessoa), nullable=False) 
    dt_pedido: Mapped[datetime] = mapped_column(DATE, nullable=False, server_default=func.sysdate())
    dt_entregaprevista: Mapped[datetime] = mapped_column(DATE, nullable=False)

    @classmethod
    def busca_pedidio_nm_cliente(self, nm_cliente):
        results = session.query(Pessoa.nm_pessoa).filter(Pessoa.nm_pessoa.ilike(f'%{nm_cliente}%')).all()
        return results
    
    @classmethod
    def busca_pedidos_cd_cliente(self, cd_cliente):
        results = session.query(Pedido).filter(Pedido.cd_pessoa == cd_cliente).all()
        return results
    
    
    @classmethod
    def persiste_pedido(self, cd_cliente, dt_entregaprevista):
        try:
            novoPedido = Pedido(cd_pessoa=cd_cliente, 
                                dt_entregaprevista=dt_entregaprevista)
            session.add(novoPedido)
            session.flush()
            return {'status': 1, 'data': novoPedido, 'mensagem': "Pedido cadastrado com sucesso!"}
        except Exception as e: 
            session.rollback()
            print(f"Erro inesperado:{str (e)}")
            return {'status': 0, 'data': "", 'mensagem': "Erro ao cadastrar Pedido!"}