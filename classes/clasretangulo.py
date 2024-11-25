class Retangulo:
    def __init__(self,lado1,lado2):
       self.lado1 = lado1
       self.lado2 = lado2
    
    def comprimento_dos_lados (self,lado1,lado2):
        self.lado1 = float(input("digite o lado A :"))
        self.lado2 = float(input("digite o lado B :"))
        return print (self.lado1, self.lado2)
    def area(self):
        return self.lado1*self.lado2
    def perimetro(self):
        return((self.lado1*2) + (self.lado2*2))
    
retangulo = Retangulo(0,0)
retangulo.comprimento_dos_lados(0,0)
print(retangulo.area())
print(retangulo.perimetro())
    