#lista 

lista1 = ["hugo", "spam", "bungee", "swallow"]
lista2 = [37, 1.75, 78.80]
print (lista1, lista2)

#sub lista 
lista3 = ["oi", 2.0, 5, [10, 20]]
print(lista3)

#len
lista4 = ["oi", 2.0, 5, [10, 20]]
print(len(lista4))

#vai seguir essa ordem 0,1,2,3 (-4,-3,-2,-1)
numeros = [17, 123, 87, 34, 66, 8398, 44]
print(numeros[2])
print(numeros[9-8])
print(numeros[-2])
print(numeros[-1])

#true false
frutas = ["maca", "laranja", "banana", "cereja"]

print("maca" in frutas)
print("pera" in frutas)

#
frutas1 = ["maca", "laranja", "banana", "cereja"]
print([1, 2] + [3,4])
print(frutas1 + [6, 7, 8, 9])

print(["teste"] * 4)
print ([1, 2, ["ola", "adeus"]]*2)

#
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(max(a))
print(min(a))
print(sum(a))

#fatiar 0=a 1=b 2=c 3=d 4=e 5=f

uma_lista = ["a", "b", "c", "d", "e", "f"]
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])
print(uma_lista[0:6])