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

    def calcula_valor_total_pedido(produtos):
        valor_total = 0
        if not produtos:
            return {'status': 0, 'data': None, 'mensagem': "Nenhum produto encontrado."}
        
        for produto in produtos:
            valor_total += produto['produto'].vl_produto * produto['qt_produto']
        
        return {'status': 1, 'data': valor_total, 'mensagem': "Valor total calculado com sucesso."}

    def finalizar_pedido(pedido, produtos):
        print(pedido)
        print(produtos)

        for produto in produtos:
            response = Produto_Pedido.persiste_produto_pedido(pedido['cd_pedido'], 
                                                    produto['produto'].cd_produto, 
                                                    produto['qt_produto'])
        response = Pedido.atualiza_data_entrega(pedido['cd_pedido'], pedido['dt_entrega'])
        Base.commit()

        return {'status': 1, 'data': None, 'mensagem': "Valor total calculado com sucesso."}

    # def cancelar_pedido(pedido):
    #     Pedido.remove_pedido(pedido['data'].cd_pedido)
    #     Base.commit()
    
    # def consultar_pedido(cd_pedido):
    #     pedido = Pedido.consulta_pedido(cd_pedido)
    #     pedido['data'].dt_pedido = datetime.strftime (pedido['data'].dt_pedido, '%d/%m/%Y')
    #     pedido['data'].dt_entregaprevista = datetime.strftime (pedido['data'].dt_entregaprevista, '%d/%m/%Y')
        
    #     return pedido
    
    # def consultar_produtos_pedido(cd_pedido):
    #     produtos = Produto_Pedido.consulta_produtos_pedido(cd_pedido)
        
    #     return produtos
        
        