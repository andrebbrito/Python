

# Altere o código da atividade 1, criando uma variável divisor e, em seguida, 
# verifique quais os números no intervalo entre 0 e 1000 (incluindo o 0 e excluindo o 1000) são múltiplos da variável divisor.

# • Por exemplo, se o valor de divisor for igual a 3, todos os números múltiplos de 3, 
# dentro do intervalo, deverão ser exibidos (0, 3, 6, 9, ..., 996, 999).

inicio = 0
fim = 1001
divisor = 3 
multiplo = 0

for posicao in range(inicio, fim): 
        multiplo = divisor * posicao
        print(posicao, divisor, multiplo)
        