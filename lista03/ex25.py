class Pessoa:
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso

    def calcular_imc(self):
        if self.altura <= 0 or self.peso <= 0:
            raise ValueError("A altura e o peso devem ser valores positivos.")
        imc = self.peso / (self.altura ** 2)
        return round(imc, 2)

    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"


pessoa = Pessoa(1.85, 80)

imc = pessoa.calcular_imc()
classificacao = pessoa.classificar_imc()

print(f"O IMC da pessoa é: {imc}")
print(f"Classificação: {classificacao}")
