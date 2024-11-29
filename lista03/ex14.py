class Eletrodomestico:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia

    def ligar(self):
       
        print(f"O {self.nome} de {self.potencia}W foi ligado.")


eletro = Eletrodomestico("Liquidificador", 500)

eletro.ligar()
