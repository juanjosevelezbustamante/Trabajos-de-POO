"""Programa de consola: ejercicio 4.6 - Métodos polimórficos."""

from profesor import Profesor, ProfesorTitular


def main() -> None:
    profesor1 = ProfesorTitular(anios=5)

    # En Java, "Profesor profesor1 = new ProfesorTitular(); profesor1.imprimirAños();"
    # NO compila, porque Profesor no declara imprimirAños().
    # En Python sí es posible, porque no hay tipos declarados en las variables:
    # el intérprete solo verifica en tiempo de ejecución que el objeto real
    # (un ProfesorTitular) sí tenga el método.
    profesor1.imprimir_anios()  # -> "Años = 5"

    # Usando polimorfismo normal, el método sobrescrito sigue funcionando:
    referencia_general: Profesor = profesor1
    referencia_general.imprimir()  # -> "Es un profesor titular."


if __name__ == "__main__":
    main()