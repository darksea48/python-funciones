# EJERCICIO: Recetario Interactivo con Archivos
# Requerimientos:
# 1. Toda la información debe guardarse en el archivo "nuevas_recetas.txt"
# 2. El usuario puede:
#    - Ver todas las recetas.
#    - Agregar una nueva receta (se guarda en el archivo).
#    - Buscar recetas por posición.
#    - Salir del programa.
# 3. Se deben utilizar:
#    - Manejo de archivos con open(), read(), write(), y close().
#    - Bucles para el menú interactivo.
#    - Condicionales para controlar las opciones del menú.
#    - Manejo de excepciones (FileNotFoundError, IOError).
# 4. Todas las recetas están almacenadas como una receta por línea.

from Clases import *
from funciones import *

# funcion principal
def menu():
    limpiar_pantalla()
    try:
        recetario = Recetario()
        while True:
            print("--- Menú Recetario ---")
            print("1. Ver todas las recetas")
            print("2. Agregar nueva receta")
            print("3. Buscar receta por posición")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                limpiar_pantalla()
                recetario.ver_recetas()
            elif opcion == '2':
                limpiar_pantalla()
                recetario.agregar_receta()
            elif opcion == '3':
                limpiar_pantalla()
                recetario.buscar_receta()
            elif opcion == '4':
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")
    except KeyboardInterrupt:
        print("\n")
        print("Programa interrumpido por el usuario. ¡Hasta luego!\n")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

menu()
