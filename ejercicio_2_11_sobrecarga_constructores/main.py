"""Programa de consola: ejercicio 2.11 - Sobrecarga de constructores (ArticuloCientifico)."""

from articulo_cientifico import ArticuloCientifico


def main() -> None:
    # Se utiliza el "tercer constructor" (completo), que internamente
    # encadena con_metadatos() -> con_titulo_y_autor(), igual que el
    # ejercicio original en Java.
    articulo = ArticuloCientifico.completo(
        titulo="Aprendizaje automático aplicado a la detección de fraude",
        autor="M. Gómez",
        palabras_clave=["machine learning", "fraude", "clasificación"],
        publicacion="Revista de Ciencias de la Computación",
        anio=2024,
        resumen=(
            "Se presenta un modelo de clasificación para detectar transacciones "
            "fraudulentas en tiempo real con alta precisión."
        ),
    )

    articulo.imprimir()


if __name__ == "__main__":
    main()