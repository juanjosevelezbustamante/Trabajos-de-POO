import tkinter as tk
from tkinter import messagebox

class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None

    def verificar_edad(self, edad):
        if edad < 18:
            raise IllegalArgumentException("El vendedor debe ser mayor de 18 anos.")
        elif 0 <= edad < 120:
            self.edad = edad
        else:
            raise IllegalArgumentException("La edad no puede ser negativa ni mayor a 120.")

    def imprimir(self):
        return (f"Nombre del vendedor   = {self.nombre}\n"
                f"Apellidos del vendedor = {self.apellidos}\n"
                f"Edad del vendedor      = {self.edad}")


class IllegalArgumentException(Exception):
    pass


# ── Logica de la GUI ───────────────────────────────────────────────────────────
def registrar():
    area_texto.config(state='normal')
    area_texto.delete('1.0', tk.END)

    nombre    = entry_nombre.get().strip()
    apellidos = entry_apellidos.get().strip()
    edad_str  = entry_edad.get().strip()

    escribir("=" * 50 + "\n", 'sep')
    escribir(" REGISTRO DE VENDEDOR\n", 'titulo')
    escribir("=" * 50 + "\n", 'sep')

    try:
        if not nombre or not apellidos:
            raise ValueError("Nombre y Apellidos son obligatorios.")
        if not edad_str:
            raise ValueError("Debe ingresar la edad.")

        edad = int(edad_str)
        vendedor = Vendedor(nombre, apellidos)
        vendedor.verificar_edad(edad)

        escribir(vendedor.imprimir() + "\n", 'ok')
        escribir("\nVendedor registrado correctamente.\n", 'ok')

    except IllegalArgumentException as e:
        escribir(f"EXCEPCION IllegalArgumentException:\n  {e}\n", 'error')
    except ValueError as e:
        escribir(f"EXCEPCION ValueError:\n  {e}\n", 'error')
    except Exception as e:
        escribir(f"EXCEPCION {type(e).__name__}:\n  {e}\n", 'error')
    finally:
        escribir("=" * 50 + "\n", 'sep')
        escribir("Proceso finalizado.\n", 'finally_')

    area_texto.config(state='disabled')


def limpiar():
    for e in [entry_nombre, entry_apellidos, entry_edad]:
        e.delete(0, tk.END)
    area_texto.config(state='normal')
    area_texto.delete('1.0', tk.END)
    area_texto.config(state='disabled')
    entry_nombre.focus()


def escribir(texto, tag):
    area_texto.insert(tk.END, texto, tag)


# ── Ventana principal ──────────────────────────────────────────────────────────
ventana = tk.Tk()
ventana.title("Registro de Vendedor")
ventana.geometry("600x620")
ventana.resizable(False, False)
ventana.configure(bg='#2B2B2B')

tk.Label(ventana, text="Registro de Vendedor",
         bg='#2B2B2B', fg='#E0E0E0', font=('Arial', 16, 'bold')).pack(pady=(18, 2))
tk.Label(ventana, text="Validacion de datos con excepciones",
         bg='#2B2B2B', fg='#888888', font=('Arial', 10)).pack(pady=(0, 16))

# ── Campos de entrada ──────────────────────────────────────────────────────────
frame_form = tk.Frame(ventana, bg='#2B2B2B')
frame_form.pack(padx=28, fill='x')

def campo(parent, label):
    f = tk.Frame(parent, bg='#2B2B2B')
    f.pack(fill='x', pady=5)
    tk.Label(f, text=label, bg='#2B2B2B', fg='#AAAAAA',
             font=('Arial', 9), width=12, anchor='w').pack(side='left')
    e = tk.Entry(f, font=('Arial', 12), bg='#3C3C3C', fg='white',
                 insertbackground='white', relief='flat', bd=6)
    e.pack(side='left', fill='x', expand=True, ipady=6)
    return e

entry_nombre    = campo(frame_form, "Nombre")
entry_apellidos = campo(frame_form, "Apellidos")
entry_edad      = campo(frame_form, "Edad")

# ── Area de texto ──────────────────────────────────────────────────────────────
tk.Frame(ventana, height=10, bg='#2B2B2B').pack()
frame_texto = tk.Frame(ventana, bg='#1E1E1E')
frame_texto.pack(padx=28, fill='both', expand=True)

area_texto = tk.Text(frame_texto, bg='#1E1E1E', fg='#D4D4D4',
                     font=('Courier New', 11), state='disabled',
                     relief='flat', padx=10, pady=8, wrap='word', height=14)
area_texto.pack(fill='both', expand=True)

area_texto.tag_config('normal',   foreground='#D4D4D4')
area_texto.tag_config('error',    foreground='#F44747', font=('Courier New', 11, 'bold'))
area_texto.tag_config('finally_', foreground='#DCDCAA')
area_texto.tag_config('titulo',   foreground='#569CD6', font=('Courier New', 11, 'bold'))
area_texto.tag_config('sep',      foreground='#555555')
area_texto.tag_config('ok',       foreground='#4EC9B0', font=('Courier New', 11, 'bold'))

# ── Botones ────────────────────────────────────────────────────────────────────
frame_botones = tk.Frame(ventana, bg='#2B2B2B')
frame_botones.pack(pady=14)

tk.Button(frame_botones, text="Registrar", command=registrar,
          bg='#0E639C', fg='white', font=('Arial', 11, 'bold'),
          relief='flat', padx=22, pady=8, cursor='hand2',
          activebackground='#1177BB', activeforeground='white').pack(side='left', padx=8)

tk.Button(frame_botones, text="Limpiar", command=limpiar,
          bg='#3C3C3C', fg='#CCCCCC', font=('Arial', 11),
          relief='flat', padx=22, pady=8, cursor='hand2',
          activebackground='#505050', activeforeground='white').pack(side='left', padx=8)

ventana.bind('<Return>', lambda e: registrar())
entry_nombre.focus()
ventana.mainloop()