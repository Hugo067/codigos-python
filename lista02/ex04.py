

a=int(input("Digite o valor 01: "))
b=int(input("Digite o valor 02: "))
c=int(input("Digite o valor 03: "))
d=int(input("Digite o valor 04: "))

lista1 = [a, b, c]
lista2 = [d, c, b]

def concatena_listas(lista1, lista2):
    return lista1 + lista2

print(concatena_listas(lista1, lista2))  