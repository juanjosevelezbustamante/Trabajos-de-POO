import tkinter as tk
import math

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un numero positivo para calcular el logaritmo.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError("El valor debe ser un numero positivo para calcular la raiz cuadrada.")
        return math.sqrt(valor)


def calcular():
    area_texto.config(state='normal')
    area_texto.delete('1.0', tk.END)
    valor_str = entry_valor.get().strip()

    escribir("=" * 50 + "\n", 'sep')
    escribir(" CALCULOS NUMERICOS\n", 'titulo')
    escribir("=" * 50 + "\n", 'sep')

    # ── Logaritmo Neperiano ───────────────────────────────────────────────────
    escribir("\n--- Logaritmo Neperiano (ln) ---\n", 'subtitulo')
    try:
        if valor_str == "":
            raise ValueError("Debe ingresar un valor numerico.")
        valor = float(valor_str)
        resultado_log = CalculosNumericos.calcular_logaritmo_neperiano(valor)
        entry_log.config(state='normal')
        entry_log.delete(0, tk.END)
        entry_log.insert(0, f"{resultado_log:.6f}")
        entry_log.config(state='readonly')
        escribir(f"Valor     = {valor}\n", 'normal')
        escribir(f"Resultado = {resultado_log:.6f}\n", 'ok')
    except ArithmeticError as e:
        entry_log.config(state='normal'); entry_log.delete(0, tk.END)
        entry_log.insert(0, "Error"); entry_log.config(state='readonly')
        escribir(f"EXCEPCION ArithmeticError:\n  {e}\n", 'error')
    except ValueError as e:
        entry_log.config(state='normal'); entry_log.delete(0, tk.END)
        entry_log.insert(0, "Error"); entry_log.config(state='readonly')
        escribir(f"EXCEPCION ValueError:\n  {e}\n", 'error')

    # ── Raiz Cuadrada ─────────────────────────────────────────────────────────
    escribir("\n--- Raiz Cuadrada (sqrt) ---\n", 'subtitulo')
    try:
        if valor_str == "":
            raise ValueError("Debe ingresar un valor numerico.")
        valor = float(valor_str)
        resultado_sqrt = CalculosNumericos.calcular_raiz_cuadrada(valor)
        entry_sqrt.config(state='normal')
        entry_sqrt.delete(0, tk.END)
        entry_sqrt.insert(0, f"{resultado_sqrt:.6f}")
        entry_sqrt.config(state='readonly')
        escribir(f"Valor     = {valor}\n", 'normal')
        escribir(f"Resultado = {resultado_sqrt:.6f}\n", 'ok')
    except ArithmeticError as e:
        entry_sqrt.config(state='normal'); entry_sqrt.delete(0, tk.END)
        entry_sqrt.insert(0, "Error"); entry_sqrt.config(state='readonly')
        escribir(f"EXCEPCION ArithmeticError:\n  {e}\n", 'error')
    except ValueError as e:
        entry_sqrt.config(state='normal'); entry_sqrt.delete(0, tk.END)
        entry_sqrt.insert(0, "Error"); entry_sqrt.config(state='readonly')
        escribir(f"EXCEPCION ValueError:\n  {e}\n", 'error')

    escribir("\n" + "=" * 50 + "\n", 'sep')
    escribir("Proceso finalizado.\n", 'finally_')
    area_texto.config(state='disabled')


def limpiar():
    entry_valor.delete(0, tk.END)
    for e in [entry_log, entry_sqrt]:
        e.config(state='normal'); e.delete(0, tk.END); e.config(state='readonly')
    area_texto.config(state='normal')
    area_texto.delete('1.0', tk.END)
    area_texto.config(state='disabled')
    entry_valor.focus()


def escribir(texto, tag):
    area_texto.insert(tk.END, texto, tag)


# ── Ventana principal ──────────────────────────────────────────────────────────
ventana = tk.Tk()
ventana.title("Calculos Numericos")
ventana.geometry("620x660")
ventana.resizable(False, False)
ventana.configure(bg='#2B2B2B')

