from clases import Barco, Tablero
import numpy as np

"""
Puedo hacer que colocar barco pille args para barcos, posiciones y orientaciones
para crear el trablero de la máquina mas fácil.

Por ahora, como los barcos del jugador se colocarán uno a uno, no hace falta.
Ya lo añadiré luego.

"""
def colocar_barco (tablero : Tablero, barco : Barco, posicion : tuple, orientacion : str):
    orientaciones = ["N", "S", "E", "O"]

    # comprobar parámetros de entrada
    if barco.eslora > tablero.lado:
        raise ValueError("El barco es demasiado grande para el tablero")
    elif orientacion not in orientaciones:
        raise ValueError("La orientación no es válida")

    else:
        if orientacion in "NS": # Para los barcos Norte y Sur, se comprueban las condiciones verticales (i)
            if orientacion == "N":
                posicion_colocar = [posicion[0] - barco.eslora + 1, posicion[1]]
                # transformar el barco hacia el norte en uno hacia el sur
            else:
                posicion_colocar = posicion    # el barco hacia el sur
            
            # el barco tiene que caber desde su posición  
            if (len(tablero.tablero[posicion_colocar[0]:, posicion_colocar[1]]) < barco.eslora) or (posicion_colocar[1] not in range(tablero.lado)) or \
                    (all(tablero.tablero[posicion_colocar[0]:, posicion_colocar[1]])):   
                # +1 para compensar el 0 porque hablamos de longitud, no de índices
                raise ValueError("El barco no cabe en esa posición")
            else:
                for i in range(barco.eslora):
                    # pongo el barco tal cual, pero se puede poner la id
                    tablero.tablero[posicion_colocar[0] + i, posicion_colocar[1]] = barco
                    barco.posiciones.append((posicion_colocar[0] + i, posicion_colocar[1]))

                tablero.barcos.append(barco) # guardar el barco en el tablero

        if orientacion in "EO": # Para los barcos Este y Oeste, se comprueban las condiciones horizontales (j)
            if orientacion == "O":
                posicion_colocar = [posicion[0], posicion[1] - barco.eslora + 1]
                # transformar el barco hacia el norte en uno hacia el este
            else:
                posicion_colocar = posicion    # el barco hacia el este

            # el barco tiene que caber desde su posición
            if (len(tablero.tablero[posicion_colocar[0], posicion_colocar[1]:]) < barco.eslora) or (posicion_colocar[0] not in range (tablero.lado)) or \
                  (all(tablero.tablero[posicion_colocar[0], posicion_colocar[1]:])):
                # +1 para compensar el 0 porque hablamos de longitud, no de índices
                raise ValueError("El barco no cabe en esa posición")
            else:
                for i in range(barco.eslora):
                    # pongo el barco tal cual, pero se puede poner la id
                    tablero.tablero[posicion_colocar[0], posicion_colocar[1] + i] = barco
                    barco.posiciones.append((posicion_colocar[0], posicion_colocar[1] + i))

                tablero.barcos.append(barco) # guardar el barco en el tablero

    return tablero


def imprimir_tablero(tablero : Tablero, completo = False):
    mapa_tablero = tablero.tablero.copy() # para no modificar el tablero original
    for i in range(tablero.lado):
        for j in range(tablero.lado):
            if (i, j) in tablero.aguas:
                mapa_tablero[i,j] = "~"
            elif tablero.tablero[i,j] != 0:
                if (i, j) in tablero.tablero[i,j].hits: # COORDENADAS SON TUPLAS
                    mapa_tablero[i,j] = "X"
                elif completo:                  # sólo si queremos imprimir el trablero completo se añaden los abrcos sin tocar
                    mapa_tablero[i,j] = "O"
                else:
                    mapa_tablero[i,j] = 0       # La copia de tablero tendria el barco en esa posicion, hay que quitarla
    print(mapa_tablero)
    return      # return None porque solo es imprimir


def disparo (tablero : Tablero, coordenada : tuple):
    acertado = False
    if coordenada[0] not in range(tablero.lado) or coordenada[1] not in range(tablero.lado):
        raise ValueError("Coordenada fuera del tablero")

    elif len(coordenada) != 2:      # por si las dimensiones de la coordenada no son correctas
        raise ValueError("Coordenada no válida")
    else:
        if coordenada in tablero.aguas:
             print("Ya has disparado a esa coordenada y no había nada")
        else:
            i, j = coordenada
            if type(tablero.tablero[i, j]) == Barco:
                acertado = True
                barco = tablero.tablero[i,j]
                barco.hit(coordenada)
                if barco.is_dead():
                    print("Tocado y hundido. Has acabado con el barco " + barco.nombre)
                else:
                    print("Tocado")

            elif tablero.tablero[i,j] == 0:
                tablero.aguas.append(coordenada)
                print("Agua")
                
    
    if tablero.flota_hundida():
        print("¡Has ganado! Has hundido toda la flota del enemigo: " + tablero.id_jugador)

    return acertado
