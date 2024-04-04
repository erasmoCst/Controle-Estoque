from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, NUMERIC, SMALLINT, ForeignKey
from models.pessoa import Pessoa
from models.pedido import Pedido
from models.produto import Produto
from models.base import Base
from config.DBConnection import * 

class Produto_Pedido (Base):
    __tablename__ = 'PRODUTO_PEDIDO'
    cd_pedido: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pedido.cd_pedido),  nullable=False, primary_key=True)
    cd_produto: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Produto.cd_produto), nullable=False, primary_key=True)
    qt_produto: Mapped[float] = mapped_column(NUMERIC(7,2), nullable=False)

    @classmethod
    def busca_pedidio_cd_cliente(self, cd_cliente):
        results = session.query(
        Pedido.cd_pedido,
        Pessoa.nm_pessoa,
        Produto.nm_produto,
        Produto.vl_produto,
        Produto_Pedido.qt_produto,
        (Produto_Pedido.qt_produto * Produto.vl_produto),
        Pedido.dt_pedido,
        Pedido.dt_entregaprevista,
        Produto.tp_embalagemproduto
            ).\
            join(Produto_Pedido, Pedido.cd_pedido == Produto_Pedido.cd_pedido).\
            join(Produto, Produto_Pedido.cd_produto == Produto.cd_produto).\
            join(Pessoa, Pedido.cd_pessoa == Pessoa.cd_pessoa).\
            filter(Pedido.cd_pessoa == cd_cliente).all()

        return results
    
    @classmethod
    def persiste_produto_pedido(self, cd_pedido, cd_produto, qt_produto):
        try:
            produto_pedido = Produto_Pedido(cd_pedido=cd_pedido, 
                                            cd_produto=cd_produto, 
                                            qt_produto=qt_produto)
            session.add(produto_pedido)
            session.flush()
            
            return {'status': 1, 'data': produto_pedido, 'mensagem': "Produto adicionado ao Pedido!"}
        except Exception as e:
            session.rollback()
            return {'status': 0, 'data': e, 'mensagem': "Erro ao adicionar Produto ao Pedido!"}