# nascimento = int(input("digite o ano que vc nasceu: "))
# if nascimento < 2008:
#     print("pode votar")
# else:
#     if nascimento >= 2008:
#         print("voce nao pode votar")

#----------------------------------------------------
# num1 = float(input("digite sua senha = "))



# if num1 == 1234:
#     print("ACESSO PERMITIDO")

# else: 
#     print("ACESSO NEGADO")
#-----------------------------------------------------
 
# x = 0.30
# y = 0.25
# n1 = float(input("quantas maça vc quer compra?"))

# if n1 < 12:
#     print(n1*x)
# else:
#     if n1 >=12:
#         print(n1*y)
#-----------------------------------------------------
    
a = float(input("digite um numero ="))
b = float(input("digite um numero ="))
c = float(input("digite um numero ="))

if a<b and b<c:
        print(a,b,c)
elif a<c and c<b:
        print(a,c,b)
elif b<a and a<c:
        print(b,a,c)
elif b<c and c<a:
        print(b,c,a)
elif c<a and a<b:
        print(c,a,b)
elif c<b and b<a:
        print(c,b,a)



