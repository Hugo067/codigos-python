class Temperatura:
    def celsius_para_fahrenheit(self, celsius):
       
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit


temperatura = Temperatura()

try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    
    fahrenheit = temperatura.celsius_para_fahrenheit(celsius)
    
    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f}")
    
except ValueError:
    print("Por favor, digite um valor numérico válido para a temperatura.")
