
class Profesor:
    """Clase padre que representa un profesor genérico."""

    def imprimir(self) -> None:
        print("Es un profesor.")


class ProfesorTitular(Profesor):
    """Clase hija que agrega el atributo 'años' y el método imprimir_anios."""

    def __init__(self, anios: int = 0) -> None:
        self.anios = anios

    def imprimir(self) -> None:
        print("Es un profesor titular.")

    def imprimir_anios(self) -> None:
        print(f"Años = {self.anios}")