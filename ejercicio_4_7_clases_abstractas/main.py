"""Programa de consola: ejercicio 4.7 - Clases abstractas (jerarquía de animales)."""

from animales import Animal, Perro, Lobo, Leon, Gato


def main() -> None:
    animales: list[Animal] = [Perro(), Lobo(), Leon(), Gato()]

    for animal in animales:
        animal.imprimir()
        print()


if __name__ == "__main__":
    main()