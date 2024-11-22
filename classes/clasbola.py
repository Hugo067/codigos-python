class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
troca_cor = Bola ("azul","10x10","latex")
print(troca_cor.material)

mostra_cor = Bola ("vermelho","20x20", "latex")
print(mostra_cor.material)