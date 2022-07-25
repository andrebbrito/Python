
# Para resolver este problema, considere as seguintes dicas:
# • A soma deverá ser 1 + 2 + 7 + 9 + 5 + 7 = 𝟑𝟏;
# • Utilize o laço de repetição for … in; para percorrer cada caractere da string;
# • Utilize a conversão do tipo string para o tipo inteiro (int(caractere)) para converter os caracteres em valores numéricos;
# • Utilize uma variável auxiliar, soma, para acumular o somatório dos valores.
      
numero = '127957'

tamanho = len(numero)
soma = 0

for posicao in range(0,tamanho) :
    soma = soma + int(numero[posicao]) 
    print(numero[posicao])

print(soma)


x = (2 + 3) * 5 - 1

print(x)






    
    
    





