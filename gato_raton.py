##############################
# 1. CONSTANTES / CONFIG
##############################

###### librerias
import os
import time
import random

# tamaño del tablero
n = 10

# posiciones iniciales
gato_inicial = (3,3)
raton_inicial = (0, 0)


##############################
# 2. FUNCIONES BÁSICAS
##############################

def dentro(n, fila, col):                           ##PERMITE MANTENER A LOS PERSONAJES DENTRO DE LA MATRIZ
    return 0 <= fila < n and 0 <= col < n
        


def comando(direccion):                               ##DETERMINAMOS LOS MOVIMIENTOS PARA LOS PERSONAJES
    if direccion == "arriba": return (-1,0)
    elif direccion == "abajo": return (1,0)
    elif direccion == "izquierda": return (0,-1)
    elif direccion == "derecha": return (0,1)

    #elif direccion == "arr-der": return (-1,1)
    #elif direccion == "abj-der": return (1,1)
    #elif direccion == "arr-izq": return (-1,-1)
    #elif direccion == "abj-izq": return (1,-1)
    else:
        return (0,0)


def movimiento_random(fila, col, n):                    ##MOVIMIENTOS ALEATORIOS PARA LOS PRIMEROS TURNOS
    direcciones = ["arriba","abajo","izquierda","derecha"] #,"arr-der","abj-der","arr-izq","abj-izq"
    
    # elige una dirección aleatoria de la lista de direcciones
    random.shuffle(direcciones)
    
    for d in direcciones:
        nueva_pos = aplicar_movimiento((fila, col), d, n)
        if nueva_pos != (fila, col):   # si realmente se movió
            return nueva_pos
    
    return (fila, col)  # fallback (no debería pasar)


def movimientos_posibles(fila, col, n):             ##DEVUELVE UNA LISTA CON MOVIMIENTOS POSIBLES (VALIDOS) 
    direcciones = ["arriba", "abajo", "izquierda", "derecha"] #,"arr-der","abj-der","arr-izq","abj-izq"
    posibles = []
    for movs in direcciones:
        df, dc = comando(movs)
        nueva_fila, nueva_col = fila + df, col + dc
        if dentro (n, nueva_fila,nueva_col):
            posibles.append((nueva_fila,nueva_col))
    return posibles


##############################
# 3. APLICAR MOVIMIENTO
##############################

def aplicar_movimiento(pos, direccion, n):          ##FUNCION QUE ACTUALIZA LAS NUEVAS POSICIONES DE LOS PERSONAJES
    
    fila, col = pos
    df, dc = comando(direccion)
    nueva_fila = fila + df
    nueva_col = col + dc

    if dentro (n,nueva_fila,nueva_col):
        return (nueva_fila,nueva_col)
    else:
        return pos


##############################
# 4. DISTANCIA + EVALUACIÓN
##############################

def distancia_manhattan(gato, raton):               ##Devuelve distancia Manhattan entre dos posiciones
    fg,cg = gato
    fr,cr = raton
    return abs(fg - fr) + abs(cg - cr)


def evaluar_estado(gato, raton):
    if gato == raton:
        return -50
    dist = distancia_manhattan(gato,raton)
    return dist 


##############################
# 5. GENERAR SIGUIENTES ESTADOS
##############################

def generar_siguientes_estados(gato, raton, turno, n):
    estados = []
    direcciones = ["arriba","abajo","izquierda","derecha"]#,"arr-der","arr-izq","abj-der","abj-izq"]

    for d in direcciones:
        if turno == "raton":
            nuevo_raton = aplicar_movimiento(raton, d, n)
            if nuevo_raton != raton:
                estados.append((gato, nuevo_raton))

        else:  # turno gato
            nuevo_gato = aplicar_movimiento(gato, d, n)
            if nuevo_gato != gato:
                estados.append((nuevo_gato, raton))

    return estados


##############################
# 6. MINIMAX
##############################

def minimax(gato, raton, turno, profundidad, n):
    
    if profundidad == 0 or gato == raton:
        return evaluar_estado(gato,raton)
    

    estados_siguientes = generar_siguientes_estados(gato, raton, turno, n)

    if turno == "raton":
        mejor = float("-inf")
        for (nuevo_gato,nuevo_raton) in estados_siguientes:
            valor = minimax (nuevo_gato,nuevo_raton,"gato",profundidad -1,n)
            mejor = max (valor,mejor)
        return mejor    
    else:
        mejor = float("inf")
        for (nuevo_gato,nuevo_raton) in estados_siguientes:
            valor = minimax (nuevo_gato,nuevo_raton,"raton",profundidad -1,n)
            mejor = min (valor,mejor)
        return mejor 
    


##############################
# 7. FUNCIÓN PARA ELEGIR EL MEJOR MOVIMIENTO
##############################

def mejor_movimiento(gato, raton, turno, n):
    candidatos  = generar_siguientes_estados(gato, raton, turno, n)

    if turno == "raton":
        mejor_valor = float("-inf")
        mejor_estado = None


        for (ngato,nraton) in candidatos:
            valor = minimax(ngato,nraton,"gato",0,n)

            if valor > mejor_valor:
                mejor_valor = valor
                mejor_estado = (ngato,nraton)
        
        return mejor_valor,mejor_estado
    
    else:   #turno del gato
        mejor_valor = float("inf")
        mejor_estado = None


        for (ngato,nraton) in candidatos:
            valor = minimax (ngato,nraton,"raton",0,n)

            if valor < mejor_valor:
                mejor_valor = valor
                mejor_estado = (ngato,nraton)
        
        return mejor_valor,mejor_estado



##############################
# 8. LOOP DEL JUEGO / SIMULACIÓN
##############################

def jugar(n, gato_inicial, raton_inicial):
    gato = gato_inicial
    raton = raton_inicial

    turnos_max = 10
    turno_actual = 1

    
    while turno_actual <= turnos_max:

        # --- Ratón mueve ---
        if turno_actual <= 3:
    # Primeros turnos: movimiento aleatorio
            nuevo_raton = movimiento_random(raton[0], raton[1], n)
            nuevo_gato = gato  # el gato aún no mueve

        else:
    # Luego usa Minimax (ratón es MAX)
            valor, (nuevo_gato, nuevo_raton) = mejor_movimiento(gato, raton, "raton", n)

        gato, raton = nuevo_gato, nuevo_raton

        
        imprimir_tablero(n, gato[0], gato[1], raton[0], raton[1])
        
        if gato == raton:
            print("🐱 El gato atrapó al ratón")
            return

        # Turno del Gato
        valor, (nuevo_gato, nuevo_raton) = mejor_movimiento(gato, raton, "gato", n)
        gato, raton = nuevo_gato, nuevo_raton

        
        imprimir_tablero(n, gato[0], gato[1], raton[0], raton[1])
        
        
        
        if gato == raton:
            print("🐱 El gato atrapó al ratón")
            return

        turno_actual += 1

    print("🧀 El ratón sobrevivió la partida.")




def imprimir_tablero(n, gato_fila, gato_columna, raton_fila, raton_columna):
    
    os.system("cls" if os.name == "nt" else "clear") #Linea para hacer limpieza de la pantalla en cada turno
    
    for fila in range(n):
        for columna in range(n):
            if (fila, columna) == (gato_fila, gato_columna):
                x = "G"
            elif (fila, columna) == (raton_fila, raton_columna):
                x = "R"
            else:
                x = "."
            print(x, end=" ")
        print()

    time.sleep(0.7)

##############################
# 9. EJECUCIÓN
##############################

jugar(n, gato_inicial, raton_inicial)


