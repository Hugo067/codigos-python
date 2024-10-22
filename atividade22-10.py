a = float(input("digite a populaçao a =  "))
c = float(input("digite a taxa de crescimento da populaçao a = "))
b = float(input("digite a populaçao b =  "))
d = float(input("digite a taxa de crescimento da populaçao b = "))

cont = 0
while True :
    if a<=b:
        a=a+(a*c/100)
        b=b+(b*d/100)
        cont=cont+1
        print(cont)
    break
