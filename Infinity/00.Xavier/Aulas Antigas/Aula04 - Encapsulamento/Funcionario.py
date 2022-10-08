# ------------------------------------
# Este arquivo contém todas as classes
# referentes a funcionarios de uma empresa
# ------------------------------------
# -------------------------------
# Classe Funcionario
# -------------------------------
class Funcionario:
    def __init__(self, nm, sl, mt, fu):
        self.nome = nm
        self._salario = sl
        self.matricula = mt
        self.funcao = fu
# Regras:
# salários não podem diminuir
# salários só podem aumentar até 20% a mais
    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self,novo_salario):
        if (novo_salario < self._salario): # salários não podem diminuir
            return False
        elif (novo_salario > (self._salario * 1.2)): # salários só podem aumentar até 20% a mais
            return False
        else:
            self._salario = novo_salario
            return True
        
class FolhaPagto:
   def __init__(self,funcs):
      self.funcionarios = funcs
      
   def valorTotal(self):
      total = 0.0
      for p in self.funcionarios:
         total += p.salario
      return total