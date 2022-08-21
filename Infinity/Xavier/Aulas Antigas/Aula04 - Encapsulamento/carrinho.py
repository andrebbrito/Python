class Carrinho:
    def __init__(self, listaDeProdutos):
        self.produtosCarrinho = listaDeProdutos
        
        def valorTotal(self):
            total = 0.0
            for p in self.produtosCarrinho:
                total = total + p.precoprod
            return total