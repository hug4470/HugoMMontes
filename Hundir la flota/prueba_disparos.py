import numpy as np
import random

class Barco:
    def __init__(self, eslora):
        self.eslora = eslora
        self.coordenadas = []

    def definir_coordenadas(self, orientacion, fila, columna):
        """
        Define las coordenadas del barco asegurando que esté dentro del tablero.
        """
        self.coordenadas = []  # Limpiar coordenadas previas
        if orientacion == 'H':
        # HORIZONTAL: Verifica si todo el barco cabe en la fila desde la columna inicial
            if columna + self.eslora <= 10:
                for numero in range(self.eslora):
                    self.coordenadas.append((fila, columna + numero))
            else:
                # print("No cabe, intenta otra eslora u otras coordenadas")
                self.coordenadas = []  # No cabe, no se añaden coordenadas
        elif orientacion == 'V':
            # VERTICAL: Verifica si todo el barco cabe en la columna desde la fila inicial
            if fila + self.eslora <= 10:
                for numero in range(self.eslora):
                    self.coordenadas.append((fila + numero, columna))
            else:
                # print("No cabe, intenta otra eslora u otras coordenadas")
                self.coordenadas = []  # No cabe, no se añaden coordenadas
                

def barco_validador(barco, tablero):
    """
    Verifica si las coordenadas del barco no colisionan con otros barcos.
    """
    for (fila, columna) in barco.coordenadas:
        if tablero[fila, columna] != '_':  # Si ya hay un barco en esa posición
            return False
    return True

def colocar_barco_en_tablero(barco, tablero):
    """
    Coloca el barco en el tablero si las coordenadas son válidas.
    """
    for (fila, columna) in barco.coordenadas:
        tablero[fila, columna] = 'O'
    return tablero

def crear_barcos_aleatorios(tamaño_tablero=10):
    """
    Crea 6 barcos (3x2, 2x3, 1x4) y los coloca en el tablero de forma aleatoria.
    """
    tablero = np.full((tamaño_tablero, tamaño_tablero), "_")
    barcos_a_crear = [(2, 3), (3, 2), (4, 1)]  # 3 barcos de eslora 2, 2 barcos de eslora 3, 1 barco de eslora 4
    barcos = []

    for eslora, cantidad in barcos_a_crear:
        for barco in range(cantidad):
            colocado = False
            while not colocado:
                # Generar orientación y posición inicial aleatorias
                orientacion = random.choice(['H', 'V'])
                fila = random.randint(0, tamaño_tablero - 1)
                columna = random.randint(0, tamaño_tablero - 1)
                
                # Crear el barco
                barco = Barco(eslora)
                barco.definir_coordenadas(orientacion, fila, columna)

                # Verificar si las coordenadas son válidas
                if len(barco.coordenadas) == eslora and barco_validador(barco, tablero):
                    # Colocar el barco en el tablero
                    tablero = colocar_barco_en_tablero(barco, tablero)
                    barcos.append(barco)
                    colocado = True

    return tablero, barcos

tablero, barcos = crear_barcos_aleatorios(tamaño_tablero=10)

def disparar(casilla, tablero):
    """
    Realiza un disparo en la casilla especificada del tablero.
    
    Args:
        casilla (tuple): Tupla (fila, columna) que representa la coordenada del disparo.
        tablero (numpy.ndarray): El tablero donde se realiza el disparo.
    
    Returns:
        numpy.ndarray: El tablero actualizado tras el disparo.
    """
    fila = casilla[0]-1
    columna = casilla[1]-1  # Desempaquetamos la tupla en fila y columna

    # Comprobamos que las coordenadas estén dentro del rango del tablero
    if 0 <= fila < tablero.shape[0] and 0 <= columna < tablero.shape[1]:
        if tablero[fila, columna] == "O":
            print("Tocado")
            tablero[fila, columna] = "X"  # Marcar como tocado
        elif tablero[fila, columna] == "_":
            print("Agua")
            tablero[fila, columna] = "A"  # Marcar como agua
        else:
            print("Ya has disparado a esta casilla.")
    else:
        print("Coordenadas fuera del tablero.")

    return tablero

disparar ((3,6), tablero)
print(tablero)