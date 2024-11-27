class contabancaria():


    def __init__(self,nome,saldo,cpf,senha):
        self.nome = nome
        self.__saldo = saldo
        self.__cpf = cpf
        self.__senha = senha
    def extrato(self,senha):
        if senha==self.__senha:     
            return f"saldo atual {self.__senha}"
        else:
         print("senha invalida")

    def depositar(self,valor):
        if valor>0:
            self.__saldo+=valor
    