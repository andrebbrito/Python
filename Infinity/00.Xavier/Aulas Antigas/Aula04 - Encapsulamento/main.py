from Produto import Produto

produto1 = Produto('Escova', 40.0 ,'Escova de cabelo')
print ('-----------------')
print ('Valor do Produto (antes):',produto1.preco)
produto1.preco = 38.0
print ('-----------------')
print ('Valor do Produto (depois):',produto1.preco)
print ('-----------------')