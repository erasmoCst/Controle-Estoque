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

    def lista_produtos():
        try:
            produtos = session.query(Produto).order_by(Produto.nm_produto).all()
            return {'status': 1, 'data': produtos, 'mensagem': "Produtos encontrados!"}
        except Exception as e: 
            return {'status': 0, 'data': e, 'mensagem': "Nenhum produto cadastrado!"}

    def busca_produto_por_nome(nm_produto):
        try:
            produto = session.query(Produto).filter(Produto.nm_produto == nm_produto).first()
            return {'status': 1, 'data': produto, 'mensagem': "Produto encontrado!"}
        except Exception as e: 
            return {'status': 0, 'data': e, 'mensagem': "Produto não cadastrado! Verifique o nome informado!"}

    def busca_todos_produtos_por_nome(nm_produto):
        try:
            produtos = session.query(Produto).filter(Produto.nm_produto.like(f"%{nm_produto}%")).all()
            return {'status': 1, 'data': produtos, 'mensagem': "Produtos encontrados!"}
        except Exception as e: 
            return {'status': 0, 'data': e, 'mensagem': "Nenhum produto com cadastrado! Verifique o nome informado!"}

    def busca_produto_por_codigo(cd_produto):
        try:
            produto = session.query(Produto).filter(Produto.cd_produto == cd_produto).first()
            return {'status': 1, 'data': produto, 'mensagem': "Produto encontrado!"}
        except Exception as e: 
            return {'status': 0, 'data': e, 'mensagem': "Produto não cadastrado! Verifique o código informado!"}

        
