import numpy as np

Arreglo_Tridimensional = np.arange(729).reshape(9, 9, 9)

#----------------------------Funciones----------------------------

# Esta funcion delimita los ejes x,y,z del cubo
def ejes(fila, columna, eje_z):
    # x
    x = np.arange(fila*3, fila*3+3, 1)
    # y
    y = np.arange(columna*3, columna*3+3, 1)
    # z
    z = np.arange(eje_z*3, eje_z*3+3, 1)
    return x, y, z

# Se reemplazan los datos de posicion a posicion 
def Reemplazo_Posicion(nums, id_remplazo, z):
    for i, val in enumerate(nums):
        z[id_remplazo[i][0], id_remplazo[i]
            [1], id_remplazo[i][2]] = val


# crear un nuevo arreglo:
def cb(m1, m2, m3):
    return np.array(np.meshgrid(m1, m2, m3)).T.reshape(-1, 3)


# Crear una copia que mantiene los datos que se reemplazaran primero
def copia(id, z):
    copia = []
    for i in id:
        copia.append(z.item(*i))
    return copia


#------------------------------- Implementacion ---------------------------

Subidentificadores = np.array([[0, 0, 0],[0, 0, 1],[0, 0, 2],[0, 1, 0],[0, 2, 2],[0, 2, 3],
               [0, 2, 0],[0, 2, 1],[0, 2, 2],[1, 0, 0],[1, 0, 1],[1, 0, 2],
               [1, 1, 0],[1, 1, 1],[1, 1, 2],[1, 2, 0],[1, 2, 1],[1, 2, 2],
               [2, 0, 0],[2, 0, 1],[2, 0, 2],[2, 1, 0],[2, 1, 1],[2, 1, 2],
               [2, 2, 0],[2, 2, 1],[2, 2, 2] ])

Posicion_Inicial = int(input('Ingrese Identificador del Bloque 1 : '))
Posicion_Final = int(input('Ingrese Identificador del Bloque 2:'))


# Ubicar un limite en las tres posiciones x,y,z con los identificadores
x, y, z = ejes(*Subidentificadores[Posicion_Inicial])

#Se realiza la conversion para utilizar identificadores en la posicion 1 
conversion_1 = cb(x, y, z)

copia1 = copia(conversion_1 , Arreglo_Tridimensional)

# Ubicar un limite en las tres posiciones x,y,z con los identificadores

x_2, y_2, z_2 = ejes(*Subidentificadores[Posicion_Final])

#Se realiza la conversion para utilizar identificadores en la posicion 2
conversion_2 = cb(x_2, y_2, z_2)
copia2 = copia(conversion_2, Arreglo_Tridimensional)

# Se Reemplaza las posiciones 
Reemplazo_Posicion(copia1, conversion_2, Arreglo_Tridimensional)
Reemplazo_Posicion(copia2, conversion_1, Arreglo_Tridimensional)

# Resultado 
print(Arreglo_Tridimensional)
