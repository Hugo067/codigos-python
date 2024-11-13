
a=int(input("Digite o valor 01: "))
b=int(input("Digite o valor 02: "))
c=int(input("Digite o valor 03: "))
d=int(input("Digite o valor 04: "))

lista = [a, b, c, d]

def diferenca_elementos_lista(lista):
    return [abs(lista[i] - lista[i + 1]) for i in range(len(lista) - 1)]

print(diferenca_elementos_lista(lista)) 