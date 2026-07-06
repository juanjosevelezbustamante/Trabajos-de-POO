"""
Genera una IMAGEN DE VISTA PREVIA (mockup) del diseño de la interfaz,
fiel a los widgets definidos en app.py. No es una captura real de
ejecución (este entorno no tiene tkinter disponible); sirve como
referencia visual. Para el entregable final, el estudiante debe
ejecutar `python app.py` en su propia máquina y tomar la captura real.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=150)
ax.set_xlim(0, 640)
ax.set_ylim(0, 480)
ax.invert_yaxis()
ax.axis("off")
ax.add_patch(patches.Rectangle((0, 0), 640, 480, facecolor="#f0f0f0", edgecolor="black"))

# Barra de título
ax.add_patch(patches.Rectangle((0, 0), 640, 24, facecolor="#2b2b2b"))
ax.text(10, 15, "Gestión de Contactos - CRUD con archivo", color="white", fontsize=9, va="center")

# Marco formulario
ax.add_patch(patches.Rectangle((10, 34), 620, 120, facecolor="white", edgecolor="gray"))
ax.text(20, 44, "Datos del contacto", fontsize=8, color="#333333")

campos = [("Nombre:", 70), ("Teléfono:", 100), ("Email:", 130)]
for etiqueta, y in campos:
    ax.text(25, y, etiqueta, fontsize=9, va="center")
    ax.add_patch(patches.Rectangle((110, y - 9), 480, 18, facecolor="#ffffff", edgecolor="black"))

# Botones CRUD
botones = ["Create", "Read / Refrescar", "Update", "Delete", "Limpiar"]
x = 15
ancho_boton = 120
for b in botones:
    ax.add_patch(patches.FancyBboxPatch((x, 162), ancho_boton - 8, 26,
                 boxstyle="round,pad=0.02", facecolor="#e0e0e0", edgecolor="black"))
    ax.text(x + (ancho_boton - 8) / 2, 175, b, fontsize=7.5, ha="center", va="center")
    x += ancho_boton

# Marco tabla
ax.add_patch(patches.Rectangle((10, 200), 620, 230, facecolor="white", edgecolor="gray"))
ax.text(20, 210, "Contactos guardados en el archivo", fontsize=8, color="#333333")

columnas = [("ID", 40), ("Nombre", 200), ("Teléfono", 340), ("Email", 460)]
ax.add_patch(patches.Rectangle((20, 220), 600, 20, facecolor="#d9d9d9", edgecolor="black"))
for texto, x0 in columnas:
    ax.text(x0 + 5, 230, texto, fontsize=8, fontweight="bold", va="center")

filas_ejemplo = [
    ("1", "Ana Torres", "3001234567", "ana.torres@mail.com"),
    ("2", "Luis Pérez", "3109876543", "luis.perez@mail.com"),
    ("3", "Marta Gómez", "3159988776", "marta.gomez@mail.com"),
]
y = 240
for fila in filas_ejemplo:
    ax.add_patch(patches.Rectangle((20, y), 600, 20, facecolor="white", edgecolor="#cccccc"))
    for (texto, x0), valor in zip(columnas, fila):
        ax.text(x0 + 5, y + 10, valor, fontsize=7.5, va="center")
    y += 20

# Barra de estado
ax.add_patch(patches.Rectangle((10, 450), 620, 20, facecolor="#e8e8e8", edgecolor="gray"))
ax.text(15, 460, "Lista de contactos actualizada desde el archivo.", fontsize=7.5, va="center", style="italic")

plt.tight_layout(pad=0.3)
plt.savefig("interfaz_mockup.png", facecolor="#f0f0f0")
print("Mockup generado.")
