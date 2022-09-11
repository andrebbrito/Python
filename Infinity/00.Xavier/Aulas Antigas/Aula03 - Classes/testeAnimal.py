from Animal import Animal
from Animal import Funcionario

coelho = Animal("penalonga","mamífero","herbívoro")
print("Coelho:",coelho.nomeAnimal,coelho.alimentacao)
aranha = Animal("pernas","inseto","carnívoro")
print("Aranha:",aranha.nomeAnimal,aranha.alimentacao)
humano = Animal("Renan","mamífero","onívoro")
print("Humano:",humano.nomeAnimal,humano.alimentacao)
func1 = Funcionario(666,"Xavier")
print("funcionario:",func1.matricula, func1.nome)
