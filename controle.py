class ControleRemoto:
    def __init__(self,cor,altura,profundidade,largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def mudar_canal (self,botao):
        if botao =="+":
            print("aumentar canal")
        elif botao =="-":
            print("diminuir canal")
        else:
            print("valor inválido")

class ControleRemoto:
    def __init__(self,cor,altura,profundidade,largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def mudar_canal (self,botao):
        if botao =="+":
            print("aumentar canal")
        elif botao =="-":
            print("diminuir canal")
        else:
            print("valor inválido")
    def aumentar_volume (self,botao):
        if botao =="vol+":
            print("volume aumentado")
        elif botao =="vol-":
            print("volume abaixado")
        else:
            print("valor inválido")
    def desligar_ligar(self,botao):
        if botao =="ligar":
            print("ligando")
        elif botao =="desligar":
            print("desligando")
        else:
            print("valor inválido")