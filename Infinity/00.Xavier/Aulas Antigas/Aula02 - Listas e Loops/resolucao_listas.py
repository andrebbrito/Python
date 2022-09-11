# 1 Forma - Questão 1
listaNomes = []
nome1 = input('Informe o nome 1: ')
listaNomes.append(nome1)
nome2 = input('Informe o nome 2: ')
listaNomes.append(nome2)
nome3 = input('Informe o nome 3: ')
listaNomes.append(nome3)
nome4 = input('Informe o nome 4: ')
listaNomes.append(nome4)
nome5 = input('Informe o nome 5: ')
listaNomes.append(nome5)

print(listaNomes)

# 2 Forma - Questão 1
listaNomes = []
for i in range(5):
    nome = input(f'Informe o {i+1}° nome: ')
    listaNomes.append(nome)
print(listaNomes)


# 1 Forma - Questão 2
listaNumeros = []
for i in range(5):
    numero = input(f'Informe o {i+1}° número: ')
    listaNumeros.append(numero)
print(listaNumeros)
listaNumerosImpares = []
for i in listaNumeros:
    if i % 2 != 0:
        listaNumerosImpares.append(i)
print(listaNumerosImpares)