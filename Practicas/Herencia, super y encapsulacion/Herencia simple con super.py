# Crea una clase Empleado con:
# Atributos: nombre y salario
# Método info() que imprima los datos
# Luego crea una clase Programador que:
# Herede de Empleado
# Añada atributo lenguaje (por ejemplo: "Python")
# Sobrescriba info() para mostrar también el lenguaje
# Use super() para no repetir código

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def info(self):
        print(f"Nombre: {self.nombre}, Salario: {self.salario}")

class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def info(self):
        super().info()
        print(f"Lenguaje: {self.lenguaje}")
