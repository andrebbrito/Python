from Empresa import Gerente

gerente = Gerente("Ana","4455577",25000.00,"654321",12)
plano_saude = 300
inss = 280
ir = 500
lista_descontos = {plano_saude, inss, ir}

salLiq = gerente.salarioLiquido(lista_descontos)

print(salLiq)

