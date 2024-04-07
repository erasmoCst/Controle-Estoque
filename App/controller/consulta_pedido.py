from models.base import Base
from models.produto_estoque import Produto_Estoque
from models.produto_pedido import Produto_Pedido
from models.pedido import Pedido

class Consulta_Pedido ():
    def lista_todos_pedidos():
        pedidos = Pedido.busca_todos_pedidos()
        return pedidos
    
    def consulta_pedido_por_codigo(cd_pedido):
        pedido = Pedido.busca_pedido_por_codigo(cd_pedido)
        return pedido
    
    def consulta_pedido_por_codigo_cliente(cliente):
        pedido = Pedido.busca_pedido_por_codigo_cliente(cliente)
        return pedido    
    
    def consulta_pedidos_nao_atendidos():
        pedidos = Pedido.busca_pedidos_nao_atendidos()
        return pedidos
    
    def consulta_pedido_nao_atendido_por_codigo(cd_pedido):
        pedido = Pedido.busca_pedido_nao_atendido_por_codigo(cd_pedido)
        return pedido
    
    def consulta_pedido_nao_atendido__por_codigo_cliente(cliente):
        pedido = Pedido.busca_pedido_nao_atendido_por_codigo_cliente(cliente)
        return pedido  
    
    def consulta_detalhes_pedido_por_codigo(cd_pedido):
        pedido = Produto_Pedido.busca_detalhes_pedido_por_codigo(cd_pedido)
        return pedido

    def baixa_estoque(cd_pedido, produtos):
        produtos_ordenados_dt_validade = []
        for produto in produtos:
            qt_produto = produto.qt_produto
            produtos_menor_dt_validade = Produto_Estoque.busca_produto_estoque_ordenado_dt_validade(produto.cd_produto)
            if produtos_menor_dt_validade['status']:
                for produto_estoque in produtos_menor_dt_validade['data']:
                    if qt_produto <= produto_estoque.qt_produtoestoque:
                        produtos_ordenados_dt_validade.append({
                                                                'cd_produto': produto.cd_produto, 
                                                                'cd_estoque': produto_estoque.cd_estoque, 
                                                                'nr_lote': produto_estoque.nr_lote,
                                                                'qt_produto': qt_produto
                                                             })
                        break
                    else:
                        produtos_ordenados_dt_validade.append({
                                                                'cd_produto': produto.cd_produto, 
                                                                'cd_estoque': produto_estoque.cd_estoque, 
                                                                'nr_lote': produto_estoque.nr_lote,
                                                                'qt_produto': qt_produto
                                                              })
                        qt_produto -= produto_estoque.qt_produtoestoque

        produtos_baixa_estoque = list(produtos_ordenados_dt_validade)
        for produto in produtos_baixa_estoque:
            Produto_Estoque.remove_produto_estoque(produto['cd_produto'],
                                                   produto['cd_estoque'],
                                                   produto['nr_lote'], 
                                                   produto['qt_produto'])
            produtos_ordenados_dt_validade.remove(produto)
        
        if not produtos_ordenados_dt_validade:
            response = Pedido.atualiza_pedido_atendido(cd_pedido)
            
            if response['status']:
                Base.commit()
                return {'status': 1, 'data': None, 'mensagem': "Pedido Atendido e Estoque Atualizado com sucesso."}
        else:
            Base.rollback()
            return {'status': 1, 'data': None, 'mensagem': "Falha ao atualizar estoque."}
