# Laberinto del Gato y el Ratón

Proyecto desarrollado como parte del desafío de simulación estratégica con el algoritmo **Minimax**.  
La misión: crear un entorno donde un **ratón intenta escapar** y un **gato intenta atraparlo**, ambos tomando decisiones inteligentes dentro de un tablero bidimensional.

---

## Descripción del Proyecto

El programa simula un juego por turnos entre dos agentes:

- **Ratón (MAX):** intenta maximizar la distancia respecto al gato.
- **Gato (MIN):** intenta minimizar esa distancia y atraparlo.

La inteligencia de ambos se basa en **Minimax**, un algoritmo clásico utilizado en juegos de estrategia como ajedrez y tic-tac-toe.

El tablero puede ser de cualquier tamaño (por defecto, 10×10), y los personajes pueden moverse en **4 direcciones** (verticales, horizontales y diagonales).

---

##  Características Principales

### ✔ Tablero dinámico  
Representado mediante coordenadas `(fila, columna)`, compatible con distintos tamaños.

### ✔ Movimiento inteligente  
Ambos agentes usan Minimax con una profundidad de búsqueda configurable.

### ✔ Movimiento aleatorio inicial  
Durante los primeros turnos, el ratón se mueve al azar antes de “despertar” su inteligencia.  
Esto cumple con el requisito del desafío de simular una fase inicial menos racional.

### ✔ Evaluación basada en distancia Manhattan  
La heurística principal mide qué tan lejos está el ratón del gato.

### ✔ Simulación visual  
El tablero se imprime turno a turno, limpiando la pantalla para mostrar la partida en tiempo real.

---

##  ¿Cómo funciona el algoritmo?

### 🔹 Generación de estados  
Cada posible movimiento del gato o ratón produce un nuevo estado del juego.

### 🔹 Minimax recursivo  
- El **ratón** (MAX) elige la jugada que maximiza la distancia.  
- El **gato** (MIN) elige la jugada que minimiza la distancia.  

Si se alcanza la profundidad límite o el gato atrapa al ratón, se evalúa el estado.

---

## 🔁 Reglas de Finalización del Juego

El juego puede terminar de dos maneras:

1. **El gato alcanza la misma posición que el ratón.**
2. **El ratón sobrevive un número determinado de turnos**.

---

##  Estructura del Código

/GATO_RATON/
│
├── gato_raton.py # Código principal del juego
└── README.md # Este archivo

Las funciones están organizadas por secciones:

1. Constantes y configuración  
2. Funciones básicas  
3. Movimiento y validación  
4. Distancia y heurística  
5. Generación de estados  
6. Algoritmo Minimax  
7. Selección de mejor movimiento  
8. Simulación completa  
9. Ejecución del programa  

---

## Cosas que funcionaron muy bien

- La modularización del código permitió mantener todo ordenado y fácil de entender.  
- Minimax con profundidad limitada mostró resultados sólidos sin comprometer rendimiento.  
- El movimiento aleatorio inicial del ratón le dio un comportamiento más natural y cumplió con los requisitos del desafío.  
- El uso de Manhattan como heurística fue simple y efectivo.

---

## Cosas que fueron un desafío

- Ajustar la profundidad del árbol para no afectar demasiado los tiempos de ejecución.  
- Encontrar un equilibrio entre movimiento aleatorio y estrategia.  
- Asegurar que ningún personaje saliera del tablero (validaciones con `dentro()` y `aplicar_movimiento()`).

---

## Mi mejor momento

Cuando entendí que Minimax no busca “el mejor movimiento absoluto”, sino **la mejor decisión basada en suposiciones recursivas** del oponente.  
Ese insight me ayudó a resolver varios errores lógicos y mejorar la calidad de las decisiones.

---

## ¿Cómo se ejecuta?

En terminal:
python gato_raton.py

