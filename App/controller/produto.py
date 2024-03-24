
from App.models.produto_estoque import Produto_Estoque
from models.produto import Produto


def adiciona_produto_pedido(cd_produto):
    qtd_produtos = Produto_Estoque.consulta_produto_estoque(cd_produto)
    if not qtd_produtos:
        return qtd_produtos['mensagem']
    else:
        if qtd_produtos['data'].qt_produtoestoque <= 0:
            return {"status": 0, "data": "", "mensagem": "Produto sem estoque"}
        else: 
            produto = Produto.busca_produto_por_id(cd_produto)

            # produtos = []
            # produto = busca_produto_por_id(cd_produto)
            # produtos.append({produto['data'].nm_produto, produto['data'].ds_produto, produto['data'].tp_embalagemproduto, produto['data'].vl_produto})
            # return Produto.lista_produtos()