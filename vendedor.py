class Vendedor():
    def __init__(self,nome,vendas):
        self.nome = nome
        self.vendas = vendas
    def vendeu(self, vendas):
        self.vendas= vendas 
        print(self.vendas)
    def bateu_meta(self, meta):
        if self.vendas > meta:
            print("bateu meta")
        













        #quando estamos criando uma classe, a primeira coisa é definir uma função "__init__"
        