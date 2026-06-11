import tkinter as tk

def ejecutar_prueba():
    area_texto.config(state='normal')
    area_texto.delete('1.0', tk.END)

    numerador_str   = entry_numerador.get().strip()
    denominador_str = entry_denominador.get().strip()

    # ── Primer bloque try: division ───────────────────────────────────────────
    escribir("=" * 48 + "\n", 'sep')
    escribir(" PRIMER BLOQUE TRY - Division\n", 'titulo')
    escribir("=" * 48 + "\n", 'sep')
    try:
        escribir("Ingresando al primer try\n", 'normal')
        if numerador_str == "" or denominador_str == "":
            raise ValueError("Debes ingresar Numerador y Denominador.")
        numerador   = float(numerador_str)
        denominador = float(denominador_str)
        cociente    = numerador / denominador     # ZeroDivisionError si denominador=0
        entry_cociente.config(state='normal')
        entry_cociente.delete(0, tk.END)
        entry_cociente.insert(0, str(cociente))
        entry_cociente.config(state='readonly')
        escribir(f"Numerador   = {numerador}\n",   'normal')
        escribir(f"Denominador = {denominador}\n", 'normal')
        escribir(f"Cociente    = {cociente}\n",    'ok')
    except ZeroDivisionError:
        entry_cociente.config(state='normal')
        entry_cociente.delete(0, tk.END)
        entry_cociente.insert(0, "Error")
        entry_cociente.config(state='readonly')
        escribir("EXCEPCION: Division por cero (denominador = 0)\n", 'error')
    except ValueError as e:
        entry_cociente.config(state='normal')
        entry_cociente.delete(0, tk.END)
        entry_cociente.insert(0, "Error")
        entry_cociente.config(state='readonly')
        escribir(f"EXCEPCION: Valor invalido - {e}\n", 'error')
    finally:
        escribir("Ingresando al primer finally\n", 'finally_')

    # ── Segundo bloque try: objeto nulo ───────────────────────────────────────
    escribir("\n" + "=" * 48 + "\n", 'sep')
    escribir(" SEGUNDO BLOQUE TRY - Objeto nulo\n", 'titulo')
    escribir("=" * 48 + "\n", 'sep')
    try:
        escribir("Ingresando al segundo try\n", 'normal')
        objeto = None
        objeto.algun_metodo()                    # AttributeError
        escribir("Imprimiendo objeto\n", 'normal')
    except ZeroDivisionError:
        escribir("EXCEPCION: Division por cero\n", 'error')
    except Exception as e:
        escribir(f"EXCEPCION: {type(e).__name__} - {e}\n", 'error')
    finally:
        escribir("Ingresando al segundo finally\n", 'finally_')

    escribir("\nEjecucion completada.\n", 'ok')
    area_texto.config(state='disabled')


def limpiar():
    entry_numerador.delete(0, tk.END)
    entry_denominador.delete(0, tk.END)
    entry_cociente.config(state='normal')
    entry_cociente.delete(0, tk.END)
    entry_cociente.config(state='readonly')
    area_texto.config(state='normal')
    area_texto.delete('1.0', tk.END)
    area_texto.config(state='disabled')
    entry_numerador.focus()


def escribir(texto, tag):
    area_texto.insert(tk.END, texto, tag)


# ── Ventana principal ──────────────────────────────────────────────────────────
ventana = tk.Tk()
ventana.title("Prueba de Excepciones en Python")
ventana.geometry("620x620")
ventana.resizable(False, False)
ventana.configure(bg='#2B2B2B')

tk.Label(ventana, text="Manejo de Excepciones",
         bg='#2B2B2B', fg='#E0E0E0', font=('Arial', 16, 'bold')).pack(pady=(18, 2))
tk.Label(ventana, text="try / except / finally",
         bg='#2B2B2B', fg='#888888', font=('Arial', 10)).pack(pady=(0, 14))

# ── Campos: Numerador, Denominador, Cociente ───────────────────────────────────
frame_inputs = tk.Frame(ventana, bg='#2B2B2B')
frame_inputs.pack(padx=24, fill='x')

def campo(parent, label, readonly=False):
    f = tk.Frame(parent, bg='#2B2B2B')
    f.pack(side='left', expand=True, fill='x', padx=5)
    tk.Label(f, text=label, bg='#2B2B2B', fg='#AAAAAA', font=('Arial', 9)).pack(anchor='w')
    e = tk.Entry(f, font=('Arial', 13), bg='#1E1E1E' if readonly else '#3C3C3C',
                 fg='#4EC9B0' if readonly else 'white',
                 insertbackground='white', relief='flat', justify='center', bd=6,
                 state='readonly' if readonly else 'normal',
                 readonlybackground='#1E1E1E')
    e.pack(fill='x', ipady=7)
    return e

entry_numerador   = campo(frame_inputs, "Numerador")
tk.Label(frame_inputs, text="/", bg='#2B2B2B', fg='#666',
         font=('Arial', 20)).pack(side='left', pady=(16,0))
entry_denominador = campo(frame_inputs, "Denominador")
tk.Label(frame_inputs, text="=", bg='#2B2B2B', fg='#666',
         font=('Arial', 20)).pack(side='left', pady=(16,0))
entry_cociente    = campo(frame_inputs, "Cociente", readonly=True)

# ── Area de texto ──────────────────────────────────────────────────────────────
tk.Frame(ventana, height=12, bg='#2B2B2B').pack()
frame_texto = tk.Frame(ventana, bg='#1E1E1E')
frame_texto.pack(padx=24, fill='both', expand=True)

area_texto = tk.Text(frame_texto, bg='#1E1E1E', fg='#D4D4D4',
                     font=('Courier New', 11), state='disabled',
                     relief='flat', padx=10, pady=8, wrap='word', height=15)
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

tk.Button(frame_botones, text="Ejecutar", command=ejecutar_prueba,
          bg='#0E639C', fg='white', font=('Arial', 11, 'bold'),
          relief='flat', padx=22, pady=8, cursor='hand2',
          activebackground='#1177BB', activeforeground='white').pack(side='left', padx=8)

tk.Button(frame_botones, text="Limpiar", command=limpiar,
          bg='#3C3C3C', fg='#CCCCCC', font=('Arial', 11),
          relief='flat', padx=22, pady=8, cursor='hand2',
          activebackground='#505050', activeforeground='white').pack(side='left', padx=8)

ventana.bind('<Return>', lambda e: ejecutar_prueba())
entry_numerador.focus()
ventana.mainloop()