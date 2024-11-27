
class Conta_Corrente:
    def __init__(self, num_conta, nome_correntista, saldo=0):
       
        self.num_conta = num_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
 
    def alterar_nome(self, novo_nome):
       
        self.nome_correntista = novo_nome
        print(f"alterado {self.nome_correntista}")
 
    def deposito(self, valor):
       
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido. O valor deve ser maior que zero.")
 
    def saque(self, valor):
   
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor de saque inválido. O valor deve ser maior que zero.")
 

banca1= float(input("digite seu deposio:"))
banca2= float(input("digite seu saque:"))
 
conta1 = Conta_Corrente(924772, "Hugo Freres")
conta1.deposito(banca1)
conta1.saque(banca2)
conta1.alterar_nome("nome alterado para Hugo Sousa")

 