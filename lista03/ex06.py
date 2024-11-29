class Animal:
    def __init__(self, especie, som):
        self.especie = especie
        self.som = som

    def emitir_som(self):
        print(f"O {self.especie} faz: {self.som}")

if __name__ == "__main__":
  
    cachorro = Animal("Cachorro", "Au au")
    gato = Animal("Gato", "Miau Miau")
    
    
    cachorro.emitir_som()
    gato.emitir_som()
