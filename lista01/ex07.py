def conta_vogais(texto):
    return sum (1 for letra in texto if letra.lower() in "aeiouáéíóú")
texto = input("dgt uma frase:")
print(conta_vogais(texto)) 