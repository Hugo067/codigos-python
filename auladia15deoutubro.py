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


salario = float(input("quanto é seu salario = "))
aumento1 = (salario*20)/100
aumento2 = (salario*15)/100
aumento3 = (salario*10)/100
aumento4 = (salario*5)/100

if salario <= 280:
    print("seu salario é de = ",salario)
    print("a porcentagem de aumento é de 20%")
    print("seu aumento foi de = ",aumento1)
    print(salario+aumento1)

elif salario > 280 and salario < 700:
    print("seu salario é de = ",salario)
    print("a porcentagem de aumento é de 15%")
    print("seu aumento foi de = ",aumento2)
    print(salario+aumento2)

elif salario > 700 and salario < 1500:
    print("seu salario é de = ",salario)
    print("a porcentagem de aumento é de 10%")
    print("seu aumento foi de = ",aumento3)
    print(salario+aumento3)

elif salario >= 1500:
    print("seu salario é de = ",salario)
    print("a porcentagem de aumento é de 5%")
    print("seu aumento foi de = ",aumento4)
    print(salario+aumento4)