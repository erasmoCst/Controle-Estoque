from models.pedido import Pedido

class Consulta_Pedido ():
    def lista_todos_pedidos():
        pedidos = Pedido.busca_todos_pedidos()
        return pedidos
    
    def consulta_pedido_por_codigo(cd_pedido):
        pedido = Pedido.busca_pedido_por_codigo(cd_pedido)
        return pedido
        
    # def consulta_PJ(cpf_cnpj):
    #     return (Pessoa_Juridica.busca_dados_cliente_CNPJ(cpf_cnpj))
