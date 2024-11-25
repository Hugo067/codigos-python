class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
troca_cor = Bola ("azul","68 centimetros","couro sintético")
print(troca_cor.cor)
print(troca_cor.material)
print(troca_cor.circunferencia)


troca = str(input("digite sim para trocar a cor da bola = "))

if troca == "sim":
    mostra_cor = Bola ("vermelho","68 centimetros", "couro sintético")
    print(mostra_cor.cor)
    print(mostra_cor.material)
    print(mostra_cor.circunferencia)

else:
    print("erro")