from datetime import date, timedelta, datetime
from models.pedido import Pedido


def criar_pedido(cd_cliente):
    pedido = Pedido.persiste_pedido(cd_cliente=cd_cliente, 
                                    dt_entregaprevista=date.today() + timedelta(days=5))
    pedido['data'].dt_pedido = datetime.strftime (pedido['data'].dt_pedido, '%d/%m/%Y')
    pedido['data'].dt_entregaprevista = datetime.strftime (pedido['data'].dt_entregaprevista, '%d/%m/%Y')
    
    return pedido
