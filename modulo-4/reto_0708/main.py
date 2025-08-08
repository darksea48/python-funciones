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