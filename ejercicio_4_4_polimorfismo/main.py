"""Programa de consola: ejercicio 4.4 - Polimorfismo (Profesor / ProfesorTitular)."""

from profesor import Profesor, ProfesorTitular


def main() -> None:
    # Caso base: variable "profesor1" referenciando un objeto ProfesorTitular.
    profesor1 = ProfesorTitular()
    profesor1.imprimir()  # -> "Es un profesor titular." (polimorfismo)

    # Ejercicio propuesto (equivalente al casting Java `(Profesor) profesor1`):
    # en Python no existe conversión de tipo explícita; profesor2 sigue
    # apuntando al mismo objeto ProfesorTitular, por lo que el resultado
    # es idéntico.
    profesor2: Profesor = profesor1
    profesor2.imprimir()  # -> "Es un profesor titular." (sin cambios)


if __name__ == "__main__":
    main()
    