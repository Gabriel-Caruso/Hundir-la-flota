class Tablero:
    def __init__(self, barcos, lado = 10):
        self.lado = lado
        self.barcos = barcos
        self.tablero = np.zeros(lado, lado)