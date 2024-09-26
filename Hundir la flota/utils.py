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

'''DEFINIMOS LA FUNCION DE DISPARAR'''

def disparar (casilla,tablero):
    if tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
    else:
        print("Agua")
        tablero[casilla] = "A"
    return tablero

'''DEFINIMOS LA FUNCION QUE SE EJECUTARA PARA GENERAR EL TABLERO Y LA LISTA DE BARCOS DEL JUGADOR'''

def iniciador_jugador():
    crear_barcos_aleatorios(tamaño_tablero=10)
    return tablero_jugador, barcos_jugador

tablero_jugador, barcos_jugador = iniciador_jugador

'''DEFINIMOS LA FUNCION QUE SE EJECUTARA PARA GENERAR EL TABLERO Y LA LISTA DE BARCOS DE LA MAQUINA'''

def iniciador_maquina():
    crear_barcos_aleatorios(tamaño_tablero=10)
    return tablero_maquina, barcos_maquina

tablero_maquina, barcos_maquina = iniciador_maquina

'''DEFINIMOS UN INICIADOR QUE EJECUTE AMBOS INICIADORES'''

def iniciador():
    iniciador_jugador()
    iniciador_maquina()

'''DEFINIMOS EL TURNO DEL JUGADOR, INTRODUCIRÁ UNA CASILLA CON INPUTS Y SE EJECUTARÁ LA FUNCION DISPARAR PARA USARLOS'''

def turno_jugador(casilla):
    casilla = (fila,columna)
    fila = (int(input("Introduce una fila para disparar"))-1)
    columna = (int(input("Introduce una columna para disparar"))-1)

    disparar(casilla, tablero_maquina)

# '''NO SE CONDICIONA ASÍ, PERO SI ESTUVIESE BIEN LLAMADO EL OUTPOUT DEL DISPARO, REPETIRIA TURNO EL JUGADOR SI FUE TOCADO'''

    if "Tocado":
        turno_jugador()
# '''EN ESTE CASO, AL FALLAR, IRIA LA MAQUINA'''
    else:
        turno_maquina

'''DEFINIMOS LO MISMO CON EL TURNO DE LA MAQUINA'''

def turno_maquina(casilla):
    casilla = (fila,columna)
    fila = (int(input("Introduce una fila para disparar"))-1)
    columna = (int(input("Introduce una columna para disparar"))-1)

    disparar(casilla, tablero_jugador)

    if "Tocado":
        turno_maquina()

    else:
        turno_jugador

'''CREAMOS UNA FUNCION QUE ENBUCLE AMBOS TURNOS. 
SI NO QUEDAN CASILLAS-BARCO ("O") EN ALGUNA DE LAS LISTAS DE JUGADOR O MAQUINA, CHEQUEA EN CUAL NO QUEDAN E INFORMA DEL GANADOR'''

def turnos():
    if ("O" in barcos_jugador) and ("O" in barcos_maquina):
        turno_jugador()
        turno_maquina()
    else:
        if "O" not in barcos_jugador:
            print("Has perdido")
        elif "O" not in barcos_maquina:
            print ("Has ganado!")

'''POSIBLES/FUTURAS MEJORAS:
- enlazar el código funcionando a partir de los disparos (está dividido entre el avance en casa y el avance de la clase)
- contador de vidas que se vayan mostrando
- mejorar los condicionantes de los outputs del turno al disparar segun el output del disparo'''

'''NOTAS:
Código 100% independiente alcanzado en clase:'''

# tablero = crear_tablero(10)  

# def colocar_barcos(tablero):
#     flota = [crear_barco(2)]+[crear_barco(2)]+[crear_barco(2)] + [crear_barco(3)] + [crear_barco(3)] + [crear_barco(4)]
#     print(flota)
#     # flota = [crear_barco(2), crear_barco(2),]
#     # print(flota)
#     for barco in flota:
#         # print(barco)
#         for casilla in barco:
#             if tablero[casilla] == "_" or (len(barco) < (len(tablero[0]) - len(barco))):
#                 try:
#                     for barco in flota:
#                         colocar_barco(barco, tablero)
#                 except:
#                     print("error")
#                     # colocar_barcos(tablero)
#             # elif len (barco) > (len(tablero[1]) - int(barco[1])):
#             #     print("Error")

# #colocar_barcos(tablero)
# colocar_barcos(tablero)
# print(tablero)

'''
GENERA UN MAPA CON BARCOS AUNQUE A VECES SE SUPERPONEN ENTRE SÍ. 
HABRÍA QUE LIMITAR LAS CELDAS YA USADAS CON UN BUCLE QUE CHEQUEE ANTES DE CADA NUEVA IMPLANTACION DE UN BARCO.

'''
    