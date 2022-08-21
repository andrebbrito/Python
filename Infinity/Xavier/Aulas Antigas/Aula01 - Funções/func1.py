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
