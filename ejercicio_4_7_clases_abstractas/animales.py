
from abc import ABC, abstractmethod


class Animal(ABC):
    """Clase raíz y abstracta que modela un animal genérico."""

    @abstractmethod
    def get_nombre_cientifico(self) -> str:
        """Devuelve el nombre científico del animal."""

    @abstractmethod
    def get_sonido(self) -> str:
        """Devuelve el sonido característico del animal."""

    @abstractmethod
    def get_alimentos(self) -> str:
        """Devuelve el tipo de alimentación del animal."""

    @abstractmethod
    def get_habitat(self) -> str:
        """Devuelve el hábitat del animal."""

    def imprimir(self) -> None:
        """Imprime en pantalla todos los atributos del animal."""
        print(f"Clase: {type(self).__name__}")
        print(f"  Nombre científico: {self.get_nombre_cientifico()}")
        print(f"  Sonido: {self.get_sonido()}")
        print(f"  Alimentación: {self.get_alimentos()}")
        print(f"  Hábitat: {self.get_habitat()}")


class Canido(Animal, ABC):
    """Clase abstracta intermedia para la familia de los cánidos."""


class Felino(Animal, ABC):
    """Clase abstracta intermedia para la familia de los felinos."""


class Perro(Canido):
    def get_sonido(self) -> str:
        return "Ladrido"

    def get_alimentos(self) -> str:
        return "Carnívoro"

    def get_habitat(self) -> str:
        return "Doméstico"

    def get_nombre_cientifico(self) -> str:
        return "Canis lupus familiaris"


class Lobo(Canido):
    def get_sonido(self) -> str:
        return "Aullido"

    def get_alimentos(self) -> str:
        return "Carnívoro"

    def get_habitat(self) -> str:
        return "Bosque"

    def get_nombre_cientifico(self) -> str:
        return "Canis lupus"


class Leon(Felino):
    def get_sonido(self) -> str:
        return "Rugido"

    def get_alimentos(self) -> str:
        return "Carnívoro"

    def get_habitat(self) -> str:
        return "Pradera"

    def get_nombre_cientifico(self) -> str:
        return "Panthera leo"


class Gato(Felino):
    def get_sonido(self) -> str:
        return "Maullido"

    def get_alimentos(self) -> str:
        return "Ratones"

    def get_habitat(self) -> str:
        return "Doméstico"

    def get_nombre_cientifico(self) -> str:
        return "Felis silvestris catus"