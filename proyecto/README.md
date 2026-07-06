# Gestión de Contactos — CRUD con archivo (Actividad 5, POO)

Aplicación de escritorio en Python con interfaz gráfica (Tkinter) que
implementa las cuatro operaciones **CRUD** (Create, Read, Update, Delete)
sobre un archivo de texto (`data/contactos.txt`), aplicando los
principios de la Programación Orientada a Objetos.

## Estructura del proyecto

```
proyecto/
├── src/
│   ├── contacto.py               # Clase modelo (entidad Contacto)
│   ├── repositorio_contactos.py  # Manejo de archivo + operaciones CRUD
│   └── app.py                    # Interfaz gráfica Tkinter (punto de entrada)
├── data/
│   └── contactos.txt             # Archivo de persistencia (se crea solo)
├── diagramas/
│   ├── clases.dot / clases.png
│   └── casos_de_uso.dot / casos_de_uso.png
└── README.md
```

## Requisitos

- Python 3.10 o superior
- Tkinter (incluido con Python en Windows/Mac). En Linux:
  ```bash
  sudo apt install python3-tk
  ```

## Ejecución

```bash
cd proyecto/src
python app.py
```

## Diseño (POO)

- **Contacto**: entidad con atributos privados y propiedades (encapsulamiento).
- **RepositorioContactos**: responsable único del manejo del archivo
  (abrir, leer, escribir, reescribir) y de las operaciones CRUD.
- **VentanaPrincipal**: interfaz gráfica (Tkinter) que solo se comunica
  con el repositorio, nunca con el archivo directamente.



