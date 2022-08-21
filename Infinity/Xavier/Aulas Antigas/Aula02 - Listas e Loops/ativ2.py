valores = []
# obter os valores
for i in range(10):
    v = int(input("Entre com valor:"))
    valores.append(v)
# testar quem é ímpar
for i in range(10):
    if ((valores[i] % 2) != 0):
        print(valores[i])