# ------------------------------------
# Em um campeonato de surf podem ter 3 categorias:
# ● Amador
# ● Profissional
# ● Lenda
# Para todos os tipos de campeonato, temos o cadastro do nome do campeonato, local onde
# ocorrerá, premiação, patrocinadores (previamente cadastrados com nome e valor) e os
# atletas. Os atletas terão nome, idade, pontuação e categoria que compete (Amador,
# profissional ou lenda). Os atletas lenda podem participar de qualquer competição, já os
# profissionais, apenas do profissional e do amador, sendo que o amador só poderá participar
# do próprio circuito. É preciso haver este bloqueio no sistema. A pontuação do atleta que
# ganha o campeonato é:
# ● Amador: 10 pontos
# ● Profissional: 50 pontos
# ● Lenda: 100 pontos
# ------------------------------------
import abc
# -------------------------------
# Classe Patrocinador
# -------------------------------
class Patrocinador:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

# -------------------------------
# Classe Atleta
# -------------------------------
class Atleta:
    def __init__(self, nome, idade, pontuacao, categoria):
        self.nome = nome
        self.idade = idade
        self.pontuacao = pontuacao
        self.categoria = categoria

# -------------------------------
# Classe Campeonato
# -------------------------------
class Campeonato(metaclass=abc.ABCMeta):
    def __init__(self, categoria, nome, local, premiacao,patrocinadores):
        self.categoria = categoria
        self.nome = nome
        self.local = local
        self.premiacao = premiacao
        self.patrocinadores = patrocinadores
        self.atletas = []
        self.vencedor = ''
    
    @abc.abstractmethod
    def incliurAtletas(self,atletas):
        pass

    @abc.abstractmethod
    def vencidoPor(self,atleta):
        pass

# -------------------------------
# Classe CampeonatoLenda
# -------------------------------
class CampeonatoLenda(Campeonato):
    def __init__(self, categoria, nome, local, premiacao,patrocinadores):
        super().__init__(categoria, nome, local, premiacao,patrocinadores)

    def incliurAtletas(self,atletas):
        for a in atletas:
            if (a.categoria == 'lenda'):
                self.atletas.append(a)

    def vencidoPor(self,atleta):
        self.vencedor = atleta.nome
        atleta.pontuacao += 100

# -------------------------------
# Classe CampeonatoProfissional
# -------------------------------
class CampeonatoProfisional(Campeonato):
    def __init__(self, categoria, nome, local, premiacao,patrocinadores):
        super().__init__(categoria, nome, local, premiacao,patrocinadores)

    def incliurAtletas(self,atletas):
        for a in atletas:
            if (a.categoria == 'lenda') or (a.categoria == 'profissional'):
                self.atletas.append(a)

    def vencidoPor(self,atleta):
        self.vencedor = atleta.nome
        atleta.pontuacao += 50

# -------------------------------
# Classe CampeonatoAmador
# -------------------------------
class CampeonatoAmador(Campeonato):
    def __init__(self, categoria, nome, local, premiacao,patrocinadores):
        super().__init__(categoria, nome, local, premiacao,patrocinadores)

    def incliurAtletas(self,atletas):
        self.atletas = atletas
            
    def vencidoPor(self,atleta):
        self.vencedor = atleta.nome
        atleta.pontuacao += 10
