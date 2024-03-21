from sqlalchemy.orm import DeclarativeBase
from config.DBConnection import * 

class Base(DeclarativeBase):
    @classmethod
    def commit(self):
        session.commit()

    @classmethod
    def rollback(self):
        session.rollback()

    @classmethod
    def add(cls):
        session.add(cls)
        session.flush()
