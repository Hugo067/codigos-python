class Jogo:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

    def iniciar_jogo(self):
        print("Iniciando o jogo " + self.nome + "...")

    def registrar_pontuacao(self, pontos):
        if pontos >= 0:
            self.pontuacao += pontos
            print("Pontuação registrada: " + str(pontos))
        else:
            print("Erro: Não é possível registrar pontos negativos.")

    def exibir_pontuacao(self):
        print("Pontuação atual: " + str(self.pontuacao))

jogo = Jogo("Super Mario")

jogo.iniciar_jogo()
jogo.registrar_pontuacao(100)  

