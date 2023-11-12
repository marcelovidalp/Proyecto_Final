import random
from tkinter import *

class S_Ecosistema:
    def __init__(self, filas, columnas):
        self.nFilas = filas
        self.nColumnas = columnas
        self.matriz = [[0] * columnas for _ in range(filas)]
    
    def interfaz(self):
        ventana = Tk()
        res_ancho = ventana.winfo_screenwidth()
        res_alto = ventana.winfo_screenheight()
        ventana.geometry(f"{res_ancho}x{res_alto}")
        ventana.title("Ecosimulador.")
        ventana.config(bg="midnight blue")
        #creacion de la matriz en la ventana
        canvas = Canvas(ventana, width=800, height=600)
        canvas.pack()
        ancho_celda = 60
        alto_celda = 60
        for i in range(self.nFilas):
            for j in range(self.nColumnas):
                x1 = j * ancho_celda
                y1 = i * alto_celda
                x2 = x1 * ancho_celda
                y2 = y1 * alto_celda
                canvas.create_rectangle(x1, y1, x2, y2, fill=self.colorCelda(self.matriz[i][j]))
        ventana.mainloop()
        
    def colorCelda(self, valor):
        if valor == 0:
            return "white"
        elif valor == 1:
            return "green"
        elif valor == 2:
            return "red"
        elif valor == 3:
            return "black"

class Leopardo(S_Ecosistema):
    def __init__(self):
        super().__init__()
        pass
    
    def movimiento(self):
        pass
        
    
    def cazar(self):
        pass
    
class Gacelas(S_Ecosistema):
    def __init__(self):
        super().__init__(self)
        pass
    
    def muerte(self):
        pass
    
    def movimiento(self):
        pass

class Plantas(S_Ecosistema):
    def __init__(self):
        super().__init__(self)
        pass
    
    def movimiento(self):
        pass

Simulador = S_Ecosistema(40, 40)
for i in range(Simulador.nFilas):
    for j in range(Simulador.nColumnas):
        Simulador.matriz[i][j] = random.choice([0, 1, 2, 3])
    
Simulador.interfaz()
