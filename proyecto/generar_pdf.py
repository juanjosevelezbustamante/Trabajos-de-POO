from reportlab.lib.pagesizes import letter
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image,
                                 PageBreak, Preformatted)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

styles = getSampleStyleSheet()
titulo = ParagraphStyle("TituloCustom", parent=styles["Title"], fontSize=18, spaceAfter=6)
h2 = ParagraphStyle("H2Custom", parent=styles["Heading2"], spaceBefore=14, spaceAfter=6, textColor=colors.HexColor("#1a1a1a"))
normal = styles["Normal"]
code_style = ParagraphStyle("Code", parent=styles["Normal"], fontName="Courier", fontSize=7.5, leading=9)

story = []

story.append(Paragraph("Actividad 5 — Aplicación de Interfaz Gráfica con Archivo", titulo))
story.append(Paragraph("Programación Orientada a Objetos · Formulario CRUD (Create, Read, Update, Delete)", normal))
story.append(Spacer(1, 16))

story.append(Paragraph("1. Descripción del proyecto", h2))
story.append(Paragraph(
    "Se desarrolló una aplicación de escritorio en Python con interfaz gráfica "
    "(Tkinter) que gestiona una lista de contactos persistida en un archivo de "
    "texto plano. La aplicación implementa las cuatro operaciones fundamentales "
    "de manejo de archivos: <b>Create</b> (crear un contacto nuevo), "
    "<b>Read</b> (leer/listar los contactos existentes), <b>Update</b> "
    "(actualizar un contacto seleccionado) y <b>Delete</b> (eliminar un "
    "contacto). El diseño separa claramente el modelo de datos, la capa de "
    "persistencia y la interfaz gráfica, siguiendo los principios de la "
    "Programación Orientada a Objetos (encapsulamiento y responsabilidad única).",
    normal))
story.append(Spacer(1, 8))

story.append(Paragraph("2. Arquitectura de clases", h2))
story.append(Paragraph(
    "<b>Contacto</b>: clase modelo con atributos privados (_id, _nombre, "
    "_telefono, _email) expuestos mediante propiedades, y métodos para "
    "convertirse hacia/desde una línea de texto del archivo.<br/>"
    "<b>RepositorioContactos</b>: encapsula todo el manejo del archivo "
    "(apertura, lectura, escritura) y expone los métodos crear(), "
    "leer_todos(), actualizar() y eliminar().<br/>"
    "<b>VentanaPrincipal</b>: interfaz gráfica construida con Tkinter que "
    "arma el formulario, la tabla (Treeview) y los botones CRUD, y delega "
    "toda la persistencia en el repositorio.",
    normal))
story.append(Spacer(1, 10))

story.append(Paragraph("3. Diagrama de clases", h2))
story.append(Image("diagramas/clases.png", width=6.3 * inch, height=6.3 * inch * (41143/46738) if False else None) if False else Image("diagramas/clases.png", width=6.2*inch, height=3.6*inch))
story.append(Spacer(1, 10))

story.append(PageBreak())
story.append(Paragraph("4. Diagrama de casos de uso", h2))
story.append(Image("diagramas/casos_de_uso.png", width=6.2*inch, height=3.2*inch))
story.append(Spacer(1, 14))

story.append(Paragraph("5. Interfaz de usuario", h2))
story.append(Paragraph(
    "Vista previa fiel del diseño de la interfaz (los widgets, botones y "
    "tabla exactamente como se definen en el código). "
    "<b>Nota:</b> esta imagen es una vista previa generada para documentar "
    "el diseño; la captura de pantalla real de la aplicación en ejecución "
    "debe adjuntarse por separado, tomada al correr <font face='Courier'>python app.py</font> "
    "en un equipo con Tkinter instalado.",
    normal))
story.append(Spacer(1, 6))
story.append(Image("diagramas/interfaz_mockup.png", width=5.6*inch, height=4.2*inch))
story.append(Spacer(1, 10))

story.append(PageBreak())
story.append(Paragraph("6. Enlace del repositorio en GitHub", h2))
story.append(Paragraph(
    "Repositorio: <font face='Courier'>https://github.com/TU-USUARIO/TU-REPOSITORIO</font> "
    "(reemplazar por el enlace real una vez publicado el proyecto).",
    normal))
story.append(Spacer(1, 10))

story.append(Paragraph("7. Instrucciones de ejecución", h2))
story.append(Preformatted(
    "cd proyecto/src\n"
    "python app.py\n\n"
    "Requisitos: Python 3.10+, Tkinter\n"
    "(Linux: sudo apt install python3-tk)",
    code_style))
story.append(Spacer(1, 10))

story.append(Paragraph("8. Manejo de archivo (extracto de código)", h2))
story.append(Paragraph("Operaciones CRUD implementadas en RepositorioContactos:", normal))
story.append(Spacer(1, 4))
codigo = """def crear(self, nombre, telefono, email):
    contactos = self.leer_todos()
    nuevo_id = (max([c.id for c in contactos]) + 1) if contactos else 1
    nuevo = Contacto(nuevo_id, nombre, telefono, email)
    with open(self._ruta_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(nuevo.to_linea() + "\\n")
    return nuevo

def leer_todos(self):
    contactos = []
    with open(self._ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip():
                contactos.append(Contacto.from_linea(linea))
    return contactos

def actualizar(self, id_contacto, nombre, telefono, email):
    contactos = self.leer_todos()
    for c in contactos:
        if c.id == id_contacto:
            c.actualizar(nombre, telefono, email)
            self._guardar_todos(contactos)
            return True
    return False

def eliminar(self, id_contacto):
    contactos = self.leer_todos()
    nuevos = [c for c in contactos if c.id != id_contacto]
    if len(nuevos) == len(contactos):
        return False
    self._guardar_todos(nuevos)
    return True"""
story.append(Preformatted(codigo, code_style))

doc = SimpleDocTemplate("Actividad5_CRUD_GUI.pdf", pagesize=letter,
                         topMargin=0.6*inch, bottomMargin=0.6*inch,
                         leftMargin=0.7*inch, rightMargin=0.7*inch)
doc.build(story)
print("PDF generado.")
