
a = int(input("Insira o 1º valor: "))
b = int(input("Insira o 2º valor: "))
c = int(input("Insira o 3º valor: "))

i = int(input("Insira o inicio: "))
f = int(input("Insira o fim: "))

lista = [a, b, c]
inicio, fim = i , f

def conta_intervalo(lista, inicio, fim):
    return sum(1 for x in lista if inicio <= x <= fim)

print(conta_intervalo(lista, inicio, fim)) 