tk.Label(ventana, text="Calculos Numericos",
         bg='#2B2B2B', fg='#E0E0E0', font=('Arial', 16, 'bold')).pack(pady=(18, 2))
tk.Label(ventana, text="Logaritmo Neperiano y Raiz Cuadrada",
         bg='#2B2B2B', fg='#888888', font=('Arial', 10)).pack(pady=(0, 16))

# ── Entrada ────────────────────────────────────────────────────────────────────
frame_entrada = tk.Frame(ventana, bg='#2B2B2B')
frame_entrada.pack(padx=28, fill='x', pady=4)
tk.Label(frame_entrada, text="Valor", bg='#2B2B2B', fg='#AAAAAA',
         font=('Arial', 9), width=12, anchor='w').pack(side='left')
entry_valor = tk.Entry(frame_entrada, font=('Arial', 13), bg='#3C3C3C', fg='white',
                       insertbackground='white', relief='flat', bd=6, justify='center')
entry_valor.pack(side='left', fill='x', expand=True, ipady=7)

# ── Resultados ─────────────────────────────────────────────────────────────────
def resultado_row(label):
    f = tk.Frame(ventana, bg='#2B2B2B')
    f.pack(padx=28, fill='x', pady=4)
    tk.Label(f, text=label, bg='#2B2B2B', fg='#AAAAAA',
             font=('Arial', 9), width=12, anchor='w').pack(side='left')
    e = tk.Entry(f, font=('Arial', 13), bg='#1E1E1E', fg='#4EC9B0',
                 relief='flat', bd=6, justify='center', state='readonly',
                 readonlybackground='#1E1E1E')
    e.pack(side='left', fill='x', expand=True, ipady=7)
    return e

entry_log  = resultado_row("ln (valor)")
entry_sqrt = resultado_row("sqrt (valor)")

# ── Area de texto ──────────────────────────────────────────────────────────────
tk.Frame(ventana, height=10, bg='#2B2B2B').pack()
frame_texto = tk.Frame(ventana, bg='#1E1E1E')
frame_texto.pack(padx=28, fill='both', expand=True)

area_texto = tk.Text(frame_texto, bg='#1E1E1E', fg='#D4D4D4',
                     font=('Courier New', 11), state='disabled',
                     relief='flat', padx=10, pady=8, wrap='word', height=13)
area_texto.pack(fill='both', expand=True)

area_texto.tag_config('normal',   foreground='#D4D4D4')
area_texto.tag_config('error',    foreground='#F44747', font=('Courier New', 11, 'bold'))
area_texto.tag_config('finally_', foreground='#DCDCAA')
area_texto.tag_config('titulo',   foreground='#569CD6', font=('Courier New', 11, 'bold'))
area_texto.tag_config('subtitulo',foreground='#9CDCFE', font=('Courier New', 10, 'bold'))
area_texto.tag_config('sep',      foreground='#555555')
area_texto.tag_config('ok',       foreground='#4EC9B0', font=('Courier New', 11, 'bold'))

# ── Botones ────────────────────────────────────────────────────────────────────
frame_botones = tk.Frame(ventana, bg='#2B2B2B')
frame_botones.pack(pady=14)

tk.Button(frame_botones, text="Calcular", command=calcular,
          bg='#0E639C', fg='white', font=('Arial', 11, 'bold'),
          relief='flat', padx=22, pady=8, cursor='hand2',
          activebackground='#1177BB', activeforeground='white').pack(side='left', padx=8)

tk.Button(frame_botones, text="Limpiar", command=limpiar,
          bg='#3C3C3C', fg='#CCCCCC', font=('Arial', 11),
          relief='flat', padx=22, pady=8, cursor='hand2',
          activebackground='#505050', activeforeground='white').pack(side='left', padx=8)

ventana.bind('<Return>', lambda e: calcular())
entry_valor.focus()
ventana.mainloop()