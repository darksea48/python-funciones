import json
import sys
import datetime


# Las palabras serán un set de palabras, separadas en categorías cargadas en un JSON.
diccionario_json = "tareas.json"

def cargar_datos(archivo: str) -> list:
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error en la carga del JSON. Favor contactar con el administrador.")
        sys.exit()

def guardar_datos(archivo: str, datos: list):
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error al guardar el dato en el archivo {archivo}: {e}")

tareas = cargar_datos(diccionario_json)

def menu_mostrar():
    print("==================================================")
    print("GESTOR DE TAREAS".center(50))
    print("==================================================")
    print("Elige una opción:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("9. Salir")

def menu_opcion():
    menu_mostrar()
    opcion = (input("Ingresa la opción deseada: "))[:1]
    while opcion != "1" and opcion != "2" and opcion != "9":
        print("Entrada inválida. Intente nuevamente")
        menu_mostrar()
        opcion = (input("Ingresa la opción deseada: "))[:1]
    else:
        opcion = int(opcion)
    return opcion

def ver_tareas():
    print("Lista de tareas:")
    print("".rjust(100, "-"))
    for tarea in tareas:
        print(f"ID Tarea: {tarea['id_tarea']} - Fecha de creación: {tarea['fecha_creacion']} - Fecha límite: {tarea['fecha_limite']} - Completada: {tarea['completada']}")
        print(f"Tarea: {tarea['nombre']}")
        print(f"Descripción: {tarea['descripcion']}")
        print("".rjust(100, "-"))

def crear_tarea(nombre_tarea, descripcion_tarea, fecha_limite=None):
    nueva_tarea = {
        "id_tarea": len(tareas) + 1,
        "nombre_tarea": nombre_tarea,
        "descripcion_tarea": descripcion_tarea,
        "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "fecha_limite": fecha_limite,
        "completada": "No iniciada"
    }
    tareas.append(nueva_tarea)
    guardar_datos(diccionario_json, tareas)

opcion = menu_opcion()

while opcion != 9:
    if opcion == 1:
        nombre_tarea = input("Ingrese el nombre de la tarea: ")
        descripcion_tarea = input("Ingrese la descripción de la tarea: ")
        pregunta_fecha = input("¿La tarea tiene fecha límite? (s/n): ")[:1].lower()
        fecha_limite = None
        while pregunta_fecha != "s" and pregunta_fecha != "n":
            print("Entrada inválida. Intente nuevamente")
            pregunta_fecha = input("¿La tarea tiene fecha límite? (s/n): ")[:1].lower()
        if pregunta_fecha == "s":
            while True:
                try:
                    fecha_limite = input("Ingrese la fecha de la tarea: ")
                    fecha_limite = datetime.datetime.strptime(fecha_limite, "%Y-%m-%d")
                    break  # Sale del bucle si el formato es correcto
                except ValueError:
                    print("Entrada inválida. El formato debe ser AAAA-MM-DD. Intente nuevamente.")
        else:
            fecha_limite = "No aplica"
        crear_tarea(nombre_tarea, descripcion_tarea, fecha_limite)
    elif opcion == 2:
        ver_tareas()
        subopcion = input("¿Quieres realizar cambios a una tarea? (s/n): ")[:1].lower()
        while subopcion != "s" and subopcion != "n":
            print("Entrada inválida. Intente nuevamente")
            subopcion = input("¿Quieres seleccionar una tarea específica? (s/n): ")[:1].lower()
        while subopcion == "s":
            continue# aqui hay que agregar funcion para modificar una tarea, ya sea completar o modificar datos de la tarea
        else:
            pass
    opcion = menu_opcion()
else:
    print("Gracias por usar el gestor de tareas. Que tengas buen día.")
    sys.exit()