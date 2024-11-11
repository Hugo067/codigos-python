texto = input("Digite um texto: ")
def conta_palavras(texto):
    palavras = texto.split()
    return len(palavras)

print(conta_palavras(texto))