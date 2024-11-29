class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print('modelo:' ,self.modelo,'\nAno:', self.ano)

if __name__ == "__main__":
    carro = Carro("jetta", 2020)

    carro.exibir_informacoes()