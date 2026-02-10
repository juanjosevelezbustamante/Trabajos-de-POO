import math

class Calculos :
    def calcular_longitud_circunferencia(radio):
        return 2 * math.pi * radio
    
    def calcular_area_cirulo(radio):
        return math.pi * math.pow(radio,2)
    
radio = 3.0

# Lamamos a los metodos estáticos
longitud_circunferencia = Calculos.calcular_longitud_circunferencia(radio)
area_circulo = Calculos.calcular_area_cirulo(radio)

# Imprimimos Resultados
print(f"Longitud_circunferencia: ", longitud_circunferencia)
print(f"Área Circulo: ", area_circulo)



  