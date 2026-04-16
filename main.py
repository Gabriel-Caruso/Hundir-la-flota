import numpy as np
import time
from variables import LADO, BARCOS, ORIENTACIONES
from clases import Barco, Tablero
from funciones import traducir_coordenada

"""
El programa consiste, incialmente, de dos bucles for con whiles anidados para colocar los barcos,
primero  el jugador y luego lamáquina.

Después, el bucle principal del juego es un buble while con anidaciones para los turnos de cada jugador.
"""

print("Bienvenido a Hundir la Flota, ¿preparado para jugar?")
nombre = input("Introduce tu nombre de jugador: ")

tablero_jugador = Tablero(nombre)
tablero_maquina= Tablero("Máquina")

# COLOCAR BARCOS DEL JUGADOR
for info_barco in BARCOS:   # BARCOS es la colección de barcos 
    barco_jugador = Barco(info_barco[0], info_barco[1])       # info_barco es una tupla
    barco_colocado = False

    while not barco_colocado:   # Vamos a colocar los barcos del jugador

        coordenada_valida = False
        while not coordenada_valida:
            print(f"\nVamos a colocar el barco {info_barco[0]} de eslora {info_barco[1]}.")
            print("Este es el estado actual de tu tablero")
            tablero_jugador.imprimir_tablero(completo=True)       # Imprimir el tablero completo del jugador para que vaya viendo todo
            orientacion_jugador = ((input("\nIntroduce una orientación en la que colocar el barco (N, S, E, O):")).upper()).strip()
            # Limpiar el input en caso de que sea minuscula o tenga espacios
            # Creo que decidir la orientación del barco antes que la posición es más intuitivo

            print(f"Introduce la coordenada donde colocar el barco de eslora {info_barco[1]}.")
            valores_jugador = input("La coordenada tiene el formato letra mayúscula seguida de número (ej: C9):")
            try:
                coordenada_jugador = traducir_coordenada(valores_jugador)
                coordenada_valida = True    # Si la coordenada vale continuamos

            except Exception as error:
                print(str(error) + ", por favor vuelve a intentarlo.")  # Continua el while con el mismo barco

        try:
            # Se coloca el barco donde se indica
            tablero_jugador.colocar_barco(barco_jugador, coordenada_jugador, orientacion_jugador)
            barco_colocado = True   # Si se coloca el barco pasamos al siguiente
        except Exception as error:
            print(str(error) + ", por favor vuelve a intertar colocar el barco.")

print("Perfecto! Ya están todos tus barcos colocados, ahora es el turno del oponente para colocar los suyos.")

print("El oponente está colocando sus barcos...")
# COLOCAR BARCOS DE LA MÁQUINA
for info_barco in BARCOS:       # Todos los jugadores tienen los mismos barcos
    barco_maquina = Barco(info_barco[0], info_barco[1])
    barco_colocado = False

    while not barco_colocado:
        coordenada_maquina = (np.random.randint(LADO), np.random.randint(LADO))     # Maybe hace falta int()
        orientacion_maquina = ORIENTACIONES[int(np.random.randint(4))]          # Puede que la orientación elegida no quepa en el tablero, así que tiene que ir dentro
        try:
            tablero_maquina.colocar_barco(barco_maquina, coordenada_maquina, orientacion_maquina)  # Intentamos colocar el barco
            barco_colocado = True
        except:
            pass    # Si no se puede colocar se vuelve a intentar, no queremos print del error para la maquina

print("¡Ya están todos los barcos colocados! Podemos empezar...")
time.sleep(1)   # Que no vaya todo tan rapido 

while not tablero_maquina.flota_hundida() or tablero_jugador.flota_hundida():
    turno_jugador = True
    turno_maquina = False

    while turno_jugador:
        print("\n¡Es tu turno! Elige una coordenada del tablero enemigo a la que disparar.")
        coordenada_valida = False

        while not coordenada_valida:
            print ("Este es el tablero del oponente:")
            tablero_maquina.imprimir_tablero()
            time.sleep(1)   # Para que tenga timing
            valores_jugador = input("Introduce la coordenada con el formato letra mayúscula seguida de número (ej: C9):")
            try:
                    coordenada_jugador = traducir_coordenada(valores_jugador)
                    coordenada_valida = True    # Si la coordenada vale continuamos
            except Exception as error:
                    print(str(error) + ", por favor vuelve a intentarlo.")
        
        try:
            resultado_disparo = tablero_maquina.disparo(coordenada_jugador)    # Devuelve True si acierta
            turno_jugador = resultado_disparo   # Si el jugador acierta le vuelve a tocar
            if resultado_disparo:
                print("¡Has acertado! Puedes volver a disparar")
                time.sleep(1)   # Para que se pueda leer todo
            else:
                turno_maquina = True    # Si falla le toca a la máquina
                if not tablero_maquina.flota_hundida():     # Que no diga que es el turno del oponente si gana el jugador
                    print("\nEs el turno del oponente...")
        except Exception as error:
            print(str(error) + ", por favor vuelve a intentarlo")

    time.sleep(1)   # Si no, no da tiempo a ver el resultado
    if tablero_maquina.flota_hundida():
        break

    while turno_maquina:
        coordenada_maquina = (np.random.randint(LADO), np.random.randint(LADO))     # Todas las coordenadas aquí deberían ser válidas
        if coordenada_maquina in tablero_jugador.aguas:
            continue    # Para que no sea súper fácil ganar a la máquina, que no dispare dos veces al mismo agua

        try:
            resultado_disparo = tablero_jugador.disparo(coordenada_maquina)
            turno_maquina = resultado_disparo

            if resultado_disparo:
                print("El oponente ha acertado, continúa su turno...")
            else:
                print("El oponente ha fallado, vuelve a ser tu turno.")
            
        except:
            pass   # No hace falta para la máquina     
    print("Este es tu tablero tras el turno del oponente:")
    tablero_jugador.imprimir_tablero(completo=True)

    time.sleep(1)   # Para que de tiempo a leer

if tablero_jugador.flota_hundida:   # Si gana la máquina
    print("\nVaya, ha ganado el oponente, ¡qué mal!")
    print("No pasa nada, puedes seguir intentándolo volviendo a jugar.")

elif tablero_maquina.flota_hundida: # Si gana el jugador
    print("¡Enhorabuena! Has ganado el juego pero, ¿podrás ganar otro?")
    
time.sleep(1)
# Para terminar el juego, imprimir todos los tableros 
print("\nEstos son los tableros al final del juego: ")
print("TABLERO DEL OPONENTE")
tablero_maquina.imprimir_tablero(completo=True)
print("\nTABLERO DEL JUGADOR")
tablero_jugador.imprimir_tablero(completo=True)