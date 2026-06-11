import tkinter as tk
from tkinter import ttk


# ── Clases de dominio ──────────────────────────────────────────────────────────
class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class EquipoMaratonProgramacion:
    MAX = 3

    def __init__(self, nombre_equipo, universidad, lenguaje):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.programadores = []
        self.tamano_equipo = 0

    def esta_lleno(self):
        return self.tamano_equipo == self.MAX

    def agregar(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo esta completo. No se pudo agregar programador.")
        self.programadores.append(programador)
        self.tamano_equipo += 1

    @staticmethod
    def validar_campo(campo):
        for c in campo:
            if c.isdigit():
                raise Exception("El nombre no puede tener digitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")
        if len(campo) == 0:
            raise Exception("El campo no puede estar vacio.")


# ── App GUI ────────────────────────────────────────────────────────────────────
class EquipoApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Equipo Maraton de Programacion")
        self.ventana.geometry("680x760")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg='#2B2B2B')

        self.equipo = None

        self._build_ui()

    def _build_ui(self):
        # Titulo
        tk.Label(self.ventana, text="Equipo Maraton de Programacion",
                 bg='#2B2B2B', fg='#E0E0E0', font=('Arial', 15, 'bold')).pack(pady=(16,2))
        tk.Label(self.ventana, text="Registro de equipo y validacion de integrantes",
                 bg='#2B2B2B', fg='#888888', font=('Arial', 9)).pack(pady=(0,12))

        # ── Datos del equipo ───────────────────────────────────────────────────
        frm_equipo = tk.LabelFrame(self.ventana, text=" Datos del Equipo ",
                                   bg='#2B2B2B', fg='#9CDCFE',
                                   font=('Arial', 9, 'bold'), bd=1, relief='groove')
        frm_equipo.pack(padx=24, fill='x', pady=4)

        self.entry_nombre_equipo  = self._campo(frm_equipo, "Nombre del equipo")
        self.entry_universidad     = self._campo(frm_equipo, "Universidad")
        self.entry_lenguaje        = self._campo(frm_equipo, "Lenguaje")

        # ── Integrantes ────────────────────────────────────────────────────────
        frm_prog = tk.LabelFrame(self.ventana, text=" Integrantes (max. 3) ",
                                  bg='#2B2B2B', fg='#9CDCFE',
                                  font=('Arial', 9, 'bold'), bd=1, relief='groove')
        frm_prog.pack(padx=24, fill='x', pady=4)

        self.integrantes = []
        for i in range(3):
            tk.Label(frm_prog, text=f"Integrante {i+1}",
                     bg='#2B2B2B', fg='#569CD6',
                     font=('Arial', 8, 'bold')).grid(row=i*2, column=0, columnspan=2,
                                                      sticky='w', padx=10, pady=(6,0))
            e_nom = self._campo_grid(frm_prog, "Nombre", row=i*2+1, col=0)
            e_ape = self._campo_grid(frm_prog, "Apellidos", row=i*2+1, col=2)
            self.integrantes.append((e_nom, e_ape))

        frm_prog.columnconfigure(1, weight=1)
        frm_prog.columnconfigure(3, weight=1)

        # ── Area de consola ────────────────────────────────────────────────────
        tk.Frame(self.ventana, height=8, bg='#2B2B2B').pack()
        frm_txt = tk.Frame(self.ventana, bg='#1E1E1E')
        frm_txt.pack(padx=24, fill='both', expand=True)

        self.area_texto = tk.Text(frm_txt, bg='#1E1E1E', fg='#D4D4D4',
                                   font=('Courier New', 10), state='disabled',
                                   relief='flat', padx=10, pady=8, wrap='word', height=10)
        self.area_texto.pack(fill='both', expand=True)

        self.area_texto.tag_config('normal',    foreground='#D4D4D4')
        self.area_texto.tag_config('error',     foreground='#F44747', font=('Courier New',10,'bold'))
        self.area_texto.tag_config('finally_',  foreground='#DCDCAA')
        self.area_texto.tag_config('titulo',    foreground='#569CD6', font=('Courier New',10,'bold'))
        self.area_texto.tag_config('subtitulo', foreground='#9CDCFE', font=('Courier New',10,'bold'))
        self.area_texto.tag_config('sep',       foreground='#555555')
        self.area_texto.tag_config('ok',        foreground='#4EC9B0', font=('Courier New',10,'bold'))

        # ── Botones ────────────────────────────────────────────────────────────
        frm_btn = tk.Frame(self.ventana, bg='#2B2B2B')
        frm_btn.pack(pady=12)

        tk.Button(frm_btn, text="Registrar equipo", command=self.registrar,
                  bg='#0E639C', fg='white', font=('Arial', 11, 'bold'),
                  relief='flat', padx=20, pady=7, cursor='hand2',
                  activebackground='#1177BB').pack(side='left', padx=8)

        tk.Button(frm_btn, text="Limpiar", command=self.limpiar,
                  bg='#3C3C3C', fg='#CCCCCC', font=('Arial', 11),
                  relief='flat', padx=20, pady=7, cursor='hand2',
                  activebackground='#505050').pack(side='left', padx=8)

        self.ventana.bind('<Return>', lambda e: self.registrar())

    def _campo(self, parent, label):
        f = tk.Frame(parent, bg='#2B2B2B')
        f.pack(fill='x', padx=10, pady=4)
        tk.Label(f, text=label, bg='#2B2B2B', fg='#AAAAAA',
                 font=('Arial', 9), width=14, anchor='w').pack(side='left')
        e = tk.Entry(f, font=('Arial', 11), bg='#3C3C3C', fg='white',
                     insertbackground='white', relief='flat', bd=5)
        e.pack(side='left', fill='x', expand=True, ipady=5)
        return e

    def _campo_grid(self, parent, label, row, col):
        tk.Label(parent, text=label, bg='#2B2B2B', fg='#AAAAAA',
                 font=('Arial', 9), anchor='w').grid(row=row, column=col,
                                                      sticky='w', padx=(10,2), pady=3)
        e = tk.Entry(parent, font=('Arial', 11), bg='#3C3C3C', fg='white',
                     insertbackground='white', relief='flat', bd=5, width=18)
        e.grid(row=row, column=col+1, sticky='ew', padx=(0,10), pady=3, ipady=5)
        return e

    def escribir(self, texto, tag='normal'):
        self.area_texto.insert(tk.END, texto, tag)

    def registrar(self):
        self.area_texto.config(state='normal')
        self.area_texto.delete('1.0', tk.END)

        self.escribir("=" * 52 + "\n", 'sep')
        self.escribir(" REGISTRO DE EQUIPO\n", 'titulo')
        self.escribir("=" * 52 + "\n", 'sep')

        try:
            # Validar datos del equipo
            nom_eq = self.entry_nombre_equipo.get().strip()
            univ   = self.entry_universidad.get().strip()
            leng   = self.entry_lenguaje.get().strip()

            for campo, etiqueta in [(nom_eq,'Nombre equipo'),(univ,'Universidad'),(leng,'Lenguaje')]:
                EquipoMaratonProgramacion.validar_campo(campo)

            self.equipo = EquipoMaratonProgramacion(nom_eq, univ, leng)
            self.escribir(f"Equipo     : {nom_eq}\n", 'ok')
            self.escribir(f"Universidad: {univ}\n", 'ok')
            self.escribir(f"Lenguaje   : {leng}\n\n", 'ok')

            # Agregar integrantes
            self.escribir("--- Integrantes ---\n", 'subtitulo')
            for i, (e_nom, e_ape) in enumerate(self.integrantes):
                nombre_p    = e_nom.get().strip()
                apellidos_p = e_ape.get().strip()
                EquipoMaratonProgramacion.validar_campo(nombre_p)
                EquipoMaratonProgramacion.validar_campo(apellidos_p)
                programador = Programador(nombre_p, apellidos_p)
                self.equipo.agregar(programador)
                self.escribir(f"  [{i+1}] {programador}\n", 'normal')

            self.escribir(f"\nTamano del equipo: {self.equipo.tamano_equipo}/{self.equipo.MAX}\n", 'ok')
            self.escribir("Equipo registrado correctamente.\n", 'ok')

        except Exception as e:
            self.escribir(f"EXCEPCION: {e}\n", 'error')
        finally:
            self.escribir("=" * 52 + "\n", 'sep')
            self.escribir("Proceso finalizado.\n", 'finally_')

        self.area_texto.config(state='disabled')

    def limpiar(self):
        for entry in [self.entry_nombre_equipo, self.entry_universidad, self.entry_lenguaje]:
            entry.delete(0, tk.END)
        for e_nom, e_ape in self.integrantes:
            e_nom.delete(0, tk.END)
            e_ape.delete(0, tk.END)
        self.area_texto.config(state='normal')
        self.area_texto.delete('1.0', tk.END)
        self.area_texto.config(state='disabled')
        self.equipo = None
        self.entry_nombre_equipo.focus()


# ── Main ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    ventana = tk.Tk()
    app = EquipoApp(ventana)
    ventana.mainloop()