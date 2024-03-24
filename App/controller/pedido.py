from datetime import date, timedelta
from models.pedido import Pedido


def criar_pedido(cd_cliente):
    pedido = Pedido.persiste_pedido(cd_cliente=cd_cliente, 
                                    dt_entregaprevista=date.today() + timedelta(days=5))
    return pedido
