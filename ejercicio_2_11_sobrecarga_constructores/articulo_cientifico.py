
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ArticuloCientifico:
    titulo: str
    autor: str
    palabras_clave: List[str] = field(default_factory=list)
    publicacion: Optional[str] = None
    anio: Optional[int] = None
    resumen: Optional[str] = None

    @classmethod
    def con_titulo_y_autor(cls, titulo: str, autor: str) -> "ArticuloCientifico":
        """Equivalente al primer constructor sobrecargado: solo título y autor."""
        return cls(titulo=titulo, autor=autor)

    @classmethod
    def con_metadatos(
        cls,
        titulo: str,
        autor: str,
        palabras_clave: List[str],
        publicacion: str,
        anio: int,
    ) -> "ArticuloCientifico":
        """Equivalente al segundo constructor: invoca al primero y agrega metadatos."""
        articulo = cls.con_titulo_y_autor(titulo, autor)
        articulo.palabras_clave = palabras_clave
        articulo.publicacion = publicacion
        articulo.anio = anio
        return articulo

    @classmethod
    def completo(
        cls,
        titulo: str,
        autor: str,
        palabras_clave: List[str],
        publicacion: str,
        anio: int,
        resumen: str,
    ) -> "ArticuloCientifico":
        """Equivalente al tercer constructor: invoca al segundo y agrega el resumen."""
        articulo = cls.con_metadatos(titulo, autor, palabras_clave, publicacion, anio)
        articulo.resumen = resumen
        return articulo

    def imprimir(self) -> None:
        """Imprime en pantalla los atributos del artículo científico."""
        print("----- Artículo científico -----")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Palabras clave: {', '.join(self.palabras_clave) if self.palabras_clave else '-'}")
        print(f"Publicación: {self.publicacion or '-'}")
        print(f"Año: {self.anio if self.anio is not None else '-'}")
        print(f"Resumen: {self.resumen or '-'}")
        print("--------------------------------")