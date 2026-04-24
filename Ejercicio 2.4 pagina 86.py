import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (2 * self.base) + (2 * self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.pow(self.base**2 + self.altura**2, 0.5)

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            print("Es un triángulo equilátero")
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")

# Bloque de captura de datos y ejecución 

def main():
    print("--- Cálculo de Figuras Geométricas ---")

    # Círculo
    r = float(input("Ingrese el radio del círculo: "))
    figura1 = Circulo(r)
    print(f"El área del círculo es = {figura1.calcular_area():.2f}")
    print(f"El perímetro del círculo es = {figura1.calcular_perimetro():.2f}\n")

    # Rectángulo
    b_rect = float(input("Ingrese la base del rectángulo: "))
    a_rect = float(input("Ingrese la altura del rectángulo: "))
    figura2 = Rectangulo(b_rect, a_rect)
    print(f"El área del rectángulo es = {figura2.calcular_area()}")
    print(f"El perímetro del rectángulo es = {figura2.calcular_perimetro()}\n")

    # Cuadrado
    l = float(input("Ingrese el lado del cuadrado: "))
    figura3 = Cuadrado(l)
    print(f"El área del cuadrado es = {figura3.calcular_area()}")
    print(f"El perímetro del cuadrado es = {figura3.calcular_perimetro()}\n")

    # Triángulo Rectángulo
    b_tri = float(input("Ingrese la base del triángulo: "))
    a_tri = float(input("Ingrese la altura del triángulo: "))
    figura4 = TrianguloRectangulo(b_tri, a_tri)
    print(f"El área del triángulo es = {figura4.calcular_area()}")
    print(f"El perímetro del triángulo es = {figura4.calcular_perimetro():.2f}")
    figura4.determinar_tipo_triangulo()

if __name__ == "__main__":
    main()