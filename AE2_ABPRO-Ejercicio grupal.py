import pprint

eventos = []
usuarios = []
equipos = []

"""
encendido = True
def menu():
    print("Selecciona la acción que deseas realizar")
    print("1. Crear evento")
    print("2. Crear usuario")
    print("3. Crear equipo")
    print("4. Inscribir usuario a evento")
    print("5. Asignar usuario a equipo")
    print("6. Consultar eventos por estado")
    print("7. Salir")

def opcion():
    menu()
    opcion = input("Ingresa la opción deseada: ")
    return opcion

def funciones(opcion):
    if opcion == "1":
        print("Crear evento")
    elif opcion == "2":
        print("Crear usuario")
    elif opcion == "3":
        print("Crear equipo")
    elif opcion == "4":
        print("Inscribir usuario a evento")
    elif opcion == "5":
        print("Asignar usuario a equipo")
    elif opcion == "6":
        print("Consultar eventos por estado")
    elif opcion == "7":
        print("Salir")
        encendido = False
    else:
        print("Opción inválida")
        
    return encendido

while encendido:
    opcion()
    funciones(opcion())

"""
def menu():
    flag = True
    contador = 1
    while flag:
        print("Selecciona la acción que quieres realizar:")
        print("1.- Crear evento")
        print("2.- Crear usuario")
        print("3.- Crear equipo")
        print("4.- Inscribir usuario a evento")
        print("5.- Asignar usuario a equipo")
        print("6.- Consultar eventos por estado")
        print("7.- Salir")
        opcion = input("Ingresa la opción: ")

        if opcion == "1":
            print("CREAR EVENTO")
            nombre = input("Ingrese el nombre del evento: ")
            tipo = input("Ingrese el tipo del evento: ")
            fecha = input("Ingrese la fecha del evento: ")
            evento = {
                "Nombre": nombre,
                "Tipo": tipo,
                "Fecha": fecha,
                "Estado": "Programado",
                "Usuarios": []
            }
            eventos.append(evento)
            print("EVENTO CREADO\n")
        elif opcion == "2":
            print("CREAR USUARIO")
        elif opcion == "3":
            print("CREAR EQUIPO")
        elif opcion == "4":
            print("INSCRIBIR USUARIO A EVENTO")
        elif opcion == "5":
            print("ASIGNAR USUARIO A EQUIPO")
        elif opcion == "6":
            print("CONSULTAR EVENTOS POR ESTADO")
        elif opcion == "7":
            print("SALIR")
            flag = False
        else:
            print("OPCION INVALIDA")
        
        contador += 1
    print(f"Se ingresó al menú {contador} veces")
    pprint.pprint(eventos)

menu()