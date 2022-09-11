# -------------------------------
# Classe Patrocinador
# -------------------------------
class Patrocinador:
    def __init__(self, nome, valor):
        self.nome = nome
        self.nome = valor

# -------------------------------
# Classe Atleta
# -------------------------------
class Atleta:
    def __init__(self, nome, idade, pontuacao, categoria)
        self.nome = nome
        self.idade = idade
        self.pontuacao = pontuacao
        self.categoria = categoria

# -------------------------------
# Classe Campeonato
# -------------------------------
class Campeonato:
    def __init__(self, nome, local, premiacao, patrocinador, atleta):
        self._nome = nome
        self._local = local
        self._premiacao = premiacao
        self._patrocinador = patrocinador
        self._atleta = atleta


class Campeonato:
    def __init__(self, categoria, nome, local, patrocinador, premiacao, ):
        self.categoria = categoria
        self.nome = nome
        self.local = local
        self.patrocinador = patrocinador
        self.premiacao = premiacao
        self.atletas = []
        self.vencedor = ''

    def incliurAtletas(self, atletas):
        self.atletas = atletas

    def vencidoPor(self, atleta):
        self.vencedor = atleta.nome
# -------------------------------
# Classe Atleta
# -------------------------------


