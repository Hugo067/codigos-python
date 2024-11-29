class Super:

    def hello(self):
        print("Olá, sou a superclasse!")

# teste = Super()
# teste.hello() 

class Sub(Super):
    def hello(self):
        print("olá, sou a subclasse!")

# teste = Sub()
# teste.hello()

class Subsub(Sub):
    def hello(self):
        print("olá, sou a subsubclasse!")

teste = Subsub()
teste.hello()