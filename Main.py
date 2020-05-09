#!/usr/bin/ python
from JugadorCPU import *
from Jugador import *

def obtenerResultado(jugador1,jugador2):
    
    jugador1.eleccion_string()
    jugador2.eleccion_string()
    
    print
    
    print "%s uso %s, %s uso %s" %(jugador1.nombre,jugador1.eleccion_str,jugador2.nombre,jugador2.eleccion_str)
    
    print
    
    # Piedra    
    if jugador1.eleccion == 1:
        # Gana contra Tijeras y Lagarto
        if jugador2.eleccion == 3 or jugador2.eleccion == 4:
            jugador1.sumarPunto()
            jugador2.sumarDerrota()
            
            if jugador2.eleccion == 3:
                mensaje = "Piedra Destruye Tijera"
            else:
                mensaje = "Piedra Aplasta Lagarto"
            
            print mensaje
            print "Jugador %s Gana" % jugador1.nombre
            
        # Pierde contra Papel y Spock
        elif jugador2.eleccion == 2 or jugador2.eleccion == 5:
            jugador2.sumarPunto()
            jugador1.sumarDerrota()
            
            if jugador2.eleccion == 2:
                mensaje = "Papel Cubre Piedra"
            else:
                mensaje = "Spock Vaporiza Piedra"
            
            print mensaje
            print "Jugador %s Gana" % jugador2.nombre            
        else:
            print "Empate"
    
    # Papel        
    elif jugador1.eleccion == 2:
        # Gana contra Piedra y Spock
        if jugador2.eleccion == 1 or jugador2.eleccion == 5:
            jugador1.sumarPunto()
            jugador2.sumarDerrota()
            
            if jugador2.eleccion == 1:
                mensaje = "Papel Cubre Piedra"
            else:
                mensaje = "Papel Refuta Spock"
            
            print mensaje
            print "Jugador %s Gana" % jugador1.nombre
            
        # Pierde contra Tijera y Lagarto
        elif jugador2.eleccion == 3 or jugador2.eleccion == 4:
            jugador2.sumarPunto()
            jugador1.sumarDerrota()
            
            if jugador2.eleccion == 3:
                mensaje = "Tijera Corta Papel"
            else:
                mensaje = "Lagarto Come Papel"
            
            print mensaje
            print "Jugador %s Gana" % jugador2.nombre
        else:
            print "Empate"
            
    # Tijeras        
    elif jugador1.eleccion == 3:
        # Gana contra Papel y Lagarto
        if jugador2.eleccion == 2 or jugador2.eleccion == 4:
            jugador1.sumarPunto()
            jugador2.sumarDerrota()
            
            if jugador2.eleccion == 2:
                mensaje = "Tijera Corta Papel"
            else:
                mensaje = "Tijera Decapita Lagarto"
            
            print mensaje
            print "Jugador %s Gana" % jugador1.nombre
            
        # Pierde contra Piedra y Spock
        elif jugador2.eleccion == 1 or jugador2.eleccion == 5:
            jugador2.sumarPunto()
            jugador1.sumarDerrota()
            
            if jugador2.eleccion == 1:
                mensaje = "Piedra Destruye Tijera"
            else:
                mensaje = "Spock Elimina Tijera"
            
            print mensaje
            print "Jugador %s Gana" % jugador2.nombre
        else:
            print "Empate"

    # Lagarto        
    elif jugador1.eleccion == 4:
        # Gana contra Papel y Spock
        if jugador2.eleccion == 2 or jugador2.eleccion == 5:
            jugador1.sumarPunto()
            jugador2.sumarDerrota()
            
            if jugador2.eleccion == 2:
                mensaje = "Lagarto Come Papel"
            else:
                mensaje = "Lagarto Envenena Spock"
            
            print mensaje
            print "Jugador %s Gana" % jugador1.nombre
            
        # Pierde contra Tijeras y Piedra
        elif jugador2.eleccion == 3 or jugador2.eleccion == 1:
            jugador2.sumarPunto()
            jugador1.sumarDerrota()
            
            if jugador2.eleccion == 3:
                mensaje = "Tijeras Decapita Lagarto"
            else:
                mensaje = "Piedra Aplasta Lagarto"
            
            print mensaje
            print "Jugador %s Gana" % jugador2.nombre
        else:
            print "Empate"

    # Spock        
    elif jugador1.eleccion == 5:
        # Gana contra Piedra y Tijeras
        if jugador2.eleccion == 1 or jugador2.eleccion == 3:
            jugador1.sumarPunto()
            jugador2.sumarDerrota()
            
            if jugador2.eleccion == 1:
                mensaje = "Spock Vaporiza Piedra"
            else:
                mensaje = "Spock Elimina Tijera"
            
            print mensaje
            print "Jugador %s Gana" % jugador1.nombre
            
        # Pierde contra Papel y Lagarto
        elif jugador2.eleccion == 2 or jugador2.eleccion == 4:
            jugador2.sumarPunto()
            jugador1.sumarDerrota()
            
            if jugador2.eleccion == 2:
                mensaje = "Papel Refuta Spock"
            else:
                mensaje = "Lagarto Envenena Spock"
            
            print mensaje
            print "Jugador %s Gana" % jugador2.nombre
        else:
            print "Empate"
    
    print
    print
    print jugador1
    print jugador2
    print 
    print
    


print "Bienvenido a piedra papel tijeras lagarto spock!"
yo = Jugador(raw_input("\nIngrese su nombre\n>>"))
pc = JugadorCPU()


# MainLoop
   
while True:
 
    print "Instrucciones: Ingresar los siguientes numeros para jugar"
    print "1 - Piedra"
    print "2 - Papel"
    print "3 - Tijeras"
    print "4 - Lagarto"
    print "5 - Spock!"
    print "0 - Salir"
    
    eleccion = raw_input("\nSiguiente Jugada\n>>")
    
    try:
        eleccion = int(eleccion)
    except:
        pass
        
    pc.realizarEleccion()
    
    if eleccion == 0:
        print "Bye!"
        break
        
    if eleccion in range(1,6):
        yo.eleccion = eleccion
        obtenerResultado(yo,pc)
    else:
        print
        print "Eleccion no valida"
        print 
    
    
