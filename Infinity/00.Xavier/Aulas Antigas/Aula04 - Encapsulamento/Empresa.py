class FolhaPagto:
    def __init__(self,funcs):
        self.funcionarios = funcs

    def exibeTotalFolha(self):
        total = 0
        for f in self.funcionarios:
            total += f.salario
        return total