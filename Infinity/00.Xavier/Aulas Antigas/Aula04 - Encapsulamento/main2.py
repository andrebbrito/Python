from Produto2 import Produto

produto1 = Produto('Escova', 40.0 ,'Escova de cabelo')
print ('-----------------')
print ('Valor do Produto (*antes):',produto1.getPreco())
produto1.setPreco(38.0)
print ('-----------------')
print ('Valor do Produto (depois):',produto1.getPreco())
print ('-----------------')