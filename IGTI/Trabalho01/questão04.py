# variáveis do tipo string 

nome = 'João da Silva' 
cidade = 'São Paulo' 
cpf = '123.456.789-00'

# Transforme todos os caracteres das variáveis em maiúsculo;
print(nome.upper() + ' - ' + cidade.upper() +  ' - ' + cpf.upper())  

# Transforme todos os caracteres das variáveis em minúsculo;
print(nome.lower() + ' - ' + cidade.lower() +  ' - ' + cpf.lower())  

# Exiba a posição do caractere ã, se presente, em cada uma das variáveis;
print(nome.find('ã'))
print(cidade.find('ã'))
print(cpf.find('ã'))

# Exiba o número de caracteres de cada variável;
print(len(nome))
print(len(cpf))
print(len(cpf))

# Remova os pontos (.) e o hífen (–) da variável cpf.
print(cpf.replace('.','-'))
      




