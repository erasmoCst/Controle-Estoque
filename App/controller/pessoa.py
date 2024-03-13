from models.DBClasses import Pessoa, Endereco
from config.DBConnection import session


def CriaPessoa(endereco: Endereco, pessoa: Pessoa):
    try:
        endereco.add()
        
        return 1
    except:
        session.rollback()
        return 0
