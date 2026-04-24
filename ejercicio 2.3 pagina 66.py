from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = 1; BIOETANOL = 2; DIESEL = 3; BIODIESEL = 4; GAS_NATURAL = 5

class TipoAutomovil(Enum):
    CIUDAD = 1; SUBCOMPACTO = 2; COMPACTO = 3; FAMILIAR = 4; EJECUTIVO = 5; SUV = 6

class TipoColor(Enum):
    BLANCO = 1; NEGRO = 2; ROJO = 3; NARANJA = 4; AMARILLO = 5; VERDE = 6; AZUL = 7; VIOLETA = 8

class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, 
                 num_puertas, cant_asientos, vel_maxima, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.num_puertas = num_puertas
        self.cant_asientos = cant_asientos
        self.vel_maxima = vel_maxima
        self.color = color
        self.vel_actual = 0

    def acelerar(self, incremento):
        if self.vel_actual + incremento <= self.vel_maxima:
            self.vel_actual += incremento
        else:
            print("¡ERROR! No se puede superar la velocidad máxima.")

    def desacelerar(self, decremento):
        if self.vel_actual - decremento >= 0:
            self.vel_actual -= decremento
        else:
            print("¡ERROR! No se puede tener velocidad negativa.")

    def frenar(self):
        self.vel_actual = 0

    def imprimir(self):
        print("\n--- DATOS DEL AUTOMÓVIL ---")
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Motor: {self.motor}L")
        print(f"Combustible: {self.tipo_combustible.name} | Tipo: {self.tipo_automovil.name}")
        print(f"Velocidad Actual: {self.vel_actual} km/h")

# LECTURA DE DATOS
if __name__ == "__main__":
    print("Ingrese la Marca del vehículo:")
    marca = input()

    print("Ingrese el Modelo (año):")
    modelo = int(input())

    print("Ingrese el Motor (litros):")
    motor = float(input())

    # Para los Enums, pedimos un número para facilitar la entrada
    print("Seleccione Combustible (1:Gasolina, 2:Bioetanol, 3:Diesel, 4:Biodiesel, 5:Gas Natural):")
    op_comb = int(input())
    tipo_comb = TipoCombustible(op_comb)

    print("Seleccione Tipo (1:Ciudad, 2:Subcompacto, 3:Compacto, 4:Familiar, 5:Ejecutivo, 6:SUV):")
    op_tipo = int(input())
    tipo_auto = TipoAutomovil(op_tipo)

    print("Ingrese número de puertas:")
    puertas = int(input())

    print("Ingrese cantidad de asientos:")
    asientos = int(input())

    print("Ingrese velocidad máxima:")
    vel_max = int(input())

    print("Seleccione Color (1:Blanco, 2:Negro, 3:Rojo, 4:Naranja, 5:Amarillo, 6:Verde, 7:Azul, 8:Violeta):")
    op_col = int(input())
    color_auto = TipoColor(op_col)

    # Crear el objeto con los datos capturados
    auto1 = Automovil(marca, modelo, motor, tipo_comb, tipo_auto, puertas, asientos, vel_max, color_auto)

    # Ejecución de la lógica solicitada 
    print("\n--- INICIANDO PRUEBAS ---")
    auto1.vel_actual = 100
    print(f"Velocidad inicial establecida en: {auto1.vel_actual} km/h")

    auto1.acelerar(20)
    print(f"Velocidad después de acelerar 20: {auto1.vel_actual} km/h")

    auto1.desacelerar(50)
    print(f"Velocidad después de desacelerar 50: {auto1.vel_actual} km/h")

    auto1.frenar()
    print(f"Velocidad después de frenar: {auto1.vel_actual} km/h")