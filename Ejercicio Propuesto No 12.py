class Nomina:
    def calcular_salario_bruto(horas_trabajadas, valor_hora):
        return horas_trabajadas * valor_hora
    
    def calcular_valor_retefuente(porcentaje_retefuente, salario_bruto):
        return porcentaje_retefuente * salario_bruto
    
    def calcular_salario_neto(salario_bruto, valor_retefuente):
        return salario_bruto - valor_retefuente
    
# Definicion de variables
horas_trabajadas = 48.0 
valor_hora = 5000.0
retencion = 12.5
porcentaje_retefuente = retencion / 100

# Calculos usando la clase Nomina
salario_bruto = Nomina.calcular_salario_bruto(horas_trabajadas, valor_hora)
valor_retefuente = Nomina.calcular_valor_retefuente(porcentaje_retefuente, salario_bruto)
salario_neto = Nomina.calcular_salario_neto(salario_bruto, valor_retefuente)

# Impresion de resultados
print (f"Salario Bruto : {salario_bruto}")
print (f"Retencion en la fuente:{valor_retefuente}")
print(f"Salario Neto : {salario_neto}")
    