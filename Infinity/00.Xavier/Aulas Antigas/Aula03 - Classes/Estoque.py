class Produto:
    def __init__(self,codProd,descProd,precoProd):
        self.codigo = codProd
        self.descricao = descProd
        self.__preco = precoProd
    
    def getPreco(self):
        return self.__preco
    
    def setPreco(self,valor):
        if (valor >= (self.preco*0.9)):
            self.__preco = valor
