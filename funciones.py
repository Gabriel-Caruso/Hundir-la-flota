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
    if barco.eslora > LADO:
        raise ValueError("El barco es demasiado grande para el tablero")
    elif orientacion not in orientaciones:
        raise ValueError("La orientación no es válida")

    else:
        if orientacion in "NS": # Para los barcos Norte y Sur, se comprueban las condiciones verticales
            if orientacion == "N":
                posicion_colocar = [posicion[0] - barco.eslora, posicion[1]]
                # transformar el barco hacia el norte en uno hacia el sur
            else:
                posicion_colocar = posicion    # el barco hacia el sur
                
            if (LADO - posicion_colocar[0] + 1) < barco.eslora or (posicion_colocar[1] not in range(LADO)):   # el barco tiene que caber desde su posición
                # +1 para compensar el 0 porque hablamos de longitud, no de índices
                raise ValueError("El barco no cabe en esa posición")
            else:
                for i in range(barco.eslora):
                    # pongo el barco tal cual, pero se puede poner la id
                    tablero.tablero[posicion_colocar[0] + i, posicion_colocar[1]] = barco
                    barco.posiciones.append((posicion_colocar[0] + i, posicion_colocar[1]))

                tablero.barcos.append(barco) # guardar el barco en el tablero

        if orientacion in "EO": # Para los barcos Este y Oeste, se comprueban las condiciones horizontales    
            if orientacion == "O":
                posicion_colocar = [posicion[0], posicion[1] - barco.eslora]
                # transformar el barco hacia el norte en uno hacia el este
            else:
                posicion_colocar = posicion    # el barco hacia el este
                
            if (LADO - posicion_colocar[1] + 1 < barco.eslora) or (posicion_colocar[0] not in range (LADO)):   # el barco tiene que caber desde su posición
                # +1 para compensar el 0 porque hablamos de longitud, no de índices
                raise ValueError("El barco no cabe en esa posición")
            else:
                for i in range(barco.eslora):
                    # pongo el barco tal cual, pero se puede poner la id
                    tablero.tablero[posicion_colocar[0], posicion_colocar[1] + i] = barco
                    barco.posiciones.append((posicion_colocar[0], posicion_colocar[1] + i))

                tablero.barcos.append(barco) # guardar el barco en el tablero

    return tablero


def imprimir_tablero(tablero : Tablero):
    mapa_tablero = tablero.tablero.copy() # para no modificar el tablero original
    for i in range(tablero.lado):
        for j in range(tablero.lado):
            if tablero[i,j] != 0:
                #if (i, j) in tablero.aguas:
                #    mapa_tablero[i,j] = "~"     # HAY QUE AÑADIR EL ATRIBUTO AGUAS

                if (i, j) in tablero[i,j].hits: # COORDENADAS SON TUPLAS
                    mapa_tablero[i,j] = "X"
                else:
                    mapa_tablero[i,j] = "O"
    print(mapa_tablero)
    return      # return None porque solo es imprimir


# también queremos poder imprimir el tablero solo con la información que tiene el oponente
def ver_tablero_juego(tablero : Tablero):
    mapa_tablero = tablero.tablero.copy() # para no modificar el tablero original
    for i in range(tablero.lado):
        for j in range(tablero.lado):
            if tablero[i,j] != 0:
                #if (i, j) in tablero.aguas:
                #    mapa_tablero[i,j] = "~"     # HAY QUE AÑADIR EL ATRIBUTO AGUAS

                if (i, j) in tablero[i,j].hits: # COORDENADAS SON TUPLAS
                    mapa_tablero[i,j] = "X"
    print(mapa_tablero)
    return mapa_tablero # es util que lo devuelva para la máquina, pero no para imprimirlo para el jugador


def disparo (tablero : Tablero, coordenada : tuple):
    if coordenada[0] not in range(tablero.lado) or coordenada[1] not in range(tablero.lado):
        raise ValueError("Coordenada fuera del tablero")

    elif len(coordenada) != 2:      # por si las dimensiones de la coordenada no son correctas
        raise ValueError("Coordenada no válida")
    else:
        # if coordenada in tablero.aguas: # HAY QUE AÑADIR EL ATRIBUTO AGUAS
        #     print("Ya has disparado a esa coordenada y no había nada")
        # else:
            if type(tablero[coordenada]) == Barco:
                barco = tablero[coordenada]
                barco.hit(coordenada)
                if barco.is_dead():
                    print("Tocado y hundido. Has acabado con el barco " + barco.nombre)
                else:
                    print("Tocado")

            elif tablero[coordenada] == 0:
                #tablero.aguas.append(coordenada) # HAY QUE AÑADIR EL ATRIBUTO AGUAS
                print("Agua")
    
    if tablero.flota_hundida():
        print("¡Has ganado! Has hundido toda la flota del enemigo" + tablero.id_jugador)

    return tablero
