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
    dt_atendimento: Mapped[datetime] = mapped_column(DATE)

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
    
    @classmethod
    def busca_pedidos_nao_atendidos(self):
        try:
            results = session.query(Pedido).filter(Pedido.in_atendido == 'N').all()
            return {'status': 1, 'data': results, 'mensagem': "Pedidos encontrados!"}
        
        except Exception as e:
            return {'status': 0, 'data': e, 'mensagem': "Erro ao buscar Pedidos!"}
        
    @classmethod
    def busca_pedido_nao_atendido_por_codigo(self, cd_pedido):
        try:
            results = session.query(Pedido).filter(Pedido.cd_pedido == cd_pedido, Pedido.in_atendido == 'N').all()
            return {'status': 1, 'data': results, 'mensagem': "Pedido encontrado!"}
        
        except Exception as e:
            return {'status': 0, 'data': e, 'mensagem': "Erro ao buscar Pedido!"}
    
    @classmethod
    def busca_pedido_nao_atendido_por_codigo_cliente(self, cd_cliente):
        try:
            results = session.query(Pedido).filter(Pedido.cd_pessoa == cd_cliente, Pedido.in_atendido == 'N').all()
            return {'status': 1, 'data': results, 'mensagem': "PedidoS encontradoS!"}
        
        except Exception as e:
            return {'status': 0, 'data': e, 'mensagem': "Erro ao buscar Pedido!"}

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
