# a = 10

# while a<100:
#     print("l")
# print("fim")

#--------------------------------------------------------------

# while True:
#     valor = int(input("digite 1 ou 0 para o fim = "))
#     if valor >= 1:
#         continue
#         print("valor correto")
#     if valor >= 1:
#         print("maior que um ")

# --------------------------------------------------------------
# valor = int(input("digite um numero  = "))
# cont = 0
# while valor >=0:
#     print(valor)
#     cont = cont +1
#     valor = valor - 1
# print(cont)
#----------------------------------------------------------------
# i = 0
# while i==0:
#     opçao = int(input("escolha umas das opçao:\n1-mult\n2-divisao\n3-adiçao\n4-sub\n5-sair\n"))
#     if opçao==1:
#         a1=float(input("digite o primeiro valor = "))
#         a2=float(input("digite o segundo valor = "))
#         a3=a1*a2
#         print("o resultado é = ",a3)
#     elif opçao==2:
#         a1=float(input("digite o primeiro valor = "))
#         a2=float(input("digite o segundo valor = "))
#         a3=a1/a2
#         print("o resultado é = ",a3)
#     elif opçao==3:
#         a1=float(input("digite o primeiro valor = "))
#         a2=float(input("digite o segundo valor = "))
#         a3=a1+a2
#         print("o resultado é = ",a3)
#     elif opçao==4:
#         a1=float(input("digite o primeiro valor = "))
#         a2=float(input("digite o segundo valor = "))
#         a3=a1-a2
#         print("o resultado é = ",a3)
#     elif opçao==5:
#         print("saindo")
#         i=1
#     else:
#         print("opçao invalida")

#--------------------------------------------------------------------
# while True :
#     a =int(input("dgt um numero entre 0 a 10 = "))

#     if a >=0 and a <= 10:
#         print("valor valido")
#         break
#     else:
#         print("numero invalido")

#---------------------------------------------------------------------
while True:
    name = str(input("digite seu nome = "))
    if len(name) >3:
        print(name)
        print("nome valido") 
        break
    else:
        print("nome invalido")
while True:  
    idade = int(input("dgt sua idade = "))
    if idade > 0 and idade < 151:
        print(idade)
        print("idade valido")
        break
    else:
        print("idade invalido")
while True:  
    salario =int(input("dgt seu salario = "))
    if salario > 0:
        print(salario)
        print("salario valido")
        break
    else:
        print("salario invalido")
while True:  
    sexo = str(input("digite seu sexo = "))
    if sexo == "f":
        print("feminino")
        print("sexo valido")
    if sexo == "m":
        print("maculino")
        print("sexo valido")
    if sexo == "o":
        print("sexo outro")
        print("sexo valido")
        break
    else:
        print("sexo invalido")
while True:  
    estadocivil = str(input("digite seu estado civil = "))
    if estadocivil == "s":
        print("solteiro")
        print("estado civil valido ")
    elif estadocivil == "c":
        print("casado")
        print("estado civil valido ")
    elif estadocivil == "v":
        print("viuvo")
        print("estado civil valido ")
    elif estadocivil == "d":
        print("divorciado")
        print("estado civil valido ")
        break
    else:
        print("estado civil invalido")