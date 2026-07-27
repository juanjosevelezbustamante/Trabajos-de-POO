


class Profesor:
    """Clase padre que representa un profesor genérico."""

    def imprimir(self) -> None:
        print("Es un profesor.")


class ProfesorTitular(Profesor):
    """Clase hija que redefine el método imprimir heredado de Profesor."""

    def imprimir(self) -> None:
        print("Es un profesor titular.")