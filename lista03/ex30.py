class Carro:
    def __init__(self, marca, combustivel):
        
        self.marca = marca
        self.combustivel = combustivel

    def abastecer(self, quantidade):
        
        if quantidade > 0:
            self.combustivel += quantidade
            print("Abastecendo... Novo nível de combustível: " + str(self.combustivel))
        else:
            print("Quantidade inválida para abastecimento. A quantidade deve ser positiva.")

    def verificar_combustivel(self):
       
        print("Nível de combustível: " + str(self.combustivel))

carro1 = Carro("Fusca", 50) 
carro1.verificar_combustivel() 
carro1.abastecer(20)  
 
