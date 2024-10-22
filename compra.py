while True:
    total=0
    while True:

        num = float(input("digite o valor da mercadoria = "))


        total = total + num
        
        if num == 0.0:
            break
        produto = str(input("digite o nome do  produto ="))
        print(produto,":",num)

    print(total)
    while True:

        dinheiro = float(input("digite a quantidade de dinheiro = "))
        if dinheiro >= total:
                troco = dinheiro - total
                print("seu troco é de  = ",troco)
                break
        else:
                print("valor insuficiente")
                        




    # if dinheiro < total:
    #     print("")