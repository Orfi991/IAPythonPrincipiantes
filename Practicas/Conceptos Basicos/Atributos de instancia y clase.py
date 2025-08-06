class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Coche: {self.marca} {self.modelo}"
        
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Focus")

print(coche1.descripcion())
print(coche2.descripcion())