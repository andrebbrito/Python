alunos = {"joão":[5,7], "maria":[8,6]}
for alu in alunos:
    somaDeNotas = sum(alunos[alu])
    qtdNotas = len(alunos[alu])
    print("A média do aluno(a)",alu,"é",somaDeNotas/qtdNotas)
    print(".....................................")
    
