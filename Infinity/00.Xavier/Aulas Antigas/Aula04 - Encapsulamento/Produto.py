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
        self.__preco = valor
        self.descricao = descricao
# preços podem ter até 10% de desconto na mudança de valor

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self,val):
        preco_min = self.__preco * 0.10
        preco_min = self.__preco - preco_min # mínimo é 10% menos que o preço original
        if (val >= preco_min):
            self.__preco = val
            return True
        else:
            return False
