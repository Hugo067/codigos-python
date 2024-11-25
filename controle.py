class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura, quarto):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        self.quarto = quarto
 
    def mudar_canal(self, botao):
        if botao == "+":
            print("aumentar canal")
        elif botao == "-":
            print("diminuir canal")
        else:
            print("Valor Inválido")
 
# Instâncias dos controles remotos
controle_remoto1 = ControleRemoto('vermelho', 10, 5, 2, 'Quarto')
controle_remoto2 = ControleRemoto('azul', 10, 5, 2, 'Cozinha')
 
# Métodos de mudar canal específicos para cada instância
def mudar_canal_quarto(botao):
    if botao == "NetFlix":
        print("abrir NetFlix")
    elif botao == "Power":
        print("desligar TV")
    else:
        print("Valor Inválido")
 
def mudar_canal_cozinha(botao):
    if botao == "CH":
        print("mudar canal")
    elif botao == "Mute":
        print("som desligado")
    else:
        print("Valor Inválido")
 
print(f"O controle remoto do {controle_remoto1.quarto} é de cor {controle_remoto1.cor}.")
mudar_canal_quarto("NetFlix")
 
print(f"O controle remoto da {controle_remoto2.quarto} é de cor {controle_remoto2.cor}.")
mudar_canal_cozinha("CH")

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


