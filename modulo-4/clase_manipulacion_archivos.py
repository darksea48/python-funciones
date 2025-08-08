"""
lista_estudiantes = [
    { "nombre": "Elena", "apellido": "De Troya", "edad": 25 },
    { "nombre": "Juana", "apellido": "De Arco", "edad": 30 },
    { "nombre": "Pedro", "apellido": "Páramo", "edad": 33 },
]

lista_estudiantes[0]["edad"] += 1
print(lista_estudiantes)
"""

# r = leer, w = escribir, a = agregar, x = crear
try:
    recetario = open("recetario.txt", "w") # w -> write, si no existe, lo crea; si existe, lo sobreescribe
    recetario.write("Empanada de pino\n")
    recetario.write("Pastel de choclo\n")
    recetario.write("Tortilla española\n")
except FileNotFoundError:
    print("El archivo no existe")
except IOError:
    print("Error al abrir el archivo")
finally:
    recetario.close()

try:
    recetario = open("recetario.txt", "r") # r -> read, permisos de lectura
    print("Recetario actual:")
    print(recetario.read())
except FileNotFoundError:
    print("El archivo no existe")
except IOError:
    print("Error al abrir el archivo")
finally:
    recetario.close()

try:
    recetario = open("recetario.txt", "r")
    recetas = recetario.readlines() # readlines -> lee el archivo y lo convierte en una lista de strings
    print("Recetas:")
    print("Receta en el índice 1:", recetas[1])
except FileNotFoundError:
    print("El archivo no existe")
except IOError:
    print("Error al abrir el archivo")
finally:
    recetario.close()

try:
    recetario = open("recetario.txt", "a") # a -> append, permite agregar contenido al archivo
    recetario.write("Ensalada Rusa\n")
    recetario.write("Mote con huesillos\n")
    recetario.write("Cazuela de ave\n")
except FileNotFoundError:
    print("El archivo no existe")
except IOError:
    print("Error al abrir el archivo")
finally:
    recetario.close()

try:
    recetario = open("recetario.txt", "r+") # r+ -> read and write, permite leer y escribir en el archivo (el archivo debe existir)
    contenido_existente = recetario.read()
    recetario.seek(0)
    recetario.write("MI RECETARIO\n")
    recetario.write(contenido_existente)
except FileNotFoundError:
    print("El archivo no existe")
except IOError:
    print("Error al abrir el archivo")
finally:
    recetario.close()

try:
    recetario = open("recetario.txt", "r")
    lineas_recetas = recetario.readlines()
    print("Lista de recetas:")
    for linea in lineas_recetas:
        print(f"Receta: {linea}")
except FileNotFoundError:
    print("El archivo no existe")
except IOError:
    print("Error al abrir el archivo")
finally:
    recetario.close()
