import math
import tkinter as tk
from tkinter import messagebox

#CLASE NOTAS
class Notas:
    def __init__(self):
        # Atributo: listaNotas (array de doubles)
        self.listaNotas = [0.0] * 5

    def calcularPromedio(self):
        return sum(self.listaNotas) / len(self.listaNotas)

    def calcularDesviación(self):
        prom = self.calcularPromedio()
        suma = sum(math.pow(nota - prom, 2) for nota in self.listaNotas)
        return math.sqrt(suma / len(self.listaNotas))

    def calcularMenor(self):
        return min(self.listaNotas)

    def calcularMayor(self):
        return max(self.listaNotas)


#CLASE VENTANAPRINCIPAL
class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        # Según el diagrama, estos son sus atributos (labels, textfields, buttons)
        self.nota1 = self.nota2 = self.nota3 = self.nota4 = self.nota5 = None
        self.campoNota1 = self.campoNota2 = self.campoNota3 = self.campoNota4 = self.campoNota5 = None
        self.promedio = self.desviación = self.mayor = self.menor = None
        self.calcular = self.limpiar = None
        
        # Configuración de ventana (similar a JFrame)
        self.root.title("Notas")
        self.root.geometry("280x380")
        self.root.resizable(False, False)
        
        self._inicio() # Llamada al método privado de inicialización

    def _inicio(self):
        """Método para inicializar los componentes gráficos (Equivalente a inicio())"""
        #Notas y campos de texto
        etiquetas_texto = ["Nota 1:", "Nota 2:", "Nota 3:", "Nota 4:", "Nota 5:"]
        self.campos = [] # Para facilitar el acceso en bucle

        for i in range(5):
            lbl = tk.Label(self.root, text=etiquetas_texto[i])
            lbl.place(x=20, y=20 + (i * 30), width=135, height=23)
            
            txt = tk.Entry(self.root)
            txt.place(x=105, y=20 + (i * 30), width=135, height=23)
            self.campos.append(txt)

        #Botones (Equivalente a JButton)
        self.calcular = tk.Button(self.root, text="Calcular", command=self.actionPerformed)
        self.calcular.place(x=20, y=170, width=100, height=23)

        self.limpiar = tk.Button(self.root, text="Limpiar", command=self.limpiar_campos)
        self.limpiar.place(x=125, y=170, width=80, height=23)

        #Etiquetas de resultados
        self.promedio = tk.Label(self.root, text="Promedio =", anchor="w")
        self.promedio.place(x=20, y=210, width=135, height=23)

        self.desviación = tk.Label(self.root, text="Desviación =", anchor="w")
        self.desviación.place(x=20, y=240, width=200, height=23)

        self.mayor = tk.Label(self.root, text="Nota mayor =", anchor="w")
        self.mayor.place(x=20, y=270, width=120, height=23)

        self.menor = tk.Label(self.root, text="Nota menor =", anchor="w")
        self.menor.place(x=20, y=300, width=120, height=23)

    def actionPerformed(self):
        """Gestiona los eventos (Equivalente al ActionListener de Java)"""
        try:
            notas_obj = Notas()
            for i in range(5):
                valor = float(self.campos[i].get())
                notas_obj.listaNotas[i] = valor

            #Actualización de etiquetas
            self.promedio.config(text=f"Promedio = {notas_obj.calcularPromedio():.2f}")
            self.desviación.config(text=f"Desviación estándar = {notas_obj.calcularDesviación():.2f}")
            self.mayor.config(text=f"Valor mayor = {notas_obj.calcularMayor()}")
            self.menor.config(text=f"Valor menor = {notas_obj.calcularMenor()}")
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos.")

    def limpiar_campos(self):
        for campo in self.campos:
            campo.delete(0, tk.END)


#CLASE PRINCIPAL
class Principal:
    @staticmethod
    def main():
        root = tk.Tk()
        # Relación 1 a 1: Principal crea la VentanaPrincipal
        miVentanaPrincipal = VentanaPrincipal(root)
        root.mainloop()

#Ejecución del programa
if __name__ == "__main__":
    Principal.main()