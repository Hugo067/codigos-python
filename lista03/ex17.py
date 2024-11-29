class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatar_data(self):
       
        return f"{str(self.dia).zfill(2)}/{str(self.mes).zfill(2)}/{self.ano}"

data = Data(29, 11, 2024)

print("Data formatada: " + data.formatar_data())
