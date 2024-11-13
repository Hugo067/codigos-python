
v1 = int(input("Digite o valor 1: "))
v2 = int(input("Digite o valor 2: "))
v3 = int(input("Digite o valor 3: "))
v4 = int(input("Digite o valor 4: "))
escalar=int(input("Digite o valor escalar: "))
 
lista = multiplica_escalar= [v1,v2,v3,v4]
escalar = escalar

def multiplica_escalar(lista,escalar):
    return [x*escalar for x in lista]
print(multiplica_escalar(lista,escalar))