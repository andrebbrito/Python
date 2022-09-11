
class Funcionario:
    def __init__(self, nm, sl, mt, fu):
        self.nome = nm
        self._salario = sl
        self.matricula = mt
        self.funcao = fu

    def salario(self):
        return self._salario

    @salario.setter
    def salario(self,novo_salario):
        if (novo_salario < self._salario):
            return False
        elif (novo_salario > (self._salario * 1.2)):
            return False
        else:
            self._salario = novo_salario
            return True

class FolhaPagto:
    def __init__(self, funcs):
        self.funcionarios = funcs
        
    def exibeTotalFolha(self):
        total = 0
        for f in self.funcionarios:
            total += f.salario
        return total