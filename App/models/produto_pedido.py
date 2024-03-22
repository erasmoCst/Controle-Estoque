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
        #SELECT A.CD_PEDIDO, D.NM_PESSOA, C.NM_PRODUTO, c.VL_PRODUTO, B.QT_PRODUTO, (B.QT_PRODUTO * C.VL_PRODUTO), A.DT_PEDIDO, A.DT_ENTREGA, C.TP_EMBALAGEMPRODUTO
        #FROM ctl_estoque.PEDIDO A 
        #LEFT JOIN ctl_estoque.PRODUTO_PEDIDO B ON A.CD_PEDIDO = B.CD_PEDIDO 
        #LEFT JOIN ctl_estoque.PRODUTO C ON B.CD_PRODUTO = C.CD_PRODUTO
        #LEFT JOIN ctl_estoque.PESSOA D ON A.CD_PESSOA = D.CD_PESSOA
        #WHERE A.CD_PESSOA = cd_cliente
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
        for result in results:
            print(result)
        return results