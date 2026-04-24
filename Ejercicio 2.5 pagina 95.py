from enum import Enum

# Definimos el tipo de cuenta como un Enumerado
class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0  # El saldo inicial siempre es cero

    def imprimir(self):
        print("\n--- Datos de la Cuenta ---")
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Número de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta.value}")
        print(f"Saldo = ${self.saldo:.2f}")

    def consultar_saldo(self):
        print(f"El saldo actual es = ${self.saldo:.2f}")

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor}. El nuevo saldo es ${self.saldo:.2f}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor}. El nuevo saldo es ${self.saldo:.2f}")
            return True
        else:
            print("Error: El valor a retirar debe ser mayor a cero y no superar el saldo actual.")
            return False

# Bloque Central 

def main():
    print("--- Registro de Nueva Cuenta Bancaria ---")
    nombres = input("Ingrese nombres del titular: ")
    apellidos = input("Ingrese apellidos del titular: ")
    num_cuenta = int(input("Ingrese número de cuenta: "))
    
    print("Seleccione tipo de cuenta: 1. Ahorros, 2. Corriente")
    opcion_tipo = input("Opción: ")
    tipo = TipoCuenta.AHORROS if opcion_tipo == "1" else TipoCuenta.CORRIENTE

    # Creación del objeto
    mi_cuenta = CuentaBancaria(nombres, apellidos, num_cuenta, tipo)

    while True:
        print("\n--- Menú de Acciones ---")
        print("1. Ver datos de la cuenta")
        print("2. Consultar saldo")
        print("3. Consignar dinero")
        print("4. Retirar dinero")
        print("5. Salir")
        
        accion = input("Seleccione una opción: ")

        if accion == "1":
            mi_cuenta.imprimir()
        elif accion == "2":
            mi_cuenta.consultar_saldo()
        elif accion == "3":
            monto = float(input("Monto a consignar: "))
            mi_cuenta.consignar(monto)
        elif accion == "4":
            monto = float(input("Monto a retirar: "))
            mi_cuenta.retirar(monto)
        elif accion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()