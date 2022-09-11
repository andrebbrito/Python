class Aluno:
    def __init__(self,nm,semstre,mat):
        self.nome = nm
        self.semestre = semstre
        self.matricula = mat

class Notas:
    def __init__(self,nom,discipl,vlr,nots):
        self.nome = nom
        self.disciplina = discipl
        self.valor = vlr
        self.notas = nots

    def score(self):
        totalPontos = 0
        for n in self.notas:
            totalPontos += n.valor
        return totalPontos