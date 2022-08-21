def calcula(numero1, numero2 = 0):
    resp1 = numero1 + numero2
    resp2 = numero1 - numero2
    return resp1, resp2
# ----------------------------------
n1 = 7
n2 = 5

r1, r2 = calcula(n1,n2)
r3 = calcula(n1,n2)

print("Resultado da função:", r1, r2)
print("Resultado da função:", r3)
