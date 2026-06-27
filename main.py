def cargar_mapa(mapa_actual) --> Gerardo:
    return None


def obtener_metas(matriz) --> Joshua:
    metas = []
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == "." or matriz[fila][columna] == "*":
                metas.append([fila, columna])
    return metas


def buscar_jugador(matriz) --> Joshua:
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] == "@":
                return f, c
    return 0, 0


def intentar_movimiento(matriz, metas, f_actual, c_actual, df, dc) --> César:

    f_actual, c_actual=buscar_jugador()
    df, dc = 0, 0
    if direccion == 'arriba':
        df = -1
    elif direccion == 'abajo':
        df = 1
    elif direccion == 'izquierda':
        dc = -1
    elif direccion == 'derecha':
        dc = 1

    f_nueva, c_nueva = f_actual + df, c_actual + dc

    Destino = mapa_actual[f_nueva][c_nueva]

    if Destino in [' ', '.']:
        if metas == (f_actual, c_actual):
            mapa_actual[f_actual][c_actual] = '.'
        else:
            mapa_actual[f_actual][c_actual] = ' '

        mapa_actual[f_nueva][c_nueva] = 'P'


    elif celda_destino == '$':

        f_caja_nueva, c_caja_nueva = f_nueva + df, c_nueva + dc


        celda_tras_caja = mapa_actual[f_caja_nueva][c_caja_nueva]


        if celda_tras_caja in [' ', '.']:
            
            if metas == (f_actual, c_actual):
                mapa_actual[f_actual][c_actual] = '.'
            else:
                mapa_actual[f_actual][c_actual] = ' '


            mapa_actual[f_nueva][c_nueva] = 'P'


            mapa_actual[f_caja_nueva][c_caja_nueva] = '$'


            if (f_caja_nueva, c_caja_nueva) == metas:
                juego_terminado = True


def actualizar_metas(matriz, metas) --> Paco:
    return None


def verificar_victoria(matriz, metas) --> Paco:
    return None


def registrar_puntuacion(nombre_jugador, nivel, movimientos) --> César:
    return None


def mostrar_puntuaciones() --> Gerardo:
    return None


def dibujar_mapa(matriz) --> Álvaro:
   def reinicio():
    with open("Sokodries#18.txt","r",encoding="utf-8") as original_map:
        # ctr + / = #
        contenido= ""
        for h in original_map:
            contenido += h

        escribirmapa(contenido)


def escribirmapa(mapa:str,instruccion):


    with open("Sokodries18game","w",encoding="utf-8") as map1:


        map1.write(mapa)
        leermapa(mapa)

def leermapa(mapa):
    with open("Sokodries18game","r",encoding="utf-8") as gameplay:

        print(mapa)

def main():

    while(1):
        reinicio()
        a = input("muevete o escribe 'esc': ")
        a.lower()
        if a =="esc":
            reinicio()
        if a == "a":

MAPAS --> Álvaro
MENÚ PRINCIPAL --> Gerardo:
