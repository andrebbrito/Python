from Medico import Medico
from Medico import Auxiliar
from Medico import Cirurgiao


med1 = Medico(111,"Paulo",57,10000)
med2 = Medico(222,"Marcia",35,10000)
aux1 = Auxiliar(333,"Ana",62,10000)
aux2 = Auxiliar(444,"Pedro",44,10000)
cir1 = Cirurgiao(555,"Lucas",57,10000)
cir2 = Cirurgiao(555,"Katia",28,10000)

print("Médico", med1._nome, med1.aposentadoria())
print("Médico", med2._nome, med2.aposentadoria())
print("Auxiliar", aux1._nome, aux1.aposentadoria())
print("Auxiliar", aux2._nome, aux2.aposentadoria())
print("Cirurgião", cir1._nome, cir1.aposentadoria())
print("Cirurgião", cir2._nome, cir2.aposentadoria())
