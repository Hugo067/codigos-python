n = int(input("Digite um nº para calcular o fatorial: "))
fatorial =1
for i in range(1, n + 1):
    fatorial *= i
    print("O resultado fatorial de n é:", fatorial)
    