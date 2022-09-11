# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 02 (Listas)
# Uma demonstração passo a passo de
# uso de dicionário
# ----------------------------------

# Primeiro, vamos criar um dicionário vazio
alunos = {}

# Agora vamos povoar o dicionário com 4 novos 
# alunos, informando a chave (nome do aluno) 
# e o valor (uma lista com 3 notas) para cada aluno
alunos['Ana'] = [3,5,8]
alunos['Pedro'] = [6,9,6]
alunos['Marta'] = [9,8,10]
alunos['Eduardo'] = [7,6,10]

# Vamos exibir o conteúdo completo do dicionário
print ( alunos )
print ( '-------------------------------' )

# Para saber quantos alunos temos no dicionário
# basta usar a função len(). Ela conta quantas
# ocorrencias de chave:valor existem armazenadas
print ( 'Quantidade de alunos:',len(alunos) )

# Para saber quantas notas um determinado aluno
# possui, usamos a mesma função len() para contar
# as ocorrências existentes na lista de notas do
# aluno. Lembre-se: ao chamar um dicionário indicando
# uma chave específica (no caso, o nome do aluno)
# é retornado o valor dessa chave (no caso, a lista
# de notas).
print ( 'Quantidade de notas de Pedro:',len(alunos['Pedro']) )

# Para somar todas as notas de um aluno
# basta usar a função sum(). Ela soma todas as
# ocorrencias de notas de um determinado aluno
print ( 'Soma das notas de Marta:',sum(alunos['Marta']) )

# Para calcular a média de cada um dos alunos
# fazemos um loop for onde a váriavel "a" assume
# a chave/valor de um novo aluno a cada execução 
# do for (até ter feito isso para cada um dos alunos
# existentes no dicionário).
# Para cada aluno processado, calculamos sua média 
# somando todas as suas notas (usando a função 
# sum()) e dividindo pela quantidade de notas deste
# aluno (usando a função len()).
print ( '-------------------------------' )
for a in alunos:
    media = sum(alunos[a])/len(alunos[a])
    print('{} teve media {:.2f}'.format(a,media))
