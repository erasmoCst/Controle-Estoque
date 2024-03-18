from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import SMALLINT, VARCHAR
from models.base import Base
from config.DBConnection import * 

class Municipio (Base):
    __tablename__ = 'MUNICIPIO'
    cd_municipio: Mapped[int] = mapped_column(SMALLINT, nullable=False, primary_key=True)
    nm_municipio: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    nm_estado: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    nm_pais: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)

    @classmethod
    def get_cd_municipio(self, nome_municipio, nome_estado, nome_pais):
        try:
            municipio = session.query(Municipio).\
                filter_by(nm_municipio = nome_municipio, nm_estado = nome_estado, nm_pais = nome_pais).\
                one_or_none()
            return {'status': 1, 'data': municipio.cd_municipio, 'mensagem': "Município válido!"}
        except:
            return {'status': 0, 'data': "", 'mensagem': "Município, Estado ou País inválido! Verifique os dados e tente novamente."}

        