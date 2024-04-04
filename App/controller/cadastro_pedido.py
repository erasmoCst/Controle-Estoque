from datetime import date, timedelta, datetime
from models.base import Base
from models.produto_pedido import Produto_Pedido
from models.pedido import Pedido

class Cadastro_Pedido():
    def criar_pedido(cd_cliente):
        pedido = Pedido.persiste_pedido(cd_cliente=cd_cliente, 
                                        dt_entregaprevista=date.today() + timedelta(days=5))
        pedido['data'].dt_pedido = datetime.strftime (pedido['data'].dt_pedido, '%d/%m/%Y')
        pedido['data'].dt_entregaprevista = datetime.strftime (pedido['data'].dt_entregaprevista, '%d/%m/%Y')
        
        return pedido

    def finalizar_pedido(pedido, produtos):
        for produto in produtos:
            Produto_Pedido.persiste_produto_pedido(pedido['data'].cd_pedido, 
                                                    produto['produto'].cd_produto, 
                                                    produto['qt_produto'])

        Pedido.atualiza_data_entrega(pedido['data'], date.today() + timedelta(days=5))        
        Base.commit()
        
        