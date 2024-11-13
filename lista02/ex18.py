
peso = int(input("Qual o peso?: "))
valor = int(input("Qual o valor?: "))

# Criando as listas de valores e pesos
lista_valores = [valor]
lista_pesos = [peso]

# Função para calcular a média ponderada
def media_ponderada(lista_valores, lista_pesos):
    soma_ponderada = sum(valor * peso for valor, peso in zip(lista_valores, lista_pesos))
    soma_pesos = sum(lista_pesos)
    return soma_ponderada / soma_pesos

# Calculando e imprimindo a média ponderada
print(media_ponderada(lista_valores, lista_pesos))