import json
import sys
import datetime
import random
import os

# Las tareas estarán guardadas en un archivo JSON.
diccionario_json = "tareas.json"

def limpiar_pantalla():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Linux, macOS
        os.system('clear')
    
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
    print("2. Ver y/o modificar tareas")
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
    print("".rjust(100, "-"))
    print("LISTA DE TAREAS:")
    print("".rjust(100, "-"))
    hoy = datetime.date.today()  # Obtenemos la fecha actual
    for tarea in tareas:
        fecha_limite_str = tarea['fecha_limite']
        print(f"ID Tarea: {tarea['id_tarea']} - Fecha de creación: {tarea['fecha_creacion']} - Fecha límite: {fecha_limite_str} - Completada: {tarea['completada']}")
        print(f"Tarea: {tarea['nombre']}")
        try:
            print(f"Descripción: {tarea['descripcion']}")
        except KeyError:
            pass

        if fecha_limite_str != "Sin fecha límite" and tarea['completada'] != "Completada":
            fecha_solo_str = fecha_limite_str.split(' ')[0]  # Nos quedamos con la fecha y eliminamos la hora
            fecha_limite_date = datetime.datetime.strptime(fecha_solo_str, "%Y-%m-%d").date()  # Convertimos a objeto datetime.date
            if fecha_limite_date < hoy:
                print("¡¡ ESTÁS ATRASADO CON ESTA TAREA !!")
            elif fecha_limite_date == hoy:
                print("ESTÁS EN LA FECHA LÍMITE DE ESTA TAREA")
        print("".rjust(100, "-"))

def crear_tarea():
    print("Crear tarea")
    print("".rjust(100, "-"))
    while True:
        consultar_id_personalizado = input("¿Quieres generar de manera aleatoria el ID de la tarea? (s/n/q para volver al menú principal): ")[:1].lower()
        if consultar_id_personalizado not in ["s", "n", "q"]:
            print("Entrada inválida. Intente nuevamente")
            continue
        elif consultar_id_personalizado == "q":
            return
        elif consultar_id_personalizado == "s":
            id_tarea = random.randint(1000, 9999)
            while any(tarea['id_tarea'] == id_tarea for tarea in tareas):
                id_tarea = random.randint(1000, 9999)
            else:
                break
        elif consultar_id_personalizado == "n":
            while True:
                id_tarea_str = input("Ingresa el ID de la tarea (debes ingresar cuatro dígitos) (o 'q' para volver al menú principal): ")
                if id_tarea_str.lower() == 'q':
                    return
                if not id_tarea_str.isdigit() or len(id_tarea_str) != 4:
                    print("Entrada inválida. Debes ingresar exactamente cuatro caracteres numéricos.")
                    continue
                else:
                    id_tarea = int(id_tarea_str)
                    
                if not 1000 <= id_tarea <= 9999:
                    print("Entrada inválida. El ID debe ser un número de cuatro dígitos entre 1000 y 9999.")
                    continue
                if any(tarea['id_tarea'] == id_tarea for tarea in tareas):
                    print("Ya existe una tarea con ese ID. Intenta nuevamente.")
                    continue
                break
            break
    nombre_tarea = input("Ingresa el nombre de la tarea: ")
    descripcion_tarea = input("Ingresa la descripción de la tarea: ")
    pregunta_fecha = input("¿La tarea tiene fecha límite? (s/n/q para volver al menú principal): ")[:1].lower()
    while pregunta_fecha != "s" and pregunta_fecha != "n":
        if pregunta_fecha == "q":
            return
        print("Entrada inválida. Intenta nuevamente")
        pregunta_fecha = input("¿La tarea tiene fecha límite? (s/n): ")[:1].lower()
    if pregunta_fecha == "s":
        while True:
            try:
                fecha_limite_str = input("Ingrese la fecha de la tarea (dd-mm-yyyy): ") # Validamos el formato convirtiendo a datetime
                fecha_limite_dt = datetime.datetime.strptime(fecha_limite_str, "%d-%m-%Y") # Guardamos la fecha como un string en formato YYYY-MM-DD
                fecha_limite = fecha_limite_dt.strftime("%Y-%m-%d")
                break
            except ValueError:
                print("Entrada inválida. El formato debe ser dd-mm-yyyy. Intente nuevamente.")
    else:
        fecha_limite = "Sin fecha límite"
    nueva_tarea = {
        "id_tarea": id_tarea,
        "nombre": nombre_tarea,
        "descripcion": descripcion_tarea,
        "fecha_creacion": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "fecha_limite": fecha_limite,
        "completada": "No iniciada"
    }
    tareas.append(nueva_tarea)
    guardar_datos(diccionario_json, tareas)
    print("Tarea creada exitosamente.")

