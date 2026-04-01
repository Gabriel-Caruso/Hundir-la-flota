class Barco:
    def __init__(self,
                 eslora = int(input("Indica la eslora de tu barco: ")),
                 nombre = str(input("Escribe el nombre de tu barco: ")),
                 orientacion = str(input("Indica la orientación: N, S, E, O: "))
                 ):
        self.nombre = nombre
        self.eslora = eslora
        self.orientacion = orientacion