from Banco import ContaCorrente

conta1 = ContaCorrente('111','999')
conta2 = ContaCorrente('222','999','777')
print("Conta 1 (antes do saque):", conta1.agencia, conta1.numero, conta1.saldo)
print("Conta 2 (antes do saque):", conta2.agencia, conta2.numero, conta2.saldo)
conta1.sacar(10)
conta1.transfere(conta2,5)
print("Conta 1 (depois do saque):", conta1.agencia, conta1.numero, conta1.saldo)
print("Conta 2 (depois do saque):", conta2.agencia, conta2.numero, conta2.saldo)
