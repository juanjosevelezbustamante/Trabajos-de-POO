"""
Clase RepositorioContactos
--------------------------
Encapsula TODO el manejo del archivo (File Handling) y expone las
cuatro operaciones CRUD que pide la actividad:
    - Create  (crear)
    - Read    (leer)
    - Update  (actualizar)
    - Delete  (eliminar)

De esta forma la interfaz gráfica (Tkinter) nunca toca el archivo
directamente: solo conversa con este repositorio. Esto respeta el
principio de responsabilidad única y separa la lógica de negocio
de la lógica de presentación.
"""

import os
from contacto import Contacto


class RepositorioContactos:

    def __init__(self, ruta_archivo: str = "data/contactos.txt"):
        self._ruta_archivo = ruta_archivo
        carpeta = os.path.dirname(self._ruta_archivo)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta, exist_ok=True)
        if not os.path.exists(self._ruta_archivo):
            open(self._ruta_archivo, "w", encoding="utf-8").close()

    # ---------------- CREATE ----------------
    def crear(self, nombre: str, telefono: str, email: str) -> Contacto:
        contactos = self.leer_todos()
        nuevo_id = (max([c.id for c in contactos]) + 1) if contactos else 1
        nuevo = Contacto(nuevo_id, nombre, telefono, email)
        with open(self._ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(nuevo.to_linea() + "\n")
        return nuevo

    # ---------------- READ ----------------
    def leer_todos(self) -> list[Contacto]:
        contactos = []
        with open(self._ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip():
                    contactos.append(Contacto.from_linea(linea))
        return contactos

    def buscar_por_id(self, id_contacto: int) -> Contacto | None:
        for c in self.leer_todos():
            if c.id == id_contacto:
                return c
        return None

    # ---------------- UPDATE ----------------
    def actualizar(self, id_contacto: int, nombre: str, telefono: str, email: str) -> bool:
        contactos = self.leer_todos()
        encontrado = False
        for c in contactos:
            if c.id == id_contacto:
                c.actualizar(nombre, telefono, email)
                encontrado = True
                break
        if encontrado:
            self._guardar_todos(contactos)
        return encontrado

    # ---------------- DELETE ----------------
    def eliminar(self, id_contacto: int) -> bool:
        contactos = self.leer_todos()
        nuevos = [c for c in contactos if c.id != id_contacto]
        if len(nuevos) == len(contactos):
            return False
        self._guardar_todos(nuevos)
        return True

    # ---------------- Utilidad interna ----------------
    def _guardar_todos(self, contactos: list[Contacto]) -> None:
        """Reescribe el archivo completo con la lista de contactos vigente."""
        with open(self._ruta_archivo, "w", encoding="utf-8") as archivo:
            for c in contactos:
                archivo.write(c.to_linea() + "\n")
