# ------------------------------------
# Este arquivo contém todas as classes
# referentes a uma medicos
# ------------------------------------
# -------------------------------
# Classe Medico
# -------------------------------
class Medico:
    def __init__(self, crm, nome, idade, salario):
        self._crm = crm
        self._nome = nome
        self._idade = idade
        self._salario = salario

    def aposentadoria(self):
        if (self._idade > 55):
            return self._salario * 0.8
        else:
            return 0

# -------------------------------
# Classe Auxiliar
# -------------------------------
class Auxiliar(Medico):
    def __init__(self, crm, nome, idade, salario):
        super().__init__(crm, nome, idade, salario)

    def aposentadoria(self):
        if (self._idade > 60):
            return self._salario * 0.8
        else:
            return 0

    
# -------------------------------
# Classe Cirurgiao
# -------------------------------
class Cirurgiao(Medico):
    def __init__(self, crm, nome, idade, salario):
        super().__init__(crm, nome, idade, salario)

    def aposentadoria(self):
        if (self._idade > 50):
            return (self._salario * 0.8)+2000
        else:
            return 0
