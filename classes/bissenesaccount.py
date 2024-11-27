from classaccount import Account



class BussinesAccount(Account):
    def __init__(self,number: int,holder: str,balance: float, loanLimit):
        super().__init__(number, holder, balance)
        self.loanLimit = loanLimit

    def loan(self, amount:float):
        if amount > 0 and amount <= self.loanLimit:
            self.balance += amount
        else:
            print("invalid deposit alo")

# holder= str(input('Name of the holder: '))
# print("name holder ",holder)
# amount = int(input("Enter the amount you want to deposit: "))
# print("Amount deposited",amount)
