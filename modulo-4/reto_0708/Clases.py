from funciones import *

# Clases
class Recetario:
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            pass
    except FileNotFoundError:
        with open(archivo, 'w', encoding='utf-8') as f:
            pass
    finally:
        f.close()

    def __init__(self):
        self.recetas = []

    def ver_recetas(self):
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                recetas = f.readlines()
                if not recetas:
                    print("No hay recetas guardadas.")
                    return
                print("\n--- Todas las Recetas ---")
                for i, receta in enumerate(recetas):
                    print(f"{i+1}. {receta.strip()}")
                print("-------------------------\n")
        except FileNotFoundError:
            print("El archivo de recetas no existe. Crea una receta primero.")
        except IOError:
            print("Error al leer el archivo de recetas.")
        finally:
            f.close()

    def agregar_receta(self):
        nombre_receta = input("Ingresa el nombre de la nueva receta: ")
        guardar_datos(archivo, nombre_receta)
        print(f"Receta '{nombre_receta}' agregada exitosamente.")

    def buscar_receta(self):
        while True:
            try:
                posicion = int(input("Ingresa la posición de la receta que deseas buscar: "))
                recetas = cargar_datos(archivo)
                if recetas and (0 < posicion <= len(recetas)):
                    print(f"\nReceta en la posición {posicion}: {recetas[posicion-1].strip()}\n")
                else:
                    print("No hay recetas en esa posición.")
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
            except TypeError:
                print("No hay recetas para buscar.")
            finally:
                print("".center(50, "-"))
                print()