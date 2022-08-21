from tkinter import E


class Produtos():
    def __init__(self,nome,preço_unit,unidade_medida,qtd_estocada):
        self.nome = nome
        self.precoUnit = preço_unit
        self.unidade = unidade_medida
        self.qtdEstocada = qtd_estocada
    def totalEstoque(self):
        pass

class Alimentos(Produtos):
    def __init__(self, nome, preço_unit, unidade_medida, qtd_estocada):
        super().__init__(nome, preço_unit, unidade_medida, qtd_estocada)
    def totalEstoque(self):
        resp = (self.qtdEstocada * self.precoUnit) * 1.15
        return resp
class Eletronicos(Produtos):
    def __init__(self, nome, preço_unit, unidade_medida, qtd_estocada):
        super().__init__(nome, preço_unit, unidade_medida, qtd_estocada)
    def totalEstoque(self):
        resp = (self.qtdEstocada * self.precoUnit) * 1.10
        return resp
class Higiene(Produtos):
    def __init__(self, nome, preço_unit, unidade_medida, qtd_estocada):
        super().__init__(nome, preço_unit, unidade_medida, qtd_estocada)
    def totalEstoque(self):
        resp = (self.qtdEstocada * self.precoUnit) * 0.80
        return resp
# -----------------------------------------
p1 = Alimentos('feijão',5.00,'kg',200)
p2 = Eletronicos('celular',1500.00,'un',100)
p3 = Higiene('detergente',7.00,'lt',300)

print (p1.nome, p1.totalEstoque(), (p1.qtdEstocada * p1.precoUnit))
print (p2.nome, p2.totalEstoque(), (p2.qtdEstocada * p2.precoUnit))
print (p3.nome, p3.totalEstoque(), (p3.qtdEstocada * p3.precoUnit))
    
