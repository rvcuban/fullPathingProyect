import FuncionesHeuristica as fh
import time

def maximaPendiente(inicial:fh.Tablero):
    inicio=time.time()
    listaAbiertos= []
    nodosGenerados=0
    hemosTerminado = False
    while (not hemosTerminado):
        if fh.movValid(inicial, inicial.posicionRobotX - 1, inicial.posicionRobotY):
            listaAbiertos.append(fh.move_up(inicial))
        if fh.movValid(inicial, inicial.posicionRobotX + 1, inicial.posicionRobotY):
            listaAbiertos.append(fh.move_down(inicial))
        if fh.movValid(inicial, inicial.posicionRobotX, inicial.posicionRobotY - 1):
            listaAbiertos.append(fh.move_left(inicial))
        if fh.movValid(inicial, inicial.posicionRobotX, inicial.posicionRobotY + 1):
            listaAbiertos.append(fh.move_right(inicial))
        if fh.movValid(inicial, inicial.posicionRobotX +1, inicial.posicionRobotY - 1):
            listaAbiertos.append(fh.diag_downLeft(inicial))     
        if fh.movValid(inicial, inicial.posicionRobotX + 1, inicial.posicionRobotY + 1):
            listaAbiertos.append(fh.diag_downRight(inicial))
        if fh.movValid(inicial, inicial.posicionRobotX -1, inicial.posicionRobotY - 1):
            listaAbiertos.append(fh.diag_upLeft(inicial))
        if fh.movValid(inicial, inicial.posicionRobotX - 1, inicial.posicionRobotY + 1):
            listaAbiertos.append(fh.diag_upRight(inicial))      
        
        mejorNodo = listaAbiertos[0]
        #Recorremos la lista de abiertos para conseguir el nodo con mejor heuristica
         
        nodosGenerados=nodosGenerados+len(listaAbiertos)
        
        for nodo in listaAbiertos:
            if mejorNodo.h > nodo.h:
                mejorNodo = nodo

        listaAbiertos.clear()
        if (mejorNodo.h < inicial.h):
            inicial = mejorNodo
        else: 
            print("BFS no ha podido encontrar una solución")
            print(f"La solucion de este tablero es {inicial.movimientosRealizados}")
            break

        if (fh.hemosTerminado(inicial)):
            hemosTerminado = True

    fin=time.time()

    if(hemosTerminado):      
        print(f"Las monedas recogidas son {inicial.monedasRecogidas}")
        print(f"La solucion de este tablero es {inicial.movimientosRealizados}")
        print(f"Tablero Final \n {inicial.table}")
        
    print(f"numero de nodos generados {nodosGenerados}")
    print(f"el timepo que ha tardado en ejecutarse BFS es {fin-inicio}")




    

        
            
        


        

