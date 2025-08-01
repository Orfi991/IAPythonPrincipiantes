# Convierte de Programación estructurada a POO
# Transforma este código en un conjunto de clases 
# (Triangulo y Rectángulo) que tengan métodos para calcular su área.

class FiguraGeometrica:
    """Clase base para figuras geométricas"""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Triangulo(FiguraGeometrica):
    """Clase que representa un triángulo"""
    def calcular_area(self):
        return (self.base * self.altura) / 2

class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo"""
    def calcular_area(self):
        return self.base * self.altura

# Crear instancias de las figuras
triangulo = Triangulo(5, 8)
rectangulo = Rectangulo(6, 4)

# Calcular y mostrar áreas
print(f"Área del triángulo: {triangulo.calcular_area()}")
print(f"Área del rectángulo: {rectangulo.calcular_area()}")