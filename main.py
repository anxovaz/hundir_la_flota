#declaracion del tablero
def main():
    tablero = [[0,0,0,0,4],
               [0,1,0,0,4],
               [0,0,0,0,4],
               [0,0,0,0,4],
               [0,2,2,0,0]]

    return tablero


def recorrer_tablero(lista): #
    contador = 0
    for i in lista:
        for j in i:
            if j != 0:
                contador += 1
    return contador

def recorrer_fila(lista): #
    contador = 0
    for i in lista:
        if i != 0:
            contador += 1

    return contador

def es_navio(parte):
    if parte in [1,2,4]:
        return True
    else:
        return False

def que_navio_es(parte): #
    if parte == 0:
        return "agua"
    elif parte == 1:
        return "submarino"
    elif parte == 2:
        return "buque"
    elif parte == 4:
        return "portaaviones"
    else:
        return "Parte incorrecta"

def salida_pantalla(coordenada, tipo_nave):
    print("Nave encontrada en " + str(coordenada) + ", tipo de nave: " + str(tipo_nave))



