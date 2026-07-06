"""
Clase Contacto
---------------
Representa la entidad principal del sistema (modelo de datos).
Aplica el principio de encapsulamiento propio de la Programación
Orientada a Objetos: los atributos son privados y se accede a ellos
mediante propiedades (getters) y métodos.
"""


class Contacto:
    """Modelo de datos que representa un contacto almacenado en el archivo."""

    def __init__(self, id_contacto: int, nombre: str, telefono: str, email: str):
        self._id = int(id_contacto)
        self._nombre = nombre
        self._telefono = telefono
        self._email = email

    # ---------- Propiedades (getters) ----------
    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def telefono(self) -> str:
        return self._telefono

    @property
    def email(self) -> str:
        return self._email

    # ---------- Setters ----------
    def actualizar(self, nombre: str, telefono: str, email: str) -> None:
        self._nombre = nombre
        self._telefono = telefono
        self._email = email

    # ---------- Conversión desde/hacia el archivo ----------
    def to_linea(self) -> str:
        """Convierte el objeto en una línea de texto separada por comas
        para ser almacenada en el archivo (persistencia)."""
        return f"{self._id},{self._nombre},{self._telefono},{self._email}"

    @staticmethod
    def from_linea(linea: str) -> "Contacto":
        """Crea un objeto Contacto a partir de una línea leída del archivo."""
        partes = linea.strip().split(",")
        return Contacto(int(partes[0]), partes[1], partes[2], partes[3])

    def __str__(self) -> str:
        return f"[{self._id}] {self._nombre} | {self._telefono} | {self._email}"
