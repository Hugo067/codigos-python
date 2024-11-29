
class Pessoa:
    def __init__(self,nome,idade ):
        self.nome = nome
        self.idade =idade 

    def print_info(self):

        print(f"Nome: {self.nome}\nIdade: {self.idade} anos")
        
pes = Pessoa("Hugo", 18)

pes.print_info()
