# Booleans
mayor_edad = True
tiene_bigote = False

# Numerales
edad = 31 # Enteros (sin decimales)
altura = 1.75 # Flotantes (con decimales)

edad_flotante = float(edad)
print(edad_flotante)
altura_entero = int(altura)
print(altura_entero)

decimal = 132.513
print(int(decimal)) # int trunca al número entero: 132
print(round(decimal)) # round redondea al número entero más cercano: 133

pi = 3.141592653589793238462643
print(round(pi, 4)) # 3.1416 / round con dos parámetros hace que redondee hasta una cierta cantidad de decimales

numero_negativo = -10
print(abs(numero_negativo)) # abs devuelve el valor absoluto de una variable tipo numérica

numero_al_cuadrado = pow(2, 2) # pow(base, exponente) emula una potencia
print(numero_al_cuadrado)

numero_maximo = max(1, 2, 3, 4, 5) # recibe n cantidad de números y regresa el número mayor
print(numero_maximo)

numero_minimo = min(1, 2, 3, 4, 5) # recibe n cantidad de números y regresa el número menor
print(numero_minimo)

import random # importamos la librería "random"

num_aleatorio = random.randint(5, 10) # número entero aleatorio entre 5 y 10
print(num_aleatorio)

decimal_aleatorio = random.uniform(-10, 10) # número decimal aleatorio entre -10 y 10
print(decimal_aleatorio)

numero_aleatorio_neg_pos = random.randrange(-10, 10) # número entero aleatorio entre -10 y 10
print(numero_aleatorio_neg_pos)


# Retos

