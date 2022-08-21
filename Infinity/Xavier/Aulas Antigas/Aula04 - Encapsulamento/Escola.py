class Aluno:
    def __init__(self,mt,nm):
        self.__matricula = mt
        self.__nome = nm
    
    @property # get de matricula
    def matricula(self):
        return self.__matricula
    
    @property # get de nome
    def nome(self):
        return self.__nome
    
    @matricula.setter # set de matricula
    def matricula(self,mat):
        print("não pode alterar a matrícula!")
    
    @nome.setter # set de nome
    def nome(self,novoNome):
        self.__nome = novoNome
    
    
    

class Funcionario:
    pass

class Professor:
    pass
