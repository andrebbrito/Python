class Pessoa:
    def __init__(self):                
        self.__nome = ''
        self.__sobrenome = ''
        self.__nascimento = '01/01/2022'
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome        
        
        
        
        