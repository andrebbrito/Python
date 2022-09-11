# ------------------------------------
# Este arquivo contém todas as classes
# referentes a uma empresa
# ------------------------------------
# -------------------------------
# Classe Funcionario
# -------------------------------
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def salarioLiquido(self,itens_descontos):
        liquido = self._salario
        for desconto in itens_descontos:
            liquido -= desconto
        return liquido

# -------------------------------
# Classe Gerente
# -------------------------------
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qt_gerenciados):
        super().__init__(nome, cpf, salario)
        self.__senha = senha
        self.__qt_gerenciados = qt_gerenciados
