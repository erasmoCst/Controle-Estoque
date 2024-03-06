from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import cx_Oracle
import os
from dotenv import load_dotenv

load_dotenv()

lib_dir = "C:\Oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)

api_key = os.getenv("API_KEY")


user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")
service_name = os.getenv("SERVICENAME")


servicename = cx_Oracle.makedsn(host, port, service_name=service_name)
instance = f"oracle+cx_oracle://{user}:{password}@{servicename}"
engine = create_engine(url=instance, echo=True, max_identifier_length=30)
session = scoped_session(sessionmaker(bind=engine, autoflush=True,autocommit=False))
try:
    session.execute(text("SELECT 1 FROM DUAL"))
    print("Conectado ao Banco de Dados com Sucesso!")
except SQLAlchemyError as e:
    print("Erro ao se conectar com o Banco de Dados:", e)