def modificar_tarea():
    seleccionar_tarea = "s"
    while seleccionar_tarea == "s":
        ver_tareas()
        # Bucle mejorado para seleccionar una tarea de forma más clara
        tarea = None
        while True:
            id_modificar_str = input("Ingresa el ID de la tarea que deseas modificar (o 'q' para volver al menú principal): ")
            if id_modificar_str.lower() == 'q':
                return
            if not id_modificar_str.isdigit():
                print("ID inválido. Debe ser un número.")
                continue

            id_modificar = int(id_modificar_str)
            tarea = next((t for t in tareas if t['id_tarea'] == id_modificar), None)
            if tarea:
                break  # Tarea encontrada, salimos del bucle de selección
            print("Tarea no encontrada.")
        limpiar_pantalla()
        print("".rjust(100, "-"))
        print(f"Tarea seleccionada: {tarea['id_tarea']} - {tarea['nombre']}")
        print(f"{tarea['descripcion']}")
        print("".rjust(100, "-"))
        print("¿Qué deseas realizar con esta tarea?")
        print("1. Cambiar estado de tarea")
        print("2. Modificar nombre")
        print("3. Modificar descripción")
        print("4. Modificar fecha límite")
        print("5. Eliminar tarea")
        print("8. Cancelar acción con esta tarea")
        print("9. Volver al menú principal")
        print("".rjust(100, "-"))
        opcion = input("Elige una opción: ")
        while opcion not in ["1", "2", "3", "4", "8", "9"]:
            print("Opción inválida.")
            opcion = input("Elige una opción: ")
        opcion = int(opcion)
        if opcion == 1:
            print("".rjust(100, "-"))
            print("1. En progreso")
            print("2. Completada")
            print("".rjust(100, "-"))
            estado_input = input("Elige una opción (o 'q' para volver al menú principal): ")
            while estado_input not in ["1", "2"]:
                if estado_input.lower() == 'q':
                    return
                print("Opción inválida.")
                estado_input = input("Elige una opción: ")
            estado_input = int(estado_input)
            if estado_input == 1:
                tarea['completada'] = "En progreso"
            elif estado_input == 2:
                tarea['completada'] = "Completada"
            print("El estado de la tarea fue cambiado exitosamente.")
        elif opcion == 2 or opcion == 3:
            nuevo_valor = input("Inserte nuevo valor (si no desea modificarlo, presione enter): ")
            if nuevo_valor != "":
                if opcion == 2:
                    tarea['nombre'] = nuevo_valor
                    print("Nombre modificado.")
                elif opcion == 3:
                    tarea['descripcion'] = nuevo_valor
                    print("Descripción modificada.")
            else:
                print("Acción cancelada.")
        elif opcion == 4:
            while True:
                try:
                    print("Ingrese la nueva fecha de la tarea (dd-mm-yyyy)")
                    print("(Si no desea modificarlo, presione enter; si desea dejarlo sin fecha límite, coloque 'No'; si quiere salir, escriba 'q')")
                    fecha_limite_str = input("La nueva fecha (dd-mm-yyyy): ")
                    # Validamos el formato
                    if fecha_limite_str == "":
                        print("No se ha modificado la fecha.")
                        break
                    elif fecha_limite_str == "No":
                        tarea['fecha_limite'] = "Sin fecha límite"
                        print("Fecha límite modificada.")
                        break
                    elif fecha_limite_str.lower() == 'q':
                        return
                    fecha_limite = datetime.datetime.strptime(fecha_limite_str, "%d-%m-%Y")
                    tarea['fecha_limite'] = fecha_limite.strftime("%Y-%m-%d")
                    print("Fecha modificada.")
                    break
                except:
                    print("Entrada inválida. Intente nuevamente")
        elif opcion == 5:
            tareas.remove(tarea)
            print("Tarea eliminada.")
        elif opcion == 8:
            print("Acción cancelada.")
        else:
            print("Volverás al menú principal.")
            return
        guardar_datos(diccionario_json, tareas)
        seleccionar_tarea = input("¿Quieres realizar cambios a otra tarea? (s/n): ")[:1].lower()
        while seleccionar_tarea != "s" and seleccionar_tarea != "n" and seleccionar_tarea != "q":
            print("Entrada inválida. Intente nuevamente")
            seleccionar_tarea = input("¿Quieres realizar cambios a otra tarea? (s/n): ")[:1].lower()
    else:
        return

limpiar_pantalla()
opcion = menu_opcion()

while opcion != 9:
    limpiar_pantalla()
    if opcion == 1: # Opción 1 (Crear Tarea)
        crear_tarea()
    elif opcion == 2: # Opción 2 (Ver y/o modificar tareas)
        modificar_tarea()
    limpiar_pantalla()
    opcion = menu_opcion()
else:
    print("Gracias por usar el gestor de tareas. Que tengas buen día.")
    sys.exit()