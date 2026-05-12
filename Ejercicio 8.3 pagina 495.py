import math
import tkinter as tk
from tkinter import messagebox

#LÓGICA DE NEGOCIO (MODELO)

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcularVolumen()
        self.superficie = self.calcularSuperficie()

    def calcularVolumen(self):
        return math.pi * self.altura * math.pow(self.radio, 2.0)

    def calcularSuperficie(self):
        areaLadoA = 2.0 * math.pi * self.radio * self.altura
        areaLadoB = 2.0 * math.pi * math.pow(self.radio, 2.0)
        return areaLadoA + areaLadoB

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.volumen = self.calcularVolumen()
        self.superficie = self.calcularSuperficie()

    def calcularVolumen(self):
        return 1.333 * math.pi * math.pow(self.radio, 3.0)

    def calcularSuperficie(self):
        return 4.0 * math.pi * math.pow(self.radio, 2.0)

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcularVolumen()
        self.superficie = self.calcularSuperficie()

    def calcularVolumen(self):
        return (math.pow(self.base, 2.0) * self.altura) / 3.0

    def calcularSuperficie(self):
        areaBase = math.pow(self.base, 2.0)
        areaLado = 2.0 * self.base * self.apotema
        return areaBase + areaLado

#INTERFACES GRÁFICAS (VISTA)

class VentanaCilindro(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)
        self._inicio()

    def _inicio(self):
        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campoRadio = tk.Entry(self)
        self.campoRadio.place(x=120, y=20, width=135)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campoAltura = tk.Entry(self)
        self.campoAltura.place(x=120, y=50, width=135)

        tk.Button(self, text="Calcular", command=self.actionPerformed).place(x=120, y=80, width=135)
        
        self.lblVolumen = tk.Label(self, text="Volumen (cm3):")
        self.lblVolumen.place(x=20, y=110)
        self.lblSuperficie = tk.Label(self, text="Superficie (cm2):")
        self.lblSuperficie.place(x=20, y=140)

    def actionPerformed(self):
        try:
            r = float(self.campoRadio.get())
            h = float(self.campoAltura.get())
            obj = Cilindro(r, h)
            self.lblVolumen.config(text=f"Volumen (cm3): {obj.volumen:.2f}")
            self.lblSuperficie.config(text=f"Superficie (cm2): {obj.superficie:.2f}")
        except:
            messagebox.showerror("Error", "Campo nulo o error en formato")

class VentanaEsfera(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Esfera")
        self.geometry("280x200")
        self._inicio()

    def _inicio(self):
        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campoRadio = tk.Entry(self)
        self.campoRadio.place(x=120, y=20, width=135)

        tk.Button(self, text="Calcular", command=self.actionPerformed).place(x=120, y=50, width=135)
        self.lblVolumen = tk.Label(self, text="Volumen (cm3):")
        self.lblVolumen.place(x=20, y=90)
        self.lblSuperficie = tk.Label(self, text="Superficie (cm2):")
        self.lblSuperficie.place(x=20, y=120)

    def actionPerformed(self):
        try:
            r = float(self.campoRadio.get())
            obj = Esfera(r)
            self.lblVolumen.config(text=f"Volumen (cm3): {obj.volumen:.2f}")
            self.lblSuperficie.config(text=f"Superficie (cm2): {obj.superficie:.2f}")
        except:
            messagebox.showerror("Error", "Error en formato")

class VentanaPiramide(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Pirámide")
        self.geometry("280x240")
        self._inicio()

    def _inicio(self):
        tk.Label(self, text="Base (cms):").place(x=20, y=20)
        self.campoBase = tk.Entry(self)
        self.campoBase.place(x=120, y=20, width=135)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campoAltura = tk.Entry(self)
        self.campoAltura.place(x=120, y=50, width=135)

        tk.Label(self, text="Apotema (cms):").place(x=20, y=80)
        self.campoApotema = tk.Entry(self)
        self.campoApotema.place(x=120, y=80, width=135)

        tk.Button(self, text="Calcular", command=self.actionPerformed).place(x=120, y=110, width=135)
        self.lblVolumen = tk.Label(self, text="Volumen (cm3):")
        self.lblVolumen.place(x=20, y=140)
        self.lblSuperficie = tk.Label(self, text="Superficie (cm2):")
        self.lblSuperficie.place(x=20, y=170)

    def actionPerformed(self):
        try:
            b = float(self.campoBase.get())
            h = float(self.campoAltura.get())
            a = float(self.campoApotema.get())
            obj = Piramide(b, h, a)
            self.lblVolumen.config(text=f"Volumen (cm3): {obj.volumen:.2f}")
            self.lblSuperficie.config(text=f"Superficie (cm2): {obj.superficie:.2f}")
        except:
            messagebox.showerror("Error", "Error en formato")

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x160")
        self.resizable(False, False)
        self._inicio()

    def _inicio(self):
        tk.Button(self, text="Cilindro", command=self.abrirCilindro).place(x=20, y=50, width=80)
        tk.Button(self, text="Esfera", command=self.abrirEsfera).place(x=125, y=50, width=80)
        tk.Button(self, text="Pirámide", command=self.abrirPiramide).place(x=225, y=50, width=100)

    def abrirCilindro(self): VentanaCilindro(self)
    def abrirEsfera(self): VentanaEsfera(self)
    def abrirPiramide(self): VentanaPiramide(self)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()