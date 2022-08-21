from Musica import Professor, Instrumento, InstruCorda, InstruPercussao

prof1 = Professor("Coreolino", 3)
prof2 = Professor("Rosicledna", 8)
prof3 = Professor("Evangivaldo", 5)

inst1 = Instrumento("trombone", prof1)
inst2 = InstruCorda("violão",prof2, 6, "nylon")
inst3 = InstruCorda("cavaquinho",prof2, 6, "aço")
inst4 = InstruPercussao("atabaque",prof3,False)
inst5 = InstruPercussao("bateria",prof3,True)

print (inst1.nome,inst1.dificuldade())
print (inst2.nome,inst2.dificuldade())
print (inst3.nome,inst3.dificuldade())
print (inst4.nome,inst4.dificuldade())
print (inst5.nome,inst5.dificuldade())
