# bi1 = float(input("escreva qual sua nota do primeiro 1 bimestre = "))
# bi2 = float(input("escreva qual sua nota do primeiro 2 bimestre = "))
 
# bi3 = (bi1+bi2)/2
# print("sua media é =",bi3)



# if bi3 == 10:
#     print("aprovado com distinção")
# elif  bi3 >= 7:
#     print("aprovado")
# else:    
#     print("reprovado")


#--- - - - --------------------------------------------------------------


# salario = float(input("quanto é seu salario = "))
# aumento1 = (salario*20)/100
# aumento2 = (salario*15)/100
# aumento3 = (salario*10)/100
# aumento4 = (salario*5)/100

# if salario <= 280:
#     print("seu salario é de = ",salario)
#     print("a porcentagem de aumento é de 20%")
#     print("seu aumento foi de = ",aumento1)
#     print(salario+aumento1)

# elif salario > 280 and salario < 700:
#     print("seu salario é de = ",salario)
#     print("a porcentagem de aumento é de 15%")
#     print("seu aumento foi de = ",aumento2)
#     print(salario+aumento2)

# elif salario > 700 and salario < 1500:
#     print("seu salario é de = ",salario)
#     print("a porcentagem de aumento é de 10%")
#     print("seu aumento foi de = ",aumento3)
#     print(salario+aumento3)

# elif salario >= 1500:
#     print("seu salario é de = ",salario)
#     print("a porcentagem de aumento é de 5%")
#     print("seu aumento foi de = ",aumento4)
#     print(salario+aumento4)

#  - - - - - - - - - - - - - - - - - - - - - - - - --- -  - -  -- - - - - - - - - 
nota1 = float(input("escreva qual sua nota do primeiro 1 bimestre = "))
nota2 = float(input("escreva qual sua nota do primeiro 2 bimestre = "))
nota3 = float(input("escreva qual sua nota do primeiro 3 bimestre = "))
nota4 = float(input("escreva qual sua nota do primeiro 4 bimestre = "))

media = (nota1+nota2+nota3+nota4)/4

if media == 9.1 and media <= 10.0:
    print ("sua media é A \nAPROVADO")
elif media == 7.6 and media <= 9.0:
    print("sua media é B \nAPROVADO")
elif media == 6.0 and media <= 7.5:
    print("sua media é C \nAPROVADO")
elif media == 4.1 and media <= 5.9:
    print("sua media é D \nREPROVADO")
elif media == 4.0 and media <= 0.0:
    print("sua media é E \nREPROVADO")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

a = input("telefonou para a vítima")
b = input("esteve no local do crime")
c = input("mora perto da vitima")
d = input("devia para a vitima")
e = input("ja trabalhou com vitima")

count=0
if a == "sim":
    count = +1
if b == "sim":
    count = +1
if c == "sim":
    count = +1
if d == "sim":
    count = +1
if e == "sim":
    count = +1

if count == 5:
    print("assassino")
elif count==4 or count==3:
    print("cumplice")
elif count==2:
    print("cumplice")
elif count==1 or count==0:
    print("cumplice")