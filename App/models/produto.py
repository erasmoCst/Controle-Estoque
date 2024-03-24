from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import NUMERIC, CHAR, SMALLINT, VARCHAR
from models.base import Base
from config.DBConnection import * 

class Produto (Base):
    __tablename__ = 'PRODUTO'
    cd_produto: Mapped[int] = mapped_column(SMALLINT, nullable=False, primary_key=True)
    nm_produto: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    ds_produto: Mapped[str] = mapped_column(VARCHAR(500), nullable=False)
    tp_embalagemproduto: Mapped[str] = mapped_column(CHAR(1), nullable=False)
    vl_produto: Mapped[float] = mapped_column(NUMERIC(7,2), nullable=False)

    def busca_produto_por_id(cd_produto):
        try:
            produto = session.query(Produto).filter(Produto.cd_produto == cd_produto).first()
            return {'status': 1, 'data': produto, 'mensagem': "Produto encontrado!"}
        except:
            return {'status': 0, 'data': "", 'mensagem': "Produto não cadastrado! Verifique o código informado!"}

        
