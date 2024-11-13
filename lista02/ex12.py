
vetor1 = list(map(int, input("Digite os valores 1 separados por espaço: ").split()))
vetor2 = list(map(int, input("Digite os valores 2 separados por espaço: ").split()))

lista = vetor1 + vetor2
def separa_pares_impares(lista):
    pares = [x for x in lista if x % 2 == 0]
    impares = [x for x in lista if x % 2 != 0]
    return pares, impares

pares, impares = separa_pares_impares(lista)
print("Pares:", pares)
print("Impares:", impares)