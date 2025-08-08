import os

archivo = "nuevas_recetas.txt"

# Funciones
def limpiar_pantalla():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Linux, macOS
        os.system('clear')

def cargar_datos(archivo: str) -> list:
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            return contenido.split('\n')
    except FileNotFoundError:
        print("El archivo no existe")
    except IOError:
        print("Error al abrir el archivo")
    finally:
        f.close()

def guardar_datos(archivo: str, receta: str):
    try:
        with open(archivo, 'a', encoding='utf-8') as f:
            f.write(f"{receta}\n")
    except FileNotFoundError:
        print("El archivo no existe")
    except IOError:
        print("Error al abrir el archivo")
    finally:
        f.close()