import numpy as np
import FuncionesHeuristica as heur
import MaximaPendiente
import time
import EscaladaSimple as ES
import AStar as A
def cargarArchivo():      #falta lanzar error en caso de que el archivo no exista o no este en la carpeta 
    with open('Tableros/LABECOIN10.txt','r') as f:
        monedas=int(next(f))
        datos = ''.join(f.readlines()).replace('\n',';').strip(';')
    m = np.matrix(datos)
    

    return (m,monedas)
 

def main():
    print("LABECOIN")
    labecoin,monedas = cargarArchivo()  #tenemos el mata y el numero de modenas 
    #despues de cargar el archivo vamos a localizar la posicion de los elementos y crear el tablero
    print("ESTE ES EL MAPA QUE SE VA A RESOLVER")
    
    print(labecoin)
    posRobot=heur.localizarObjetivo(labecoin, 8) 
    salida =heur.localizarObjetivo(labecoin,7)
    coordMonedas= heur.obtMonedasTab(labecoin)
    tablero = heur.Tablero(monedas, posRobot[0],posRobot[1], labecoin,salida,coordMonedas,0,[])
    tablero.h = heur.DistanciaManhatan(tablero)
    print(f"El numero de monedas es {tablero.monedasNecesarias}")


    print("¿Con que algoritmo quieres resolver el puzzle?")
    opcion = input("1-Escalada simple.\n2-AStar \n3-BFS \n")

    match int(opcion):
        case 1:
            inicio=time.time()
            ES.EscaladaSimple(tablero)
            fin=time.time()
            print(f"el timepo que ha tardado en ejecutarse BFS es {fin-inicio}")
        case 2:
            A.AStar(tablero)
        case 3:
            MaximaPendiente.maximaPendiente(tablero)
      
    
main()
