class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

quadrado = Quadrado(5)

area = quadrado.calcular_area()
perimetro = quadrado.calcular_perimetro()


print(f"Área do quadrado: {area}")
print(f"Perímetro do quadrado: {perimetro}")
