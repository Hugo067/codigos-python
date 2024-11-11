#se = if   elif continuação de if    else: caso o teste de cima dele seja falso

num1 = float(input("digite um numero para sua divição = "))
num2 = float(input("digite outro numero para sua divição = "))


if num1 == 0:
    print("erro")
elif num2 == 0:
    print("erro")

else:
     n1 = (num1/num2)
     print(n1)

#else  sempre ira usar if da msm linha 
idade = int(input("digite sua idade: "))
if idade ==16:
    print("pode votar")
else:
    if idade>=18:
        print("pode dirigir")
    else:
        if idade <16:
            print ("apenas estude")

#(senao se) elif

            