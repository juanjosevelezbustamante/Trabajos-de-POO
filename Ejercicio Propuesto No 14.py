import math

class Calculos:
    def calcular_cuadrado(numero):
        return math.pow(numero, 2)
    
    def calcular_cubo(numero):
        return math.pow(numero, 3)
    
numero = 4.0

# Llamada a la clase calculos
cuadrado = Calculos.calcular_cuadrado(numero)
cubo = Calculos.calcular_cubo(numero)

print("Cuadrado:" , cuadrado)
print("Cubo:", cubo)


    



    