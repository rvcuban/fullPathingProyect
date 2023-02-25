import numpy as np
import math
import copy

valorMoneda = 0

def localizarObjetivo(tablero, num):
    for x, y in zip(*np.where(tablero == num)):
        print("El elemento buscado[{}, {}] vale {}".format(x, y, tablero[x, y]))
        break
    return x, y


class Tablero:
    """esta es la clase tablero que almacenara toda la infomracion del juego"""

   
    def __init__(self, monedasNecesarias = 0, posicionRobotX = None, posicionRobotY = None, table = None, salida = None
                ,coordMonedas = None, h = 0, movimientosRealizados: list = None, monedasRecogidas = 0, g : int = 0, f : int = 0):
        if not monedasNecesarias:
            return None
        self.monedasNecesarias = monedasNecesarias
        self.posicionRobotX = posicionRobotX
        self.posicionRobotY = posicionRobotY
        self.table = table
        self.h = h
        self.movimientosRealizados = movimientosRealizados
        self.g = g
        self.f = f


        # agregado
        self.monedasRecogidas = monedasRecogidas # contador con monedas recogidas hasta el momento dentro del tablero
        self.salida = salida
        self.coordMonedas= coordMonedas #lista de las coordenadas de las monedas dentro de la matriz 

    def __str__(self) -> str:
        return f"Numero de monedas:{self.monedas} en el tablero\n {self.table}\n posicion del robot:{self.posicionRobotX,self.posicionRobotY}\n el numero de monedas recogidas actualmente es {self.monedasRecogidas}"


def obtMonedasTab(tablero):
    listaMonedas=[]
    dim = len(tablero)  # Es una matriz cuadrada N x N
    for i in range(0, dim):  # columna
        for j in range(0, dim):  # fila
            if (tablero[i,j]>=1) and (tablero[i,j]<7):
                posicion=i,j
                listaMonedas.append(posicion)
    return listaMonedas

def movValid(tablero: Tablero, x, y):
    return tablero.table[x, y] != 9


def hayMoneda(tablero: Tablero, x, y):
    global valorMoneda
    if tablero.table[x, y] < 7 and tablero.table[x, y] != 0:
        valorMoneda = tablero.table[x, y]
        m = True
        return m
    else:
        m = False
        return m


