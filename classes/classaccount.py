class Account:
    def __init__(self,number: int,holder: str,balance: float):
        self.number = number
        self.holder = holder
        self.balance = balance
        
    def withdraw(self, amount: float):

        if amount > 0 and amount <= self.balance:
            self.balance -= amount

    def deposito(self,amount: float):
        if amount > 0:
            self.balance += amount
            # print(f"Deposit R${amount:.2f} successfully accomplished. Current balance: R${self.balance:.2f}")
        else:
            print("invalid deposit alor. The value must be greater than zero.")
 
    def __str__(self):
        return f"cont({self.number}, {self.holder}, balance: {self.balance:.2f})"

class BussinesAccount(Account):
    def __init__(self,number: int,holder: str,balance: float, loanLimit: float):
        super().__init__(number, holder, balance)
        self.loanLimit = loanLimit

    def loan(self, amount:float):
        if amount > 0 and amount <= self.loanLimit:
            self.balance += amount
            self.loanLimit -= self.loanLimit
        else:
            print("invalid deposit alo")

    def __str__(self):
       return f"cont({self.number}, {self.holder}, balance: {self.balance:.2f}), loanLimit: {self.loanLimit:.2f}"
    
acc = Account(123,"hugo",3.50)
print(f"primeiro print: {acc}")
acc.deposito(5.50)
print(f'segundo print:{acc}')
acc.withdraw(1.50)

b_acc = BussinesAccount(321," padaria", 500.0, 2000.0)
print(f"1 bc: {b_acc}")
b_acc.loan(2000.0)
print(f'2 BC: {b_acc}')