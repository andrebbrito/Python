class Medicos:
    def __init__(self, crm, nome, idade, salario):
        self.crm = crm
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def calculo(self):
        if self.idade > 55:
            return self.salario * 0.8