def move_up(tablero: Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY

    coorMov = (x - 1, y)
    exisMoneda= hayMoneda(nuevoEstado, x - 1, y)
    if (exisMoneda):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
        nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor
        nuevoEstado.coordMonedas.remove(coorMov) 

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX - 1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY
    nuevoEstado.table[x - 1, y] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("A")
    nuevoEstado.g = len(nuevoEstado.movimientosRealizados)
    nuevoEstado.f = nuevoEstado.g + nuevoEstado.h
    return nuevoEstado

def move_down(tablero: Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY

    
    coorMov = (x + 1, y)
    exisMoneda= hayMoneda(nuevoEstado, x + 1, y)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor
            nuevoEstado.coordMonedas.remove(coorMov)

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX + 1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY
    nuevoEstado.table[x + 1, y] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("B")
    nuevoEstado.g = len(nuevoEstado.movimientosRealizados)
    nuevoEstado.f = nuevoEstado.g + nuevoEstado.h
    return nuevoEstado

def move_left(tablero: Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY

    coorMov = (x, y-1)
    exisMoneda= hayMoneda(nuevoEstado, x, y - 1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor
            nuevoEstado.coordMonedas.remove(coorMov) 

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX 
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY - 1
    nuevoEstado.table[x , y - 1] = 8
    nuevoEstado.table[x, y ] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("I")
    nuevoEstado.g = len(nuevoEstado.movimientosRealizados)
    nuevoEstado.f = nuevoEstado.g + nuevoEstado.h
    return nuevoEstado

def move_right(tablero: Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY

    coorMov = (x, y + 1)
    exisMoneda= hayMoneda(nuevoEstado, x, y + 1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor
            nuevoEstado.coordMonedas.remove(coorMov) 

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX 
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY + 1
    nuevoEstado.table[x , y +1] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("D")
    nuevoEstado.g = len(nuevoEstado.movimientosRealizados)
    nuevoEstado.f = nuevoEstado.g + nuevoEstado.h
    return nuevoEstado
        

def  diag_upRight(tablero:Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY


    coorMov = (x - 1, y + 1)
    exisMoneda= hayMoneda(nuevoEstado, x - 1, y + 1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor
            nuevoEstado.coordMonedas.remove(coorMov) 

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX -1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY + 1
    nuevoEstado.table[x-1 , y +1] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("AD")
    nuevoEstado.g = len(nuevoEstado.movimientosRealizados)
    nuevoEstado.f = nuevoEstado.g + nuevoEstado.h
    return nuevoEstado


def  diag_upLeft(tablero:Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY

    coorMov = (x - 1, y - 1)
    exisMoneda= hayMoneda(nuevoEstado, x - 1, y - 1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor
            nuevoEstado.coordMonedas.remove(coorMov) 

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX -1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY -1
    nuevoEstado.table[x-1 , y -1] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("AI")
    nuevoEstado.g = len(nuevoEstado.movimientosRealizados)
    nuevoEstado.f = nuevoEstado.g + nuevoEstado.h
    return nuevoEstado


def  diag_downRight(tablero:Tablero): 
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY

    coorMov = (x + 1, y + 1)
    exisMoneda= hayMoneda(nuevoEstado, x + 1, y + 1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor
            nuevoEstado.coordMonedas.remove(coorMov) 

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX +1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY + 1
    nuevoEstado.table[x+1 , y +1] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("BD")
    nuevoEstado.g = len(nuevoEstado.movimientosRealizados)
    nuevoEstado.f = nuevoEstado.g + nuevoEstado.h
    return nuevoEstado  

def  diag_downLeft(tablero:Tablero):   
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY

    coorMov = (x + 1, y - 1)
    exisMoneda= hayMoneda(nuevoEstado, x + 1, y - 1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor
            nuevoEstado.coordMonedas.remove(coorMov)
            

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX +1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY -1 
    nuevoEstado.table[x+1 , y -1] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("BI")
    nuevoEstado.g = len(nuevoEstado.movimientosRealizados)
    nuevoEstado.f = nuevoEstado.g + nuevoEstado.h
    return nuevoEstado



def DistanciaManhatan(tablero:Tablero):
     #la distancia de manjatan nos dice que la distancia entre 2 putnos con coordenadas 
     #siendo p(x,y) y q(r,s) la distancia d se calcula (d(p,q))=raiz( (r-x)^2+(s-y)^2)
     #para nosotros sera la distancia del robot p a la moneda .quedando asi= d(r,m)=raiz(moneda[x]-robotX)^2+(mondeda[y]-robot`[y]^2)
     
    heuristica = 0
     
    posRobot = [tablero.posicionRobotX , tablero.posicionRobotY]
    if tablero.monedasRecogidas < int(tablero.monedasNecesarias):
        for moneda in tablero.coordMonedas:
            valorX = moneda[0] - posRobot[0]
            valorY = moneda[1] - posRobot[1]
            heuristica = heuristica + math.sqrt(math.pow(valorX, 2) + math.pow(valorY, 2) + math.pow(tablero.salida[0] - moneda[0],2) + math.pow(tablero.salida[1] - moneda[1],2))
    else:
        heuristica = math.sqrt(math.pow(tablero.posicionRobotX - tablero.salida[0],2) + math.pow(tablero.posicionRobotY - tablero.salida[1],2))
    
    return heuristica


def hemosTerminado (tablero: Tablero):
    if (tablero.posicionRobotX == tablero.salida[0] and tablero.posicionRobotY == tablero.salida[1] and (tablero.monedasRecogidas >= tablero.monedasNecesarias)):
        return True
    else:
        return False
    
def tablerosIguales(inicial:Tablero, nuevoTablero:Tablero):
     
     return 

def estaEnLista(nodo : Tablero, listaAbiertos):
    for nodoA in listaAbiertos:
          if(np.array_equal(nodo.table,nodoA.table)):
               return True
    
    return False



     


