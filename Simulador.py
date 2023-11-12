import random
from tkinter import *
from PIL import Image, ImageTk

class S_Ecosistema:
    def __init__(self, filas, columnas):
        self.nFilas = filas
        self.nColumnas = columnas
        self.matriz = [[0] * columnas for _ in range(filas)]
        self.canvas = None
    
    def interfaz(self):
        ventana = Tk()
        res_ancho = ventana.winfo_screenwidth()
        res_alto = ventana.winfo_screenheight()
        ventana.geometry(f"{res_ancho}x{res_alto}")
        ventana.title("Ecosimulador.")
        ventana.config(bg="midnight blue")
        #Frame1
        frame1 = Frame(ventana,height=1100, width=400, bg="royal blue")
        frame1.pack(side=LEFT)
        #creacion de la matriz en la ventana
        canvas = Canvas(ventana, width=res_ancho-400, height=res_alto, bg="midnight blue")
        canvas.pack(side=RIGHT)
        ancho_celda = (res_ancho-400) // self.nColumnas
        alto_celda = res_alto // self.nFilas
        
        for i in range(self.nFilas):
            for j in range(self.nColumnas):
                x1 = j * ancho_celda
                y1 = i * alto_celda
                x2 = (i+1) * ancho_celda
                y2 = (j+1) * alto_celda
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
        super().__init__(50, 50)
        pass
    
    def movimiento(self):
        pass
        
    def cazar(self):
        pass
    
class Gacelas(S_Ecosistema):
    def __init__(self):
        super().__init__(50, 50)
        pass
    
    def muerte(self):
        pass
    
    def movimiento(self):
        pass

class Plantas(S_Ecosistema):
    def __init__(self,fila, columna, ruta_img):
        super().__init__(50, 50)
        self.fila = fila
        self.columna = columna
        self.ruta_img = ruta_img
    
    def accion(self, canvas):
        if canvas is not None:
            imagen =  Image.open(self.ruta_img)
            imagen =  ImageTk.PhotoImage(imagen)
            self.canvas.create_image(self.columna * self.ancho_celda, self.fila * self.alto_celda, anchor=NW, image=imagen) 
        else:
            print("Error, el canvas no ha sido correctamente inicializado")
Simulador = S_Ecosistema(50, 50)
for i in range(Simulador.nFilas):
    for j in range(Simulador.nColumnas):
        Simulador.matriz[i][j] = random.choice([0, 1, 2, 3])
        
planta = Plantas(fila= 2, columna = 2, ruta_img="Escritorio/arbustopixel(1).png")
planta.accion(Simulador.canvas)
Simulador.interfaz()
