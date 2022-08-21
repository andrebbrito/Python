from re import A
from socket import ALG_SET_AEAD_ASSOCLEN


def calcula(numero):
    " Esta função foi escrita na aula"
    resposta = (numero * 2) + 5
    return resposta

# ----------------------------------

print("Resultado da função:", calcula(30))
n = 15
x = calcula(n)
print("Segundo resultado:", x)
print(calcula.__doc__)

