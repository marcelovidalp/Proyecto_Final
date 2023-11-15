import random
from tkinter import *

class Organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad
    
class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta
        pass
        
    def cazar(self, presas):
        presa_selec = None
        presas_range = [presa for presa in presas if self.cal_distancia(presa) < self.velocidad]
        
        if presas_range:
            presa_selec = random.choice(presas_range)
            self.energia += presa_selec.energia
            presas.remove(presa_selec)
        return presa_selec
    
    def reproducir(self):
        prob_reproduccion = random.uniform(0,1)
        if prob_reproduccion > 0.8:
            descendencia = Animal(self.posicion, vida = 100, energia = 50, 
                                  velocidad = 1, especie = self.especie,
                                  dieta = self.dieta)
            return descendencia
        else:
            return None
        pass
    
class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad):
        super().__init__(posicion, vida, energia, velocidad)
        pass
    
    def fotosintesis(self):
        pass
    
    def reproducir(self):
        pass
    
class Ambiente:
    def __init__(self):
        pass

class Ecosistema:
    def __init__(self):
        self.animales = []
        pass
    
    def cicloVida(self):
        new_animales = []
        for animal in self.animales:
            pareja = random.choice(self.animales)
            descendencia = animal.reproducir(pareja)
            if descendencia:
                new_animales.append(descendencia)
        self.animales.extend(new_animales)
        pass
    
    def cadenaAlimenticia(self):
        pass
    
ecosistema = Ecosistema()

for _ in range(1000):
    ecosistema.cicloVida()
    ecosistema.cadenaAlimenticia()
    