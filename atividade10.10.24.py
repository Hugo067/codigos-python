senha = int(input("digite sua senha = "))

extrato = 0
adm= 4

if senha == 1234:
    print("\n1.EXTRATO",
          "\n2.DEPOSITO",
          "\n3.SAQUE",
          "\n4.ADM",
          "\n5.SAIR")

  

    opção1= int(input("escolha sua opção = "))

    if opção1 == 1:
        print("seu saldo bancario = ", extrato)


    elif opção1 == 2:
        deposito = float(input("digite o falor que vai depositar = "))
        extrato=deposito+extrato
        print("seu saldo bancario = ", extrato)
        print("o valor depositado foi = ", deposito)


    elif opção1 == 3:
        saque = float(input("digite o valor que deseja sacar = ", ))
        extrato=saque-extrato
        print("seu saldo bancario = ", extrato)
        print("o valor desejado para saque foi = ",saque)




        if opção1 == 4:
            print("1.\ncadastro")
                  
            adm = int(input("digite a opção = "))
            
        elif adm ==1:
            nome = str(input("digite seu nome = "))
            cpf = int(input("digite seu cpf = "))
            fone = int(input("digite seu fone = "))
            sexo = str(input("digite seu sexo = "))

#             if

#             elif adm ==2:
#                 print(nome)
#                 print(cpf)
#                 print(fone)
#                 print(sexo)


#     elif opção1 == 5:
#         sair = str(input("saida bem sucedida..."))

# else: 
#     print("senha invalida")
    