class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, titular, saldo):
        conta = ContaBancaria(titular, saldo)
        self.contas.append(conta)

    def listar_saldos(self):
        for conta in self.contas:
          
            print(f"Titular: {conta.titular} | Saldo: R${conta.saldo:,.2f}")

    def deposito_banco(self, titular, valor):
        
        for conta in self.contas:
            if conta.titular == titular:
                conta.deposito(valor)
                return
        print(f"Conta de {titular} não encontrada.")

    def saque_banco(self, titular, valor):
       
        for conta in self.contas:
            if conta.titular == titular:
                conta.saque(valor)
                return
        print(f"Conta de {titular} não encontrada.")


banco = Banco()

banco.adicionar_conta("João", 1000)
banco.adicionar_conta("Maria", 500)
banco.adicionar_conta("Pedro", 1200)

banco.listar_saldos()

