"""Programa de consola: ejercicio 2.10 - Sobrecarga de métodos (clase Pedido)."""

from pedido import Pedido


def main() -> None:
    # Pedido 1: primer plato + bebida
    pedido1 = Pedido(
        primer_plato="Sopa de verduras",
        costo_primer_plato=6.50,
        bebida="Jugo de naranja",
        costo_bebida=2.50,
    )

    # Pedido 2: primer plato + segundo plato + bebida
    pedido2 = Pedido(
        primer_plato="Ensalada César",
        costo_primer_plato=7.00,
        bebida="Limonada",
        costo_bebida=2.00,
        segundo_plato="Lomo saltado",
        costo_segundo_plato=15.00,
    )

    # Pedido 3: primer plato + segundo plato + bebida + postre
    pedido3 = Pedido(
        primer_plato="Crema de espárragos",
        costo_primer_plato=6.00,
        bebida="Agua mineral",
        costo_bebida=1.50,
        segundo_plato="Pollo al horno",
        costo_segundo_plato=14.00,
        postre="Tiramisú",
        costo_postre=5.50,
    )

    for pedido in (pedido1, pedido2, pedido3):
        pedido.mostrar()


if __name__ == "__main__":
    main()