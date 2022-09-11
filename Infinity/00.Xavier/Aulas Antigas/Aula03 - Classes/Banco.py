class ContaCorrente:
    def __init__(self,nm, sh, ag='555', bc='01', sd=15.0):
        self.numero = nm
        self.senha = sh
        self.agencia = ag
        self.banco = bc
        self.saldo = sd
        
    def sacar(self, valor):
        self.saldo = self.saldo - valor
    
    def transfere(self,contaDestino, valorTransferido):
        self.saldo = self.saldo - valorTransferido
        contaDestino.saldo = contaDestino.saldo + valorTransferido