# Hundir-la-flota

Desarrollado en Python. Proyecto POO del Team Challenge del Sprint 03 del Bootcamp de DataScience + IA en [TheBridge](https://thebridge.tech/)

## ¿Cómo funciona?

- Dos jugadores: tú y la máquina
- Tablero de 10x10
- Colocas tus barcos al principio de la partida indicando coordenada y orientación (N, S, E, O)
- Si aciertas, vuelves a disparar. Si fallas, le toca a la máquina
- Gana quien hunda la flota del adversario

## Listado de barcos

Los barcos se diferencian por su eslora, que es la cantidad de casillas que ocupan.

| Barco | Eslora | Cantidad |
|:-----:|:------:|:--------:|
| Eslora 4 | 4 | 1 |
| Eslora 3 | 3 | 2 |
| Eslora 2 | 2 | 3 |
| Eslora 1 | 1 | 4 |

## Requisitos

Requiere instalar Pandas y Numpy para ejecutarlo

Numpy:

```bash
pip install numpy
```

Pandas:
```bash
pip install pandas
```

## Ejecución
```bash
python main.py
```

## Equipo y estructuras del proyecto
### Equipo
[Ramiro Caruso Campos](https://github.com/Gabriel-Caruso) y [Ana Manzanares Muñoz](https://github.com/A-Manz)

### Estructura

- main.py - Programa principal
- clases.py - Clases Barco y Tablero
- funciones.py - Funciones auxiliares
- variables.py - Variables del juego
