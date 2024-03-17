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
    def get_cd_municipio(nome_municipio, nome_estado, nome_pais):
        try:
            session.query(Municipio).\
                filter(nm_municipio = nome_municipio, nm_estado = nome_estado, nm_pais = nome_pais).\
                one_or_none()
            return Municipio.cd_municipio
        except:
            return -1