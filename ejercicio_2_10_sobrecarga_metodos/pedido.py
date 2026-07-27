

from dataclasses import dataclass
from typing import Optional


@dataclass
class Pedido:
    """Representa el pedido que realiza un cliente en un restaurante."""

    primer_plato: str
    costo_primer_plato: float
    bebida: str
    costo_bebida: float
    segundo_plato: Optional[str] = None
    costo_segundo_plato: float = 0.0
    postre: Optional[str] = None
    costo_postre: float = 0.0

    def calcular_valor(self) -> float:
        """Calcula el valor total del pedido según los ítems presentes.

        Actúa como los tres métodos sobrecargados del ejercicio original:
        - primer plato + bebida
        - primer plato + segundo plato + bebida
        - primer plato + segundo plato + bebida + postre
        """
        total = self.costo_primer_plato + self.costo_bebida
        if self.segundo_plato:
            total += self.costo_segundo_plato
        if self.postre:
            total += self.costo_postre
        return total

    def mostrar(self) -> None:
        """Muestra en pantalla el detalle del pedido y su costo total."""
        print("----- Detalle del pedido -----")
        print(f"Primer plato: {self.primer_plato} (${self.costo_primer_plato:.2f})")
        if self.segundo_plato:
            print(f"Segundo plato: {self.segundo_plato} (${self.costo_segundo_plato:.2f})")
        print(f"Bebida: {self.bebida} (${self.costo_bebida:.2f})")
        if self.postre:
            print(f"Postre: {self.postre} (${self.costo_postre:.2f})")
        print(f"Total a pagar: ${self.calcular_valor():.2f}")
        print("-------------------------------")