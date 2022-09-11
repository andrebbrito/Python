import abc

class Pessoa (metaclass=abc.ABCMeta):
    def __init__(self, nome):
        self.nome = nome
    @abc.abstractmethod
    def nacionalidade(self):
        pass

class Hermano(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
    def nacionalidade(self):
        return 'argentino'

class Brazuca(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
    def nacionalidade(self):
        return 'brasileiro'

p2 = Hermano('Pablo')
p3 = Brazuca('João')
p1 = Pessoa('Maria')

print('{0} é {1}'.format(p1.nome,p1.nacionalidade()))
print('{0} é {1}'.format(p2.nome,p2.nacionalidade()))
print('{0} é {1}'.format(p3.nome,p3.nacionalidade()))