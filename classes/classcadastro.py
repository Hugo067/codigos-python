from classpessoaj import *

while True:
    tipo = int(input("1 - PF\n2 - PJ\nqual deseja: "))

    if tipo == 1:
        instancia = PFF()
        instancia.PF()
    
    elif tipo == 2:
        instancia = PJL()
        instancia.PJ()
   

