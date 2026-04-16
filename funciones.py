import string as st

# Función que traduce un número a su correspondiente secuencia de letras
def orden_alfabetico(numero):
    abecedario = st.ascii_uppercase
    correspondencia = ""
    # si A -> 0, Z -> len(ABC)-1
    cociente = numero // (len(abecedario) - 1)  # El módulo toma la letra "grande" de la secuencia
    modulo = numero % (len(abecedario) - 1)     # El resto de la función es la letra mas "pequeña"
    
    if cociente > 1:
        correspondencia += abecedario[cociente]
    correspondencia += abecedario[modulo]   # 0 -> A
    return correspondencia  # Es una correspondencia para un número menor a 26^2

def traducir_coordenada (entrada : str):     # String de entrada es una secuencia letra-numero
    string_desglosado = entrada.strip()   # Quitar posibles espaciones y separar valores
    numero = int(string_desglosado[1:])
    letra = (string_desglosado[0]).upper()      # Por si ha puesto minuscula
    numero_letra = ord(letra) - 65      # 0 -> A
    return (numero - 1 , numero_letra)  # Numero + 1 para compensar que le dataframe printea desde el 1