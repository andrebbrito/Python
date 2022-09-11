numeros = []
i = 0
while (i<10):
    num = int(input("informe um número:"))
    numeros.append(num)
    i = i+1

impares=[]

for n in numeros:
    if ((n%2) != 0):
        impares.append(n)

print("Os ímpares são:",impares)