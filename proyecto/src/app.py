"""
Actividad 5 - Programación Orientada a Objetos
Aplicación de Interfaz Gráfica con archivo
(formulario con botones Create, Read, Update y Delete)

Punto de entrada de la aplicación. Contiene la clase VentanaPrincipal,
que arma la interfaz gráfica con Tkinter y delega toda la persistencia
en RepositorioContactos (manejo de archivo).

Para ejecutar:
    python app.py
Requisitos: Python 3.10+ (usa la sintaxis "list[Contacto] | None").
Tkinter viene incluido con Python en Windows/Mac. En Linux instalar con:
    sudo apt install python3-tk
"""

import tkinter as tk
from tkinter import ttk, messagebox

from repositorio_contactos import RepositorioContactos


class VentanaPrincipal(tk.Tk):
    """Ventana principal: formulario + tabla + botones CRUD."""

    def __init__(self):
        super().__init__()
        self.title("Gestión de Contactos - CRUD con archivo")
        self.geometry("640x480")
        self.resizable(False, False)

        self.repositorio = RepositorioContactos("../data/contactos.txt")
        self.id_seleccionado = None  # id del contacto seleccionado en la tabla

        self._crear_widgets()
        self._cargar_tabla()

    # ------------------------------------------------------------------
    # Construcción de la interfaz
    # ------------------------------------------------------------------
    def _crear_widgets(self):
        # ---- Formulario ----
        marco_formulario = ttk.LabelFrame(self, text="Datos del contacto")
        marco_formulario.pack(fill="x", padx=10, pady=10)

        ttk.Label(marco_formulario, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entrada_nombre = ttk.Entry(marco_formulario, width=40)
        self.entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(marco_formulario, text="Teléfono:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entrada_telefono = ttk.Entry(marco_formulario, width=40)
        self.entrada_telefono.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(marco_formulario, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entrada_email = ttk.Entry(marco_formulario, width=40)
        self.entrada_email.grid(row=2, column=1, padx=5, pady=5)

        # ---- Botones CRUD ----
        marco_botones = ttk.Frame(self)
        marco_botones.pack(fill="x", padx=10, pady=(0, 10))

        ttk.Button(marco_botones, text="Create", command=self._crear).pack(side="left", expand=True, fill="x", padx=3)
        ttk.Button(marco_botones, text="Read / Refrescar", command=self._cargar_tabla).pack(side="left", expand=True, fill="x", padx=3)
        ttk.Button(marco_botones, text="Update", command=self._actualizar).pack(side="left", expand=True, fill="x", padx=3)
        ttk.Button(marco_botones, text="Delete", command=self._eliminar).pack(side="left", expand=True, fill="x", padx=3)
        ttk.Button(marco_botones, text="Limpiar", command=self._limpiar_formulario).pack(side="left", expand=True, fill="x", padx=3)

        # ---- Tabla (Treeview) ----
        marco_tabla = ttk.LabelFrame(self, text="Contactos guardados en el archivo")
        marco_tabla.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        columnas = ("id", "nombre", "telefono", "email")
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas, show="headings", height=12)
        for col, texto, ancho in (
            ("id", "ID", 40),
            ("nombre", "Nombre", 180),
            ("telefono", "Teléfono", 120),
            ("email", "Email", 220),
        ):
            self.tabla.heading(col, text=texto)
            self.tabla.column(col, width=ancho)
        self.tabla.pack(fill="both", expand=True, padx=5, pady=5)
        self.tabla.bind("<<TreeviewSelect>>", self._al_seleccionar_fila)

        # ---- Barra de estado ----
        self.estado = tk.StringVar(value="Listo.")
        ttk.Label(self, textvariable=self.estado, anchor="w").pack(fill="x", padx=10, pady=(0, 8))

    # ------------------------------------------------------------------
    # Operaciones CRUD conectadas a los botones
    # ------------------------------------------------------------------
    def _crear(self):
        nombre, telefono, email = self._leer_formulario()
        if not self._validar(nombre, telefono, email):
            return
        nuevo = self.repositorio.crear(nombre, telefono, email)
        self._cargar_tabla()
        self._limpiar_formulario()
        self.estado.set(f"Contacto creado con ID {nuevo.id}.")

    def _cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for contacto in self.repositorio.leer_todos():
            self.tabla.insert("", "end", values=(contacto.id, contacto.nombre, contacto.telefono, contacto.email))
        self.estado.set("Lista de contactos actualizada desde el archivo.")

    def _actualizar(self):
        if self.id_seleccionado is None:
            messagebox.showwarning("Actualizar", "Selecciona primero un contacto de la tabla.")
            return
        nombre, telefono, email = self._leer_formulario()
        if not self._validar(nombre, telefono, email):
            return
        exito = self.repositorio.actualizar(self.id_seleccionado, nombre, telefono, email)
        if exito:
            self._cargar_tabla()
            self._limpiar_formulario()
            self.estado.set(f"Contacto {self.id_seleccionado} actualizado.")
        else:
            messagebox.showerror("Actualizar", "No se encontró el contacto.")

    def _eliminar(self):
        if self.id_seleccionado is None:
            messagebox.showwarning("Eliminar", "Selecciona primero un contacto de la tabla.")
            return
        if messagebox.askyesno("Eliminar", f"¿Eliminar el contacto {self.id_seleccionado}?"):
            self.repositorio.eliminar(self.id_seleccionado)
            self._cargar_tabla()
            self._limpiar_formulario()
            self.estado.set("Contacto eliminado.")

    # ------------------------------------------------------------------
    # Utilidades de la interfaz
    # ------------------------------------------------------------------
    def _al_seleccionar_fila(self, evento):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        valores = self.tabla.item(seleccion[0], "values")
        self.id_seleccionado = int(valores[0])
        self.entrada_nombre.delete(0, "end")
        self.entrada_nombre.insert(0, valores[1])
        self.entrada_telefono.delete(0, "end")
        self.entrada_telefono.insert(0, valores[2])
        self.entrada_email.delete(0, "end")
        self.entrada_email.insert(0, valores[3])

    def _leer_formulario(self):
        return (
            self.entrada_nombre.get().strip(),
            self.entrada_telefono.get().strip(),
            self.entrada_email.get().strip(),
        )

    def _validar(self, nombre, telefono, email) -> bool:
        if not nombre or not telefono or not email:
            messagebox.showwarning("Datos incompletos", "Todos los campos son obligatorios.")
            return False
        return True

    def _limpiar_formulario(self):
        self.entrada_nombre.delete(0, "end")
        self.entrada_telefono.delete(0, "end")
        self.entrada_email.delete(0, "end")
        self.id_seleccionado = None
        self.tabla.selection_remove(self.tabla.selection())


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
