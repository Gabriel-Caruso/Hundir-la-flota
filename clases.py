import numpy as np
import pandas as pd

from variables import LADO, ORIENTACIONES
from funciones import orden_alfabetico

class Barco:
    def __init__(self, nombre: str, eslora: int):
        self.nombre = nombre
        self.eslora = eslora
        self.vidas = eslora
        self.posiciones = []
        self.hits = []

    #Método para recibir el disparo. Comprueba que no le hayas disparado ya en una lista de hits
    #Si no has disparado ya en esa coordenada, añade la coordenada a la lista hits y resta una vida
    def hit(self, coordenada):
        if coordenada not in self.hits:
            self.hits.append(coordenada)
            self.vidas -= 1
    
    #Comprueba las vidas y devuelve True o False
    def is_dead(self):
        return self.vidas == 0


class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.lado = LADO # Viene de de variables.py
        self.barcos = []
        self.aguas = []
        self.tablero = np.zeros((self.lado, self.lado), dtype=object)

    def colocar_barco (self, barco : Barco, posicion : tuple, orientacion : str):

        # Comprobar parámetros de entrada
        if barco.eslora > self.lado:
            raise ValueError("El barco es demasiado grande para el tablero")
        elif orientacion not in ORIENTACIONES:
            raise ValueError("La orientación no es válida")

        else:
            if orientacion in "NS": # Para los barcos Norte y Sur, se comprueban las condiciones verticales (i)
                if orientacion == "N":
                    posicion_colocar = (posicion[0] - barco.eslora + 1, posicion[1])
                    # Transformar el barco hacia el norte en uno hacia el sur
                else:
                    posicion_colocar = posicion    # El barco hacia el sur
                
                fila, columna = posicion_colocar        # Para entender mejor el código
                # El barco tiene que caber en el tablero desde su posición  
                if (len(self.tablero[fila:, columna]) < barco.eslora) or (columna not in range(self.lado)) or \
                        (any(self.tablero[fila : fila + barco.eslora, columna])):   # Comprueba si hay un barco obstruyendo
                    raise ValueError("El barco no cabe en esa posición")
                else:
                    for i in range(barco.eslora):
                        # Pongo el barco tal cual, pero se puede poner la id
                        self.tablero[fila + i, columna] = barco
                        barco.posiciones.append((fila + i, columna))

                    self.barcos.append(barco) # guardar el barco en el tablero

            # Hacemos igual para las orientaciones de este y oeste
            if orientacion in "EO": # Para los barcos Este y Oeste, se comprueban las condiciones horizontales (j)
                if orientacion == "O":
                    posicion_colocar = (posicion[0], posicion[1] - barco.eslora + 1)
                    # Transformar el barco hacia el norte en uno hacia el este
                else:
                    posicion_colocar = posicion    # El barco hacia el este
                
                fila, columna = posicion_colocar        # Para entender mejor el código
                # El barco tiene que caber en el tablero desde su posición
                if (len(self.tablero[fila, columna:]) < barco.eslora) or (fila not in range (self.lado)) or \
                    (any(self.tablero[fila, columna:columna + barco.eslora])): # Comprueba si hay un barco obstruyendo
                    raise ValueError("El barco no cabe en esa posición")
                else:
                    for i in range(barco.eslora):
                        # Pongo el barco tal cual, pero se puede poner la id
                        self.tablero[fila, columna + i] = barco
                        barco.posiciones.append((fila, columna + i))

                    self.barcos.append(barco) # Guardar el barco en el tablero

        return  # No tiene que devolver nada

    def imprimir_tablero(self, completo = False):
        mapa_tablero = self.tablero.copy() # Para no modificar el tablero original
        for i in range(self.lado):
            for j in range(self.lado):
                if (i, j) in self.aguas:
                    mapa_tablero[i,j] = "~"
                elif self.tablero[i,j] != 0:
                    if (i, j) in self.tablero[i,j].hits: # COORDENADAS SON TUPLAS
                        mapa_tablero[i,j] = "X"
                    elif completo:                  # Sólo si queremos imprimir el trablero completo se añaden los abrcos sin tocar
                        mapa_tablero[i,j] = "O"
                    else:
                        mapa_tablero[i,j] = "·"     # La copia de tablero tendria el barco en esa posicion, hay que quitarla
                else:
                    mapa_tablero[i,j] = "·"         # Reemplazar 0 por "·"
                        
        columnas_tablero = [orden_alfabetico(i) for i in range(self.lado)]
        df_tablero = pd.DataFrame(mapa_tablero, columns=columnas_tablero, index=list(range(1, self.lado + 1)))
        print(df_tablero)
        return      # return None porque solo es imprimir

    def disparo (self, coordenada : tuple):
        acertado = False
        if coordenada[0] not in range(self.lado) or coordenada[1] not in range(self.lado):
            raise ValueError("Coordenada fuera del tablero")

        elif len(coordenada) != 2:      # por si las dimensiones de la coordenada no son correctas
            raise ValueError("Coordenada no válida")
        else:
            if coordenada in self.aguas:
                print("Ya has disparado a esa coordenada y no había nada")
            else:
                i, j = coordenada
                if type(self.tablero[i, j]) == Barco:
                    acertado = True
                    barco = self.tablero[i,j]
                    barco.hit(coordenada)
                    if barco.is_dead():
                        print("Tocado y hundido. Has acabado con el barco " + barco.nombre)
                    else:
                        print("Tocado")

                elif self.tablero[i,j] == 0:
                    self.aguas.append(coordenada)
                    print("Agua")
                    
        if self.flota_hundida():
            print("¡Has ganado! Has hundido toda la flota del enemigo: " + self.id_jugador)

        return acertado
    
    def flota_hundida(self):
        # Función all(): Recibe una lista de booleanos y devuelve True si todos son True
        # Por tanto, aquí recorre todos los barcos del tablero y pregunta is_dead(). Con que uno solo esté vivo, devuelve False
        return all(barco.is_dead() for barco in self.barcos)

