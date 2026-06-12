import tkinter as tk
from tkinter import filedialog


class LeerArchivo:
    @staticmethod
    def leer(ruta):
        lineas = []
        with open(ruta, 'r', encoding='utf-8', errors='replace') as archivo:
            for linea in archivo:
                lineas.append(linea.rstrip('\n'))
        return lineas


class LeerArchivoApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Leer Archivo de Texto")
        self.ventana.geometry("700x560")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg='#2B2B2B')
        self._build_ui()

    def _build_ui(self):
        # Titulo
        tk.Label(self.ventana, text="Leer Archivo de Texto",
                 bg='#2B2B2B', fg='#E0E0E0',
                 font=('Arial', 16, 'bold')).pack(pady=(18, 2))
        tk.Label(self.ventana, text="Lectura de archivos con manejo de excepciones",
                 bg='#2B2B2B', fg='#888888',
                 font=('Arial', 10)).pack(pady=(0, 14))

        # ── Fila: ruta + botón examinar ───────────────────────────────────────
        frm_ruta = tk.Frame(self.ventana, bg='#2B2B2B')
        frm_ruta.pack(padx=24, fill='x')

        tk.Label(frm_ruta, text="Ruta del archivo",
                 bg='#2B2B2B', fg='#AAAAAA',
                 font=('Arial', 9), width=14, anchor='w').pack(side='left')

        self.entry_ruta = tk.Entry(frm_ruta, font=('Arial', 11),
                                   bg='#3C3C3C', fg='white',
                                   insertbackground='white',
                                   relief='flat', bd=6)
        self.entry_ruta.pack(side='left', fill='x', expand=True, ipady=6)

        tk.Button(frm_ruta, text="Examinar...", command=self.examinar,
                  bg='#3C3C3C', fg='#CCCCCC', font=('Arial', 9),
                  relief='flat', padx=10, pady=6, cursor='hand2',
                  activebackground='#505050').pack(side='left', padx=(6, 0))

        # ── Area de contenido del archivo ─────────────────────────────────────
        tk.Label(self.ventana, text="Contenido del archivo",
                 bg='#2B2B2B', fg='#9CDCFE',
                 font=('Arial', 9, 'bold')).pack(anchor='w', padx=28, pady=(14, 2))

        frm_contenido = tk.Frame(self.ventana, bg='#1E1E1E')
        frm_contenido.pack(padx=24, fill='both', expand=True)

        scroll_y = tk.Scrollbar(frm_contenido, orient='vertical')
        scroll_y.pack(side='right', fill='y')

        self.area_contenido = tk.Text(
            frm_contenido, bg='#1E1E1E', fg='#D4D4D4',
            font=('Courier New', 11), state='disabled',
            relief='flat', padx=10, pady=8, wrap='none',
            yscrollcommand=scroll_y.set)
        self.area_contenido.pack(fill='both', expand=True)
        scroll_y.config(command=self.area_contenido.yview)

        self.area_contenido.tag_config('linea',   foreground='#D4D4D4')
        self.area_contenido.tag_config('error',   foreground='#F44747',
                                       font=('Courier New', 11, 'bold'))
        self.area_contenido.tag_config('info',    foreground='#9CDCFE')
        self.area_contenido.tag_config('ok',      foreground='#4EC9B0',
                                       font=('Courier New', 11, 'bold'))
        self.area_contenido.tag_config('finally_',foreground='#DCDCAA')
        self.area_contenido.tag_config('sep',     foreground='#555555')
        self.area_contenido.tag_config('num',     foreground='#858585')

        # ── Barra de estado ───────────────────────────────────────────────────
        self.lbl_estado = tk.Label(self.ventana, text="Sin archivo cargado.",
                                   bg='#252526', fg='#888888',
                                   font=('Arial', 9), anchor='w')
        self.lbl_estado.pack(fill='x', padx=0, pady=(6, 0))

        # ── Botones ───────────────────────────────────────────────────────────
        frm_btn = tk.Frame(self.ventana, bg='#2B2B2B')
        frm_btn.pack(pady=12)

        tk.Button(frm_btn, text="Leer archivo", command=self.leer,
                  bg='#0E639C', fg='white', font=('Arial', 11, 'bold'),
                  relief='flat', padx=22, pady=8, cursor='hand2',
                  activebackground='#1177BB').pack(side='left', padx=8)

        tk.Button(frm_btn, text="Limpiar", command=self.limpiar,
                  bg='#3C3C3C', fg='#CCCCCC', font=('Arial', 11),
                  relief='flat', padx=22, pady=8, cursor='hand2',
                  activebackground='#505050').pack(side='left', padx=8)

        self.ventana.bind('<Return>', lambda e: self.leer())

    def examinar(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"),
                       ("Todos los archivos", "*.*")])
        if ruta:
            self.entry_ruta.delete(0, tk.END)
            self.entry_ruta.insert(0, ruta)

    def escribir(self, texto, tag='linea'):
        self.area_contenido.insert(tk.END, texto, tag)

    def leer(self):
        self.area_contenido.config(state='normal')
        self.area_contenido.delete('1.0', tk.END)

        ruta = self.entry_ruta.get().strip()

        self.escribir("=" * 52 + "\n", 'sep')
        self.escribir(" LECTURA DE ARCHIVO\n", 'info')
        self.escribir("=" * 52 + "\n", 'sep')

        try:
            if not ruta:
                raise IOError("Debe ingresar o seleccionar la ruta del archivo.")

            self.escribir(f"Archivo : {ruta}\n\n", 'info')
            lineas = LeerArchivo.leer(ruta)

            if not lineas:
                self.escribir("(El archivo esta vacio)\n", 'finally_')
            else:
                for i, linea in enumerate(lineas, start=1):
                    self.escribir(f"{i:>4} ", 'num')
                    self.escribir(f"{linea}\n", 'linea')

            self.escribir(f"\nTotal de lineas leidas: {len(lineas)}\n", 'ok')
            self.lbl_estado.config(
                text=f"Archivo cargado: {ruta}  |  {len(lineas)} lineas",
                fg='#4EC9B0')

        except IOError as e:
            self.escribir(f"EXCEPCION IOException:\n  {e}\n", 'error')
            self.lbl_estado.config(text=f"Error: {e}", fg='#F44747')
        except Exception as e:
            self.escribir(f"EXCEPCION {type(e).__name__}:\n  {e}\n", 'error')
            self.lbl_estado.config(text=f"Error inesperado: {e}", fg='#F44747')
        finally:
            self.escribir("=" * 52 + "\n", 'sep')
            self.escribir("Proceso finalizado.\n", 'finally_')

        self.area_contenido.config(state='disabled')

    def limpiar(self):
        self.entry_ruta.delete(0, tk.END)
        self.area_contenido.config(state='normal')
        self.area_contenido.delete('1.0', tk.END)
        self.area_contenido.config(state='disabled')
        self.lbl_estado.config(text="Sin archivo cargado.", fg='#888888')
        self.entry_ruta.focus()


if __name__ == "__main__":
    ventana = tk.Tk()
    app = LeerArchivoApp(ventana)
    ventana.mainloop()