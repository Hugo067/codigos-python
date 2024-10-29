# time = ['1-palmeiros','2-curitiba','3-sao paulo']
# for n in time:
#     print(n)

#-------------------------------------------------------------
# soma=0
# x = int(input('first number = '))
# y = int(input('second number = '))
# for i in range(x,y+1):
#     print(i)
#     soma=soma+i
# print(soma) 
#---------------------------------------------------------------
# for i in range(1,21):
#     print(i, end= " ")
#----------------------------------------------------------------
# cont=0
# soma=0
# for x in range(5):
#     n1= int(input("digite um numero = "))
#     soma= soma+n1
#     cont=cont+1
# print(soma)

# media=soma/cont
# print(media)
#---------------------------------------------------------------
size = 15
num3 = 0
num2 = 1
num1 = 1
for i in range(0,size):
    if(i == 0 or i== 1):
        print(1)
    else:
        num3 = num1 + num2
        num1 = num2
        num2 = num3

        print(num3)
