# ------------------------------------
# Este arquivo contém todas as classes
# referentes a uma escola de musica
# ------------------------------------
# -------------------------------
# Classe Professor
# -------------------------------
class Professor:
    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao

# -------------------------------
# Classe Instrumento
# -------------------------------
class Instrumento:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
    
    def dificuldade(self):
        return self.professor.pontuacao

# -------------------------------
# Classe InstruCorda
# -------------------------------
class InstruCorda(Instrumento):
    def __init__(self, nome, professor, qtd_cordas, tipo_corda):
        super().__init__(nome, professor)
        self.qtd_cordas = qtd_cordas
        self.tipo_corda = tipo_corda

    def dificuldade(self):
        if (self.tipo_corda == "aço"):
            return (self.professor.pontuacao * self.qtd_cordas)
        else:
            return self.professor.pontuacao

# -------------------------------
# Classe IntruPercussao
# -------------------------------
class InstruPercussao(Instrumento):
    def __init__(self, nome, professor, tem_baqueta):
        super().__init__(nome, professor)
        self.tem_baqueta = tem_baqueta
