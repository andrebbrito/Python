dados1 = {'alunos':[{'nome':'edu','idade':'17'},
                    {'nome':'ana','idade':'16'}]}
dados2 = [{'nome':'edu','idade':'17'},
            {'nome':'ana','idade':'16'}]
dados3 = {'aluno1':{'nome':'edu','idade':'17'},
            'aluno2':{'nome':'ana','idade':'16'}}

print ('--- dados ------')
print (dados1)
print ('--- dados2 -----')
print (dados2)
print ('--- dados3 -----')
print (dados3)

print ('\n<<<< inserindo um novo "sub-dicionário >>>>\n')
dados1['alunos'].append({'nome':'maria','idade':'15'})
dados2.append({'nome':'maria','idade':'15'})
dados3['aluno3'] = {'nome':'maria','idade':'15'}

print ('--- dados ------')
print (dados1)
print ('--- dados2 -----')
print (dados2)
print ('--- dados3 -----')
print (dados3)

# fazendo referencia a elementos dos dicionários
print ('\n<<<< inserindo um novo "sub-dicionário >>>>\n')
print (dados1['alunos'][1])
print (dados1['alunos'][2]['idade'])

print (dados2[1])
print (dados2[2]['idade'])

print (dados3['aluno2'])
print (dados3['aluno3']['idade'])
