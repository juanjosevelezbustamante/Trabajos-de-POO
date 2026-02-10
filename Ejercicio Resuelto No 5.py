import math
# Definicion de variables
suma = 0
x = 20
y = 40

# Calculos
suma = suma + x

x = x + math.pow(y,2)
# En pyhton el operador potencias es **
suma = suma + (x / y)

# Impresion de resultados
print(f"El valor de x es : {x}")
print(f"El valor de y es {y}")
print(f"El valor de la suma es : {suma}")