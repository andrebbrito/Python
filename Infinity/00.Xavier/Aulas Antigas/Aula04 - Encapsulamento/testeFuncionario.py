from Funcionario import Funcionario
from Funcionario import FolhaPagto


func1 = Funcionario('\nPedro', 3000.00, 111, 'Vendedor')
func2 = Funcionario('Maria', 5000.00, 222, 'Gerente')
func3 = Funcionario('Fernando', 2000.00, 333, 'Atendente')

print('Funcionario 1:', func1.nome, func1.funcao, func1.salario)
print('Funcionario 2:', func2.nome, func2.funcao, func2.salario)
print('Funcionario 3:', func3.nome, func3.funcao, func3.salario)

salarios = [func1, func2, func3]
listaPagamentos = FolhaPagto(salarios)

print('---(Folha de Pagamentos)---')
print('Valor Total:', listaPagamentos.valorTotal())