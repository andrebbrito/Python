# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 01 (Funções)
# Pgm8: Atividade 4
#       Função recebe 1 valor inteiro e positivo
#       e devolve o somatório deste valor
# ----------------------------------

# definindo a função
def somatorio(valor):
    soma = 0
    for num in range(1,valor+1,1):
        print ('somando',num,'...')
        soma = soma + num
    return soma

# --- programa executando a função ---
print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

v = int(input('Entre com o valor: '))

print('Somatório do valor :',somatorio(v))

print('\n----- FIM DA EXECUÇÃO: -----\n')