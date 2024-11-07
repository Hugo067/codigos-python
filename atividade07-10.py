#função

# def hello():
#     print("ola")
# hello()

#-------------------------------------------------------------------

# def helo(nome):
#     print("ola", nome)
# helo("pjl")

#---------------------------------------------------------------------

# def helo(nome1):
#     print("seja bem vindo", nome1)

# a = input("digite seu nome = ")
# helo (a)

#--------------------------------------------------------------------

# def hi(nome2, idade):
#     print("ola",nome2, "\nsua iadade é:", idade)

# c = input("digite seu nome =")
# b = input("digite sua idade =")
# hi(c,b)

#----------------------------------------------------------------------

# def calcular_pag(qts_hrs, valor_hrs):
#     print(qts_hrs, valor_hrs)

# a = float(input("digite as horas trabalhada = "))
# b= float(input("digite a taxa = "))
# calcular_pag(a,b)

# hrs= float(a)
# taxa= float(b)
# if hrs <=40:
#     salario=hrs*taxa
# else:
#     h_excd= hrs-40
#     salario = 40*taxa+(h_excd*(1.5*taxa))
# print(salario)

#----------------------------------------------------------------------
# def soma(x,y):
#     result = x+y
#     return result

# a = int(input("primeiro numero = "))
# b = int(input("segundo numero = "))

# res = soma (a,b) 
# print("soma", res)
#-----------------------------------------------------------------

# def inverte(nome, sobrenome):
#     nomeinverso = sobrenome+",",nome
#     return nomeinverso
# nome = input("nome: ")
# sobrenome = input("sobrenome: ")
# invertido = inverte(nome, sobrenome)
# print("ola", invertido)

#----------------------------

# def par(x):
#     if(x%2)==8:
#         return True
#     else:
#         return False

# while True:
#     num = int(input("insira um numero = "))
#     if par (num):
#         print("é par")
#     else:
#         print("é impar")
#------------------------------------------------------

# def cadastro():
#     name = input("qual seu nome: ")
#     age =  int(input("idade"))
#     return name,age

# print("iniciado cadastro....")
# nome,idade = cadastro()
# print("cadastro realizado com secesso: ")
# print("seu nome  é ", nome, "e vc tem", idade, "anos de idade.")
#--------------------------------------------------------------------

# def soma (x,y,z):
#     result = (x+y)*z
#     return result

# a = int(input(" 1 numero"))
# b = int(input(" 2 numero"))
# c = int(input(" 3 numero"))
# res = soma(a,b,c)
# print("resultado",res)
#------------------------------------------------------------------------

def neg(x):
    if x < 0:
        return True
    else:
        return False

while True:
    num = int(input("insira um numero = "))
    if neg (num):
        print("N")
    elif num==0:
        print("Zero")
    else:
        print("P")