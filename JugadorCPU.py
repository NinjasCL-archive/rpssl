#!/usr/bin/ python
from Jugador import *
import random
class JugadorCPU(Jugador):
    def __init__(self):
      Jugador.__init__(self,'CPU')
      self.level = 0 
      self.eleccion = 0

    def __str__(self):
        return Jugador.__str__(self)
        
    def realizarEleccion(self):
        if self.level == 0:
            self.eleccion_aleatoria()
    
    def eleccion_aleatoria(self):
        self.eleccion = random.randint(1,5)

            
