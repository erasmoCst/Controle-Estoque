from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import INTEGER, NUMERIC, SMALLINT, VARCHAR, CHAR, DATE, NUMERIC, ForeignKey, func
from datetime import datetime
from config.DBConnection import * 

class Base(DeclarativeBase):
    @classmethod
    def add(cls):
        session.add(cls)
        session.flush()
 
class Municipio (Base):
    __tablename__ = 'MUNICIPIO'
    cd_municipio: Mapped[int] = mapped_column(SMALLINT, nullable=False, primary_key=True)
    nm_municipio: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    nm_estado: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    nm_pais: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)

class Estoque (Base):
    __tablename__ = 'ESTOQUE'
    cd_estoque: Mapped[int] = mapped_column(SMALLINT, nullable=False, primary_key=True) 
    nr_rua: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    nr_prateleira: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    nr_sequencia: Mapped[str] = mapped_column(CHAR(1), nullable=False) 

class Endereco (Base):
    __tablename__ = 'ENDERECO'
    cd_endereco: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True)
    nr_cep: Mapped[str] = mapped_column(CHAR(8), nullable=False)
    nm_logradouro: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    nr_endereco: Mapped[str] = mapped_column(VARCHAR(5), nullable=False)
    nm_bairro: Mapped[str] = mapped_column(VARCHAR(25), nullable=False)
    ds_complemento: Mapped[str] = mapped_column(VARCHAR(100))
    cd_municipio: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Municipio.cd_municipio), nullable=False)

    @classmethod
    def CadastraEndereco(self, nr_cep, nm_logradouro, nr_logradouro, cd_municipio):
        novoEndereco = Endereco(nr_cep=nr_cep, nm_logradouro=nm_logradouro, nr_logradouro=nr_logradouro, cd_municipio=cd_municipio)
        session.add(novoEndereco)
        session.flush()
        return novoEndereco

class Pessoa (Base):
    __tablename__ = 'PESSOA'
    cd_pessoa: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True)
    nm_pessoa: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    cd_endereco: Mapped[int] = mapped_column(INTEGER, ForeignKey(Endereco.cd_endereco), nullable=False) 
    nr_telefone: Mapped[str] = mapped_column(VARCHAR(15), nullable=False)
    nm_email: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    
    def CadastraPessoa():
        pass

class Cliente (Base):
    __tablename__ = 'CLIENTE'
    cd_cliente: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.cd_pessoa), nullable=False, primary_key=True)
    nr_cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True) 
    dt_nascimento: Mapped[datetime] = mapped_column(DATE, nullable=False)
    tp_genero: Mapped[str] = mapped_column(CHAR(1), nullable=False) 

class Fornecedor (Base):
    __tablename__ = 'FORNECEDOR'
    cd_fornecedor: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.cd_pessoa), nullable=False, primary_key=True)
    nr_cnpj: Mapped[str] = mapped_column(CHAR(14), nullable=False, unique=True)
    nm_razaosocial: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)

class Pedido (Base):
    __tablename__ = 'PEDIDO'
    cd_pedido: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True)
    cd_pessoa: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pessoa.cd_pessoa), nullable=False) 
    tp_pedido: Mapped[str] = mapped_column(CHAR(1), nullable=False)
    dt_pedido: Mapped[datetime] = mapped_column(DATE, nullable=False, server_default=func.sysdate())
    dt_entrega: Mapped[datetime] = mapped_column(DATE, nullable=False)

class Produto (Base):
    __tablename__ = 'PRODUTO'
    cd_produto: Mapped[int] = mapped_column(SMALLINT, nullable=False, primary_key=True)
    nm_produto: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    ds_produto: Mapped[str] = mapped_column(VARCHAR(500), nullable=False)
    tp_embalagemproduto: Mapped[str] = mapped_column(CHAR(1), nullable=False)

class Produto_estoque (Base):
    __tablename__ = 'PRODUTO_ESTOQUE'
    cd_produto: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Produto.cd_produto), nullable=False, primary_key=True)
    cd_estoque: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Estoque.cd_estoque), nullable=False, primary_key=True) 
    nr_lote: Mapped[str] = mapped_column(VARCHAR(10), nullable=False)
    qt_produtoestoque : Mapped[float] = mapped_column(NUMERIC(7,2), nullable=False) 
    dt_validade: Mapped[datetime] = mapped_column(DATE, nullable=False)
    dt_produtoestoque: Mapped[datetime] = mapped_column(DATE, nullable=False)

class Produto_fonecedor (Base):
    __tablename__ = 'PRODUTO_FONECEDOR'
    cd_produto: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Produto.cd_produto), nullable=False, primary_key=True)
    cd_fornecedor:  Mapped[int] = mapped_column(SMALLINT, ForeignKey(Fornecedor.cd_fornecedor), nullable=False, primary_key=True)
    vl_produto: Mapped[float] = mapped_column(NUMERIC(7,2), nullable=False)

class Produto_pedido (Base):
    __tablename__ = 'PRODUTO_PEDIDO'
    cd_pedido: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pedido.cd_pedido),  nullable=False, primary_key=True)
    cd_produto: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Produto.cd_produto), nullable=False, primary_key=True)
    qt_produto: Mapped[float] = mapped_column(NUMERIC(7,2), nullable=False)

class Transacao (Base):
    __tablename__ = 'TRANSACAO'
    cd_transacao: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True)
    cd_estoque: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Estoque.cd_estoque), nullable=False)
    cd_produto: Mapped[int] = mapped_column(SMALLINT, ForeignKey(Produto.cd_produto), nullable=False)
    cd_pedido: Mapped[int] = mapped_column(INTEGER, ForeignKey(Pedido.cd_pedido), nullable=False)
    tp_transacao: Mapped[str] = mapped_column(CHAR(1), nullable=False)
    qt_produto: Mapped[float] = mapped_column(NUMERIC(7,2), nullable=False)
    dt_transacao: Mapped[datetime] = mapped_column(DATE, nullable=False, server_default=func.sysdate()) 
