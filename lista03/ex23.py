class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_aumento(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f"Aumento de R${aumento:.2f} aplicado.")
        print(f"Novo salário de {self.nome}: R${self.salario:.2f}")

funcionario = Funcionario("Carlos", 3000)
funcionario.calcular_aumento(10)
