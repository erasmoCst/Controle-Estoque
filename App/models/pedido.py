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
    in_atendido: Mapped[str] = mapped_column(CHAR(1), nullable=False, server_default='N') 
    dt_pedido: Mapped[datetime] = mapped_column(DATE, nullable=False, server_default=func.sysdate())
    dt_entregaprevista: Mapped[datetime] = mapped_column(DATE, nullable=False)

    @classmethod
    def busca_todos_pedidos(self):
        try:
            results = session.query(Pedido).all()
            return {'status': 1, 'data': results, 'mensagem': "Pedidos encontrados!"}
        
        except Exception as e:
            return {'status': 0, 'data': e, 'mensagem': "Erro ao buscar Pedidos!"}

    @classmethod
    def busca_pedido_por_codigo(self, cd_pedido):
        try:
            results = session.query(Pedido).filter(Pedido.cd_pedido == cd_pedido).all()
            return {'status': 1, 'data': results, 'mensagem': "Pedido encontrado!"}
        
        except Exception as e:
            return {'status': 0, 'data': e, 'mensagem': "Erro ao buscar Pedido!"}
    
    @classmethod
    def busca_pedido_por_codigo_cliente(self, cd_cliente):
        try:
            results = session.query(Pedido).filter(Pedido.cd_pessoa == cd_cliente).all()
            return {'status': 1, 'data': results, 'mensagem': "Pedido encontrado!"}
        
        except Exception as e:
            return {'status': 0, 'data': e, 'mensagem': "Erro ao buscar Pedido!"}
        
    # @classmethod
    # def busca_pedidio_nm_cliente(self, nm_cliente):
    #     results = session.query(Pessoa.nm_pessoa).filter(Pessoa.nm_pessoa.ilike(f'%{nm_cliente}%')).all()
    #     return results
    
    # @classmethod
    # def busca_pedidos_cd_cliente(self, cd_cliente):
    #     results = session.query(Pedido).filter(Pedido.cd_pessoa == cd_cliente).all()
    #     return results
    
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
            return {'status': 0, 'data': e, 'mensagem': "Erro ao cadastrar Pedido!"}
        
    @classmethod
    def atualiza_data_entrega(self, cd_pedido, dt_entrega):
        try:
            session.query(Pedido).\
                    filter(Pedido.cd_pedido == cd_pedido).\
                    update({Pedido.dt_entregaprevista: dt_entrega})
            session.flush()
            
            return {'status': 1, 'data': cd_pedido, 'mensagem': "Data de entrega atualizada com sucesso!"}
        except Exception as e:
            session.rollback()
            return {'status': 0, 'data': e, 'mensagem': "Erro ao cadastrar Pedido!"}
        