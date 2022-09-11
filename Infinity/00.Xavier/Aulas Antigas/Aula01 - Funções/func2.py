def calcula(numero1, numero2 = 0, operacao = "+"):
    if operacao == "+":
        resposta = numero1 + numero2
    if operacao == "-":
        resposta = numero1 - numero2
    return resposta
# ----------------------------------
n1 = 7
n2 = 5
print("Resultado da função:", calcula(n1,n2,"+"))
print("Resultado da função:", calcula(n1,n2,"-"))
print("Resultado da função:", calcula(n1,n2))
print("Resultado da função:", calcula(n1))
