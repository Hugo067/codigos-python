class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def verificar_altura(self):
        if self.altura > 1.75:
            print(f"{self.nome} é mais alta que 1,75 m.")
        else:
            print(f"{self.nome} não é mais alta que 1,75 m.")


pessoa = Pessoa("Henrique", 1.88)
pessoa.verificar_altura()


nome = input("Digite seu nome: ")
while True:
    try:
        altura = float(input("Digite sua altura em metros (ex: 1.80): "))
        if altura <= 0:
            print("Por favor, insira uma altura válida (número positivo).")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido para a altura.")

pessoa = Pessoa(nome, altura)
pessoa.verificar_altura()
