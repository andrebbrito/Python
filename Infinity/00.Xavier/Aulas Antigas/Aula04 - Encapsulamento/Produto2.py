# ------------------------------------
# Este arquivo contém todas as classes
# referentes a produtos
# ------------------------------------
# -------------------------------
# Classe Produto
# -------------------------------
class Produto:
    def __init__(self, nome, valor, descricao):
        self.nome = nome
        self.preco = valor
        self.descricao = descricao
# preços podem ter até 10% de desconto na mudança de valor

    def getPreco(self):
        return self.preco

  
    def setPreco(self,val):
        preco_min = self.preco * 0.10
        preco_min = self.preco - preco_min # mínimo é 10% menos que o preço original
        if (val >= preco_min):
            self.preco = val
            return True
        else:
            return False
