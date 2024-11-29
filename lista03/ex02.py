
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
    
        return self.largura * self.altura

retan = Retangulo(5, 10)

area = retan.area()
print(f" área do retângulo: {area}")