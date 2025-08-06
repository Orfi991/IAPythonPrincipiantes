class Persona:
    nombre = "Orfilia"
    edad = 33

    def __init__(self, nombre, edad):
        nombre = nombre
        edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")