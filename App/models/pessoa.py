from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, ForeignKey
from models.endereco import Endereco
from models.base import Base
from config.DBConnection import * 


class Pessoa (Base):
    __tablename__ = 'PESSOA'
    cd_pessoa: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True)
    nm_pessoa: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    cd_endereco: Mapped[int] = mapped_column(INTEGER, ForeignKey(Endereco.cd_endereco), nullable=False) 
    nr_telefone: Mapped[str] = mapped_column(VARCHAR(15), nullable=False)
    nm_email: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    
    @classmethod
    def persiste_pessoa(self, nm_cliente, nr_telefone, nm_email, cd_endereco):
        try:
            novaPessoa = Pessoa(nm_pessoa=nm_cliente, nr_telefone=nr_telefone, nm_email=nm_email, cd_endereco=cd_endereco)
            session.add(novaPessoa)
            session.flush()
            
            return {'status': 1, 'data': novaPessoa, 'mensagem': "Pessoa cadastrada com sucesso!"}
        except Exception as e:  
            session.rollback()
            return {'status': 0, 'data': e, 'mensagem': "Erro ao cadastrar pessoa!"}

    @classmethod
    def busca_clientes_nome(self, nm_cliente):
        results = session.query(Pessoa.nm_pessoa).filter(Pessoa.nm_pessoa.ilike(f'%{nm_cliente}%')).all()
        return results

    @classmethod
    def atualiza_pessoa(self, cd_pessoa, nm_cliente, nr_telefone, nm_email, cd_endereco):
        try:
            session.query(Pessoa).\
                    filter(Pessoa.cd_pessoa == cd_pessoa).\
                    update({Pessoa.nm_pessoa: nm_cliente, Pessoa.nr_telefone: nr_telefone, Pessoa.nm_email: nm_email, Pessoa.cd_endereco: cd_endereco})
            session.flush()
            
            return {'status': 1, 'data': cd_pessoa, 'mensagem': "Pessoa atualizada com sucesso!"}
        except Exception as e:
            session.rollback()
            return {'status': 0, 'data': e, 'mensagem': "Erro ao atualizar pessoa!"}        
