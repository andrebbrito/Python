from Estoque import Produto

prod1 = Produto(1,"biscoito",3.00)
prod2 = Produto(2,"leite em caixa",7.00)
prod3 = Produto(3,"café soluvel",5.00)

prod2.setPreco(6.50)

print(prod1.descricao, prod1.preco)
print(prod2.descricao, prod2.preco)
print(prod3.descricao, prod3.preco)
print("------ Promoção ------")
print(prod1.descricao, prod1.getPreco())
print(prod2.descricao, prod2.getPreco())
print(prod3.descricao, prod3.getPreco())
