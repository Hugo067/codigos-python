class Quadrado:
    def __init__(self,lado):
       self.lado = lado
    def mostrar_area (self):
        print(self.lado*self.lado)

    def mudar_valor_lado(self,novo_lado):
        self.lado=novo_lado
        print(self.lado*self.lado)

quadrado =Quadrado(6)

quadrado.mostrar_area()
quadrado.mudar_valor_lado(10)
