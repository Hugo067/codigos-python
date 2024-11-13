
a=int(input("Digite o valor 01: "))
b=int(input("Digite o valor 02: "))
c=int(input("Digite o valor 03: "))
d=int(input("Digite o valor 04: "))

lista = [a, b, c, d]
import math

def desvio_padrao(lista):
    media = sum(lista) / len(lista)
    variancia = sum((x - media) ** 2 for x in lista) / len(lista)
    return math.sqrt(variancia)

print(desvio_padrao(lista))