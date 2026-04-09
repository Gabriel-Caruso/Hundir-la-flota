import numpy as np

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
        self.lado = LADO # -> constante de variables.py || Lo de las mayúsculas es porque en Java se hace así con las constantes!
        self.barcos = []
        self.tablero = np.zeros((self.lado, self.lado))     #TODO: Comprobar si no hace falta meter un dtype=object para que nos deje pasar "X" y "~"

        #Aquí se recorre la constante BARCOS con todos los barcos indicados en el ejercicio. Esto debería estar en variables.py
        #Se almacena en la lista de self.barcos
        for nombre, eslora in BARCOS:
            barco = Barco(nombre, eslora)
            self.barcos.append(barco)

    def colocar_barcos(self):
        #TODO: De esta función se encarga Ana
        pass

    def imprimir_tablero(self):
        #TODO: De esta función se encarga Ana
        pass

    def disparo(self, coordenada):
        #TODO: De esta función se encarga Ana
        #Comprobar si hay barco, recorrer self.barcos y mirar bien cuándo llamar a barco.hit() y barco.is_dead()
        pass
    
    #Función interesantísima la de all(): Recibe una lista de booleanos y devuelve True si todos son True
    #Por tanto, aquí recorre todos los barcos del tablero y pregunta is_dead(). Con que uno solo esté vivo, devuelve False
    #Eso sí, hay que comprobar que funcione bien :_)
    def flota_hundida(self):
        return all(barco.is_dead() for barco in self.barcos)    
    
    """Creo que es lo mismo que escribir esto otro, pero lo comprobaremos cuando tengamos el main:
            def flota_hundida(self):
                for barco in self.barcos:
                    if not barco.is_dead():
                        return False
                return True
    """

