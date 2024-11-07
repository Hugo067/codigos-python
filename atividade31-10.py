
salario = float(input("quanto é seu salario = "))
anosdeserv = float(input("voce trabalha a quantos anos? = "))
aumento1 = (salario*10)/100
aumento2 = (salario*20)/100
aumento3 = (salario*30)/100


if anosdeserv <=1 :
    print("seu salario é de = ",salario)
    print("a porcentagem de aumento é de 10%")
    print("seu aumento foi de = ",aumento1)
    print(salario+aumento1)

if anosdeserv ==2 and anosdeserv == 3:
    print("seu salario é de = ",salario)
    print("a porcentagem de aumento é de 20%")
    print("seu aumento foi de = ",aumento2)
    print(salario+aumento2)

elif anosdeserv >= 4 :
    print("seu salario é de = ",salario)
    print("a porcentagem de aumento é de 30%")
    print("seu aumento foi de = ",aumento3)
    print(salario+aumento3)

