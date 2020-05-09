#!/usr/bin python
class Jugador(object):
    def __init__(self, _nombre):
        self.nombre = _nombre
        self.puntos = 0
        self.derrotas = 0
        self.eleccion = 0
        self.eleccion_str = "Ninguna"
    
    def sumarPunto(self):
        self.puntos += 1
        
    def sumarDerrota(self):
        self.derrotas +=1
        
    
    def __str__(self):
        msg = "%s : %d Wins %d Fails" %(self.nombre,self.puntos,self.derrotas)
        return msg
    
    def eleccion_string(self):
        if self.eleccion == 1:
            self.eleccion_str = "Piedra"
            
        elif self.eleccion == 2:
            self.eleccion_str =  "Papel"
            
        elif self.eleccion == 3:
            self.eleccion_str = "Tijera"
            
        elif self.eleccion == 4:
            self.eleccion_str =  "Lagarto"
            
        elif self.eleccion == 5:
            self.eleccion_str =  "Spock"
