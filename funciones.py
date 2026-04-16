import string as st

def orden_alfabetico(numero):
    abecedario = st.ascii_uppercase
    correspondencia = ""
    cociente = numero // (len(abecedario) - 1)      # si A -> 0, Z -> len(ABC)-1
    modulo = numero % (len(abecedario) - 1)
    
    if cociente > 1:
        correspondencia += abecedario[cociente]
    correspondencia += abecedario[modulo]   # 0 -> A
    return correspondencia

def traducir_coordenada (entrada : str):     # string de entrada es una secuencia letra-numero
    string_desglosado = entrada.strip()   # quitar posibles espaciones y separar valores
    numero = int(string_desglosado[1])
    letra = (string_desglosado[0]).upper()      # por si ha puesto minuscula
    numero_letra = ord(letra) - 65      # 0 -> A
    return (numero - 1 , numero_letra)  # numero + 1 para compensar que le dataframe printea desde el 1