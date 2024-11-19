
# def esta_ordenada(lista):
#     return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


# entrada = input("Digite os números da lista separados por espaço: ")


# lista = list(map(int, entrada.split()))


# print(esta_ordenada(lista))

def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False  
    return True  

lista = [1, 2, 3, 4, 5]
resultado = esta_ordenada(lista)
print("A lista está ordenada em ordem crescente? {resultado}")