
a = input("Insira a 1ª string: ")
b = input("Insira a 2ª string: ")
c = input("Insira a 3ª string: ")

# Criando a lista de strings
lista_strings = [a, b, c]

# Função para concatenar strings
def concatena_strings(lista_strings):
    return ''.join(lista_strings)

# Concatenando e imprimindo as strings
print(concatena_strings(lista_strings))