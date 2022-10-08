# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 02 (Dicionário)
# Atividade 2: calcula médias de alunos
# ----------------------------------

print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

aluno = {}

def mediaNotas(alu,nm):
    return sum(alu[nm])/2

while (True):
    nome = input('Nome do aluno:')
    if (nome == ''):
        break;
    n1 = float(input ('Nota 1:'))
    n2 = float(input ('Nota 2:'))
    aluno[nome] = [n1,n2]

a = input('calcular média do aluno:')
med = mediaNotas(aluno,a)
print(f'A média do aluno {a} é {med}')

print('\n----- FIM DA EXECUÇÃO: -----\n')