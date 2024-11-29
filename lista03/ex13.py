class Veiculo:
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade

    def aumentar_velocidade(self, aumento):
        self.velocidade += aumento
        # Usando f-strings para melhorar a legibilidade
        print(f"Velocidade aumentada em {aumento} km/h.")
        print(f"Velocidade atual: {self.velocidade} km/h.")

veiculo = Veiculo("jetta",90)

# Usando f-strings também na exibição da velocidade inicial
print(f"Velocidade inicial: {veiculo.velocidade} km/h")
veiculo.aumentar_velocidade(20)
