
# Altere o código da atividade 1 para que ele exiba os números múltiplos de 2, 5 e 7 e 
# que estejam dentro do intervalo entre 100 e 500 (incluindo o 100 e o 500).

inicio = 100 
fim = 501
numero = 2 
multiplo = 0

for posicao in range(inicio, fim): 
        multiplo = numero * posicao
        print(posicao, numero, multiplo)
        

        