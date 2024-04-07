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
        print(pedido)
        return pedido
    
    def baixa_estoque(produtos):
        produtos_ordenados_dt_validade = []
        for produto in produtos:
            qt_produto = produto.qt_produto
            produtos_menor_dt_validade = Produto_Estoque.busca_produto_estoque_ordenado_dt_validade(produto.cd_produto)
            if produtos_ordenados_dt_validade['status']:
                for produto_estoque in produtos_menor_dt_validade:
                    if qt_produto <= produto_estoque.qt_produtoestoque:
                        produtos_ordenados_dt_validade.append = {
                                                                    produto.cd_produto, 
                                                                    produto_estoque.cd_estoque, 
                                                                    produto_estoque.nr_lote,
                                                                    qt_produto
                                                                }
                        break
                    else:
                        produtos_ordenados_dt_validade.append = {
                                                                    produto.cd_produto, 
                                                                    produto_estoque.cd_estoque, 
                                                                    produto_estoque.nr_lote,
                                                                    qt_produto
                                                                }
                        qt_produto -= produto_estoque.qt_produtoestoque

        for produto in produtos_ordenados_dt_validade:
            Produto_Estoque.remove_produto_estoque(produto.cd_produto, produto.qt_produto)
            produtos_ordenados_dt_validade.pop()

        return {'status': 1, 'data': None, 'mensagem': "Estoque atualizado com sucesso."}
        