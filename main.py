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
    return None


def actualizar_metas(matriz, metas) --> Paco:
    return None


def verificar_victoria(matriz, metas) --> Paco:
    return None


def registrar_puntuacion(nombre_jugador, nivel, movimientos) --> César:
    return None


def mostrar_puntuaciones() --> Gerardo:
    return None


def dibujar_mapa(matriz) --> Álvaro:
    return None

MAPAS --> Álvaro
MENÚ PRINCIPAL --> Gerardo:
