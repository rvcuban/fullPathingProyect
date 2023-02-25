import FuncionesHeuristica as fh
import time

def crearListaF(lista):
    listaF = []
    for nodo in lista:
        listaF.append(nodo.f)
    return listaF


def AStar(inicial:fh.Tablero):
    listaCerrados=[]
    listaAbiertos = []
    listaVecinos = []
    listaAvacia = False
    listaCerrados.append(inicial)
    while (not fh.hemosTerminado(inicial) and (not listaAvacia)):
     
        if fh.movValid(inicial, inicial.posicionRobotX - 1, inicial.posicionRobotY) and (fh.move_up not in listaCerrados):
            listaVecinos.append(fh.move_up(inicial))

        if fh.movValid(inicial, inicial.posicionRobotX + 1, inicial.posicionRobotY) and (fh.move_down not in listaCerrados):
            listaVecinos.append(fh.move_down(inicial))

        if fh.movValid(inicial, inicial.posicionRobotX, inicial.posicionRobotY - 1) and (fh.move_left not in listaCerrados):
            listaVecinos.append(fh.move_left(inicial))

        if fh.movValid(inicial, inicial.posicionRobotX, inicial.posicionRobotY + 1) and (fh.move_right not in listaCerrados):
            listaVecinos.append(fh.move_right(inicial))

        if fh.movValid(inicial, inicial.posicionRobotX +1, inicial.posicionRobotY - 1) and (fh.diag_downLeft not in listaCerrados):
            listaVecinos.append(fh.diag_downLeft(inicial))  

        if fh.movValid(inicial, inicial.posicionRobotX + 1, inicial.posicionRobotY + 1) and  (fh.diag_downRight not in listaCerrados):
            listaVecinos.append(fh.diag_downRight(inicial))

        if fh.movValid(inicial, inicial.posicionRobotX -1, inicial.posicionRobotY - 1) and  (fh.diag_upLeft not in listaCerrados):
            listaVecinos.append(fh.diag_upLeft(inicial))

        if fh.movValid(inicial, inicial.posicionRobotX - 1, inicial.posicionRobotY + 1) and (fh.diag_upRight not in listaCerrados):
            listaVecinos.append(fh.diag_upRight(inicial))
        
        for nodoVecino in listaVecinos:
            if (not fh.estaEnLista(nodoVecino,listaAbiertos) and (not fh.estaEnLista(nodoVecino,listaCerrados))):
                listaAbiertos.append(nodoVecino)
            else:
                
                for nodoAbierto in listaAbiertos:
                    if(fh.tablerosIguales(nodoAbierto, nodoVecino) and nodoAbierto.g > nodoVecino.g):
                        listaAbiertos.remove(nodoAbierto)
                        listaAbiertos.append(nodoVecino)
                        break
            
        listaVecinos.clear()
        mejorNodo = listaAbiertos[0]
        for nuevoNodo in listaAbiertos:
            if (nuevoNodo.f < mejorNodo.f):
                mejorNodo = nuevoNodo
        
        listaAbiertos.remove(mejorNodo)
        listaCerrados.append(mejorNodo)
        
        if (len(listaAbiertos) == 0):

            listaAvacia = True
        
        inicial = mejorNodo

    
    if(fh.hemosTerminado(inicial)):
        print(f"La solución que ha encontrado A* es {inicial.movimientosRealizados}")
        print(f"Tablero final: \n {inicial.table}")
        print(f"El numero total de monedas recogidas es: {inicial.monedasRecogidas}")

    else:
        print("A* no ha podido encontrar una solución")
        print(inicial.table)

    