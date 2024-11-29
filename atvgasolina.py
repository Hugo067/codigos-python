class Vehicle:
    def __init__(self, mark: str, model: str):
        self.mark = mark
        self.model = model

    def Info(self):
        pass  # Método genérico de informação pode ser sobrescrito pelas subclasses


class Car(Vehicle):
    def __init__(self, mark: str, model: str):
        super().__init__(mark, model)

    def Type_Fuel(self, fuel: str):
        if fuel == 'Gasoline':
            print(f'Added {fuel}')
        else:
            print("This car only accepts Gasoline.")

    def Capacity_Passengers(self, passengers: int):
        if passengers > 5:
            print("This car can't support more than 5 passengers!")
        elif passengers <= 0:
            print("Invalid number of passengers!")
        else:
            print(f'Will board {passengers} passengers.')

    def Info(self):
        print(f'This car is a {self.mark} {self.model}, and only accepts Gasoline fuel, supporting a maximum of 5 passengers.')


class MotorBike(Vehicle):
    def __init__(self, mark: str, model: str):
        super().__init__(mark, model)

    def Type_Fuel(self, fuel: str):
        if fuel == 'Gasoline':
            print(f'Added {fuel}')
        else:
            print("This motorbike only accepts Gasoline.")

    def Capacity_Passengers(self, passengers: int):
        if passengers > 2:
            print("This motorbike can't support more than 2 passengers!")
        elif passengers <= 0:
            print("Invalid number of passengers!")
        else:
            print(f'Will board {passengers} passengers.')

    def Info(self):
        print(f'This motorbike is a {self.mark} {self.model}, and only accepts Gasoline fuel, supporting a maximum of 2 passengers.')


class Truck(Vehicle):
    def __init__(self, mark: str, model: str):
        super().__init__(mark, model)

    def Type_Fuel(self, fuel: str):
        if fuel == 'Diesel':
            print(f'Added {fuel}')
        else:
            print("This truck only accepts Diesel.")

    def Capacity_Passengers(self, passengers: int):
        if passengers > 2:
            print("This truck can't support more than 2 passengers!")
        elif passengers <= 0:
            print("Invalid number of passengers!")
        else:
            print(f'Will board {passengers} passengers.')

    def Info(self):
        print(f'This truck is a {self.mark} {self.model}, and only accepts Diesel fuel, supporting a maximum of 2 passengers.')


fiatmobi = Car('fiat', 'mobi')
fiatmobi.Info()
fiatmobi.Type_Fuel('Gasoline')
fiatmobi.Capacity_Passengers(4)

start160 = MotorBike('160 ', 'start')
start160.Info()
start160.Type_Fuel('Gasoline')
start160.Capacity_Passengers(2)

caminhao =Truck('carreta','furacao')
caminhao.Info
caminhao.Type_Fuel('diesel')
caminhao.Capacity_Passengers(2)
