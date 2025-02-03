class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
       
        print(f"Depósito de R${valor} realizado com sucesso.")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
           
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            
            print(f"Saldo insuficiente para saque de R${valor}.")

    def exibir_saldo(self):
       
        print(f"Saldo atual: R${self.saldo}")



conta = ContaBancaria()

conta.depositar(1000)    
conta.sacar(500)         
conta.exibir_saldo()    
conta.sacar(600)         
conta.exibir_saldo()     