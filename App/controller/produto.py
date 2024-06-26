
from models.produto import Produto
from models.produto_estoque import Produto_Estoque



# def consulta_produto_por_codigo(cd_produto):
#     produto = Produto.busca_produto_por_codigo(cd_produto)
#     return produto

# def consulta_produto_por_nome(nm_produto):
#     produto = Produto.busca_produto_por_nome(nm_produto)
#     return produto

def consulta_produto_estoque(cd_produto):
    produto_estoque = Produto_Estoque.consulta_produto_estoque(cd_produto)    
    return produto_estoque

def lista_produtos():
    produtos = Produto.lista_produtos()
    return produtos

def consulta_todos_produtos_por_nome(nm_produto):
    produtos = Produto.busca_todos_produtos_por_nome(nm_produto)
    return produtos

def adiciona_produto_pedido(cd_produto):
    produto = Produto_Estoque.consulta_produto_estoque(cd_produto)
    if not produto:
        return produto['mensagem']
    else:
        if produto['data'].qt_produtoestoque <= 0:
            return {"status": 0, "data": None, "mensagem": "Produto sem estoque!"}
        else:
            return {"status": 1, "data": produto, "mensagem": "Produto encontrado!"}
