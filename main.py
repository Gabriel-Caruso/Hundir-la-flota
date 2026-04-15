import numpy as np
from variables import LADO, BARCOS
from clases import Barco, Tablero
from funciones import imprimir_tablero, disparo, colocar_barco
"""
importar ORIENTACIONES y cambiar var en este programa
Imprimr tablero como dataframe
imput del jugador sea LetraNumero y no num, num
"""

######!!!!!!!!!!!!!
orientaciones = ["N", "S", "E", "O"]
######

print("Bienvenido a Hundir la Flota, ¿preparado para jugar?")
nombre = input("Introduce tu nombre de jugador: ")

tablero_jugador = Tablero (nombre, LADO)
tablero_máquina= Tablero("Máquina", LADO)

# COLOCAR BARCOS DEL JUGADOR
for info_barco in BARCOS:       # todos los jugadores tienen los mismos barcos
    barco_jugador = Barco(info_barco)       # info_barco[0], info_barco[1] es una tupla
    orientacion_jugador = orientaciones[int(np.randint(4))]
    barco_colocado = False
    while not barco_colocado:

        coordenada_válida = False
        while not coordenada_válida:
            print(f"\nVamos a colocar el barco {info_barco[0]} de eslora {info_barco[1]}.")
            print("Este es el estado actual de tu tablero")
            imprimir_tablero(tablero_jugador, completo=True)       # imprimir el tablero completo del jugador para que vaya viendo todo
            orientacion_jugador = input("\nIntroduce una orientación en la que colocar el barco (N, S, E, O):")
            # creo que decidir la orientación del barco antes que la posición es más intuitivo

            print(f"Introduce la coordenada donde colocar el barco de eslora {info_barco[1]}.")
            valores_jugador = input("La coordenada debe tener el formato de dos enteros separados por una coma :")
            try:
                valor1 = int((valores_jugador.split(",")[0]).strip())   # strip por si acaso se ponen espacios
                valor2 = int((valores_jugador.split(",")[1]).strip())
                coordenada_jugador = (valor1, valor2)
                coordenada_válida = True    # si la coordenada vale continuamos

            except Exception as error:
                print(error + ", por favor vuelve a intentarlo.")

        try:
            # se coloca el barco donde se indica
            colocar_barco(tablero_jugador, barco_jugador, coordenada_jugador, orientacion_jugador)
            barco_colocado = True   # si se coloca el barco pasamos al siguiente
        except Exception as problema:
            print(problema + ", por favor vuelve a intertar colocar el barco.")

print("Perfecto! Ya están todos tus barcos colocados, ahora es el turno del oponente para colocar los suyos.")

print("El oponente está colocando sus barcos...")
# COLOCAR BARCOS DE LA MÁQUINA
for info_barco in BARCOS:       # todos los jugadores tienen los mismos barcos
    barco_maquina = Barco(info_barco)       # info_barco[0], info_barco[1] es una tupla
    orientacion_maquina = orientaciones[int(np.randint(4))]
    barco_colocado = False

    while not barco_colocado:
        coordenada_maquina = (np.random.randint(LADO), np.random.randint(LADO))     # maybe hace falta int()
        try:
            colocar_barco(tablero_maquina, barco_maquina, coordenada_maquina,orientacion_maquina)
            barco_colocado = True
        except: # Exception as problema
            # print(problema)   no hace falta para la máquina

print("¡Ya están todos los barcos colocados! Podemos empezar...")

while not tablero_máquina.flota_hundida or tablero_jugador.flota_hundida:
    turno_jugador = True
    turno_maquina = False
    while turno_jugador:
        print("¡Es tu turno! Elige una coordenada del tablero enemigo a la que disparar.")
        coordenada_válida = False

        while not coordenada_válida:
            print ("Este es el tablero del oponente:")
            imprimir_tablero(tablero_máquina)
            valores_jugador = input("Introduce la coordenada con el formato de dos enteros separados por una coma :")   # DOS ENTEROS CON COMA O LETRA+NUM
            try:
                    valor1 = int((valores_jugador.split(",")[0]).strip())   # strip por si acaso se ponen espacios
                    valor2 = int((valores_jugador.split(",")[1]).strip())
                    coordenada_jugador = (valor1, valor2)
                    coordenada_válida = True    # si la coordenada vale continuamos
            except Exception as error:
                    print(error + ", por favor vuelve a intentarlo.")
        
        try:
            resultado_disparo = disparo(tablero_máquina, coordenada_jugador)    # devuelve True si acierta
            turno_jugador = resultado_disparo   # si el jugador acierta le vuelve a tocar
            if resultado_disparo:
                print("¡Has acertado! Puedes volver a disparar")
            else:
                turno_maquina = True    # si falla le toca a la máquina
                print("\nEs el turno del oponente...")
        except Exception as error:
            print(error + ", por favor vuelve a intentarlo")
    
    if tablero_máquina.flota_hundida:
        break

    while turno_maquina:
        coordenada_maquina = (np.random.randint(LADO), np.random.randint(LADO))     # todas las coordenadas aquí deberían ser válidas
        try:
            resultado_disparo = disparo(tablero_jugador, coordenada_maquina)
            turno_maquina = resultado_disparo

            if resultado_disparo:
                print("El oponente ha acertado, continúa su turno...")
            else:
                print("El oponente ha fallado, vuelve a ser tu turno.")
            
        except: # Exception as problema
            # print(problema)   no hace falta para la máquina     

if tablero_jugador.flota_hundida:
    print("Vaya, ha ganado el oponente, ¡qué mal!")
    print("No pasa nada, puedes seguir intentándolo volviendo a jugar.")   

elif tablero_máquina.flota_hundida:
    print("¡Enhorabuena! Has ganado el juego pero, ¿podrás ganar otro?")