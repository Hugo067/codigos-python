class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self, outra_pessoa, saudacao="Olá"):
        print(f"{saudacao}, {outra_pessoa.nome}!")

pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")

pessoa1.cumprimentar(pessoa2)
pessoa2.cumprimentar(pessoa1)