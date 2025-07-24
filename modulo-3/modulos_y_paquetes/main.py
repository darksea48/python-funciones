import random # Importa la librería "random" (https://www.w3schools.com/python/module_random.asp <- documentación de librería)
import funciones # Importa una librería local que se encuentra en el mismo nivel
import paquetes.saludos # Importa una libreria del paquete local "paquetes"
from paquetes.matematicas import suma, resta # Importa funciones desde el módulo "matemáticas" del paquete "paquetes"
from paquetes.matematicas import * # Importa todas las funciones desde el módulo "matemáticas" del paquete "paquetes"

numero_aleatorio = random.randint(0, 10) # llama a la función randit (el número mínimo y máximo son requeridos)
print(numero_aleatorio)

funciones.hola()

paquetes.saludos.saludar("Douglas")

print("¿Cuánto es 5 + 3?", suma(5, 3))
print("¿Cuánto es 5 - 3?", resta(5, 3))

a = 6
b = 3

print("¿Cuánto es", a, "+", b, "?", suma(a, b))
print("¿Cuánto es", a, "-", b, "?", resta(a, b))