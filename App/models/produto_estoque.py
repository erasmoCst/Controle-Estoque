from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DATE, NUMERIC, SMALLINT, VARCHAR, ForeignKey
from models.estoque import Estoque
from models.produto import Produto
from models.base import Base
from datetime import datetime
from config.DBConnection import * 

class Produto_Estoque (Base):
    __tablename__ = 'PRODUTO_ESTOQUE'
    cd_produto: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Produto.cd_produto), nullable=False, primary_key=True)
    cd_estoque: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Estoque.cd_estoque), nullable=False, primary_key=True) 
    nr_lote: Mapped[str] = mapped_column(VARCHAR(10), nullable=False)
    qt_produtoestoque : Mapped[float] = mapped_column(NUMERIC(7,2), nullable=False) 
    dt_validade: Mapped[datetime.date] = mapped_column(DATE, nullable=False)
    dt_produtoestoque: Mapped[datetime] = mapped_column(DATE, nullable=False, default=0)

    def consulta_produto_estoque(cd_produto):
        try:
            produto_estoque = session.query(Produto.cd_produto,
                                            Produto.nm_produto,
                                            Produto.ds_produto,
                                            Produto.tp_embalagemproduto,
                                            Produto.vl_produto,
                                            Produto_Estoque.qt_produtoestoque).\
                join(Produto, Produto.cd_produto == Produto_Estoque.cd_produto).\
                filter(Produto_Estoque.cd_produto == cd_produto).\
                first()
            
            return {'status': 1, 'data': produto_estoque, 'mensagem': "Produto consultado com sucesso"}
        except Exception as e: 
            return {'status': 0, 'data': e, 'mensagem': "Erro ao consultar o produto no estoque"}
    
    def busca_produto_estoque_ordenado_dt_validade(cd_produto):
        try:
            produto_estoque = session.query(Produto_Estoque).\
                filter(Produto_Estoque.cd_produto == cd_produto).\
                order_by(Produto_Estoque.dt_validade).\
                all()
            
            return {'status': 1, 'data': produto_estoque, 'mensagem': "Produto com sucesso"}
        except Exception as e: 
            return {'status': 0, 'data': e, 'mensagem': "Erro ao consultar o produto no estoque"}

    def remove_produto_estoque(cd_produto, cd_estoque, nr_lote, qt_produto):
        try:
            produto_estoque = session.query(Produto_Estoque).\
                filter(Produto_Estoque.cd_produto == cd_produto,
                       Produto_Estoque.cd_estoque == cd_estoque,
                       Produto_Estoque.nr_lote == nr_lote).\
                first()
            
            if produto_estoque.qt_produtoestoque >= qt_produto:
                produto_estoque.qt_produtoestoque -= qt_produto

                session.query(Produto_Estoque).\
                filter(Produto_Estoque.cd_produto == cd_produto, 
                       Produto_Estoque.cd_estoque == cd_estoque,
                       Produto_Estoque.nr_lote == nr_lote).\
                update({Produto_Estoque.qt_produtoestoque: produto_estoque.qt_produtoestoque})

                session.flush()

                return {'status': 1, 'data': None, 'mensagem': "Produto removido do estoque com sucesso"}
            else:
                return {'status': 0, 'data': None, 'mensagem': "Quantidade de produto indisponível no estoque"}
        except Exception as e: 
            return {'status': 0, 'data': e, 'mensagem': "Erro ao remover o produto do estoque"}
