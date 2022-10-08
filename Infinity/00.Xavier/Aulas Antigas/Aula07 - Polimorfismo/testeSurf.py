from Surf import Patrocinador, Atleta
from Surf import CampeonatoLenda, CampeonatoProfisional, CampeonatoAmador

pat1 = Patrocinador('OndaLivre Pranchas', 50000)
pat2 = Patrocinador('Maresia Surfwear', 100000)
pat3 = Patrocinador('McRonald', 20000)

patrocinadores = [pat1,pat2,pat3]

at1 = Atleta('Pedro', 18, 0, 'amador')
at2 = Atleta('Marcos', 22, 10, 'amador')
at3 = Atleta('Lucia', 21, 100, 'profissional')
at4 = Atleta('Jorge', 19, 50, 'profissional')
at5 = Atleta('Helena', 26, 300, 'lenda')
at6 = Atleta('Antonio', 28, 400, 'lenda')

atletas = [at1,at2,at3,at4,at5,at6]

camp1 = CampeonatoAmador('amador','Surf na Veia','Recife',10000,patrocinadores)
camp1.incliurAtletas(atletas)
camp1.vencidoPor(at5)
camp2 = CampeonatoProfisional('profissional','Copa Surf','Natal',25000,patrocinadores)
camp2.incliurAtletas(atletas)
camp2.vencidoPor(at4)
camp3 = CampeonatoLenda('lenda','Desafio das Ondas','Rio de Janeiro',50000,patrocinadores)
camp3.incliurAtletas(atletas)
camp3.vencidoPor(at6)

part = ""
print("=========================="*2)

print("Campeonato : {0} ({1}) em {2}".format(camp1.nome,camp1.categoria,camp1.local))
for a in camp1.atletas:
    print("             Participante: ", a.nome)
print("             Vencedor: [{0}]".format(camp1.vencedor))

print("Campeonato : {0} ({1}) em {2}".format(camp2.nome,camp2.categoria,camp2.local))
for a in camp2.atletas:
    print("             Participante: ", a.nome)
print("             Vencedor: [{0}]".format(camp2.vencedor))

print("Campeonato : {0} ({1}) em {2}".format(camp3.nome,camp3.categoria,camp3.local))
for a in camp3.atletas:
    print("             Participante: ", a.nome)
print("             Vencedor: [{0}]".format(camp3.vencedor))

print("==========================")
