import FuncionesHeuristica as fh
import time

contadorNodos = 0
def esMejorHeuristica (inicial: fh.Tablero, nuevoNodo:fh.Tablero):
    return nuevoNodo.h < inicial.h
            

def EscaladaSimple(inicial:fh.Tablero):
    global contadorNodos
    while(not fh.hemosTerminado(inicial)):
        contadorNodos=contadorNodos + 1
        if fh.movValid(inicial, inicial.posicionRobotX - 1, inicial.posicionRobotY) and esMejorHeuristica(inicial,fh.move_up(inicial)):
            inicial = fh.move_up(inicial)
            
        elif fh.movValid(inicial, inicial.posicionRobotX + 1, inicial.posicionRobotY) and esMejorHeuristica(inicial,fh.move_down(inicial)):
            inicial = fh.move_down(inicial)
            
        elif fh.movValid(inicial, inicial.posicionRobotX, inicial.posicionRobotY - 1) and esMejorHeuristica(inicial,fh.move_left(inicial)):
            inicial = fh.move_left(inicial)
            
        elif fh.movValid(inicial, inicial.posicionRobotX, inicial.posicionRobotY + 1) and esMejorHeuristica(inicial,fh.move_right(inicial)):
            inicial = fh.move_right(inicial)
            
        elif fh.movValid(inicial, inicial.posicionRobotX +1, inicial.posicionRobotY - 1) and esMejorHeuristica(inicial,fh.diag_downLeft(inicial)):
            inicial = fh.diag_downLeft(inicial)
            
        elif fh.movValid(inicial, inicial.posicionRobotX + 1, inicial.posicionRobotY + 1) and esMejorHeuristica(inicial,fh.diag_downRight(inicial)):
            inicial = fh.diag_downRight(inicial)
            
        elif fh.movValid(inicial, inicial.posicionRobotX -1, inicial.posicionRobotY - 1) and esMejorHeuristica(inicial,fh.diag_upLeft(inicial)):
            inicial = fh.diag_upLeft(inicial)
            
        elif fh.movValid(inicial, inicial.posicionRobotX - 1, inicial.posicionRobotY + 1) and esMejorHeuristica(inicial,fh.diag_upRight(inicial)):
            inicial = fh.diag_upRight(inicial)
            
        else:
            print("BFS no ha podido encontrar una solución")
            print(f"Los movimientos de este tablero han sido {inicial.movimientosRealizados}")
            break

    if(fh.hemosTerminado(inicial)):     
        print(f"Las monedas recogidas son {inicial.monedasRecogidas}")
        print(f"La solucion de este tablero es {inicial.movimientosRealizados}")
        print(f"Tablero Final \n {inicial.table}")
        
    print(f"El numero de nodos generados es {contadorNodos}")