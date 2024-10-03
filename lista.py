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

b = [1, 2, 1, 5, 6, 4, 3, 1]

# uma maneira de excluir

uma_lista1 = ["a", "b", "c", "d", "e", "f"]
print(uma_lista1)
print(len(uma_lista1))

uma_lista1[1:3] = []
print(uma_lista1)
print(len(uma_lista1))

#adicionar
uma_lista2 = ["a", "b", "f"]
uma_lista2[1:1] = ["b", "c"]
print(uma_lista2)
uma_lista2[4:4] = ["e"]
print(uma_lista2)

#deletar

c = ["um", "dois", "três"]
del c[1]
print(c)

lista = ["a", "b", "c", "d", "e", "f"]
del lista [1:5]
print(lista)

#inserir elemento
d = [81, 82, 83]
d.append(5)
print (d)

#ordenar crescente
e = [88, 81, 82, 90]
e.sort()
print (e)

#ordenar decrescente

e = [88, 81, 82, 90]
e.sort(reverse = True)
print (e)

#indice do elemento que eu quero

f =[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f.index (4))

#inserir na posiçao que eu quero

g = [81, 82, 88, 90]
g.insert(0,100)
print(g)

#quantas vezes o elemento aparece
h = [82, 88, 88, 88, 84, 88, 88, 88, 88, 88, 88, 88, 80]
print(h)
print(h.count(88))

#excluir o elemento que eu quero
i = [82, 88, 88, 88, 84, 88, 88, 88, 88, 88, 88, 88, 80]
i.pop()
print(i)

i.pop(0)
print(i)

#extand ele unifica a lista

j = [1,2,3]
j.extend([4,5])
print(j)


frutas2 = ["maca", "laranja", "banana", "cereja", "uva"]
print(frutas2)
frutas2 [1] = "goiaba"
print(frutas2)
