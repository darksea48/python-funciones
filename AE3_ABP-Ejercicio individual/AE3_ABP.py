clientes = [
    {
        "id_cliente": 11111111,
        "nombre": "Cliente 1",
        "edad": 30,
        "compras_hechas": 5,
    },
    {
        "id_cliente": 12345678,
        "nombre": "Cliente 2",
        "edad": 25,
        "compras_hechas": 2,
    },
    {
        "id_cliente": 87654321,
        "nombre": "Cliente 3",
        "edad": 40,
        "compras_hechas": 1,
    },
]
productos = [
    {
        "id_producto": 1,
        "nombre": "Producto 1",
        "precio": 10,
    },
    {
        "id_producto": 2,
        "nombre": "Producto 2",
        "precio": 200,
    },
    {
        "id_producto": 3,
        "nombre": "Producto 3",
        "precio": 150,
    },
    {
        "id_producto": 4,
        "nombre": "Producto 4",
        "precio": 50,
    },
    {
        "id_producto": 5,
        "nombre": "Producto 5",
        "precio": 300,
    },
    {
        "id_producto": 6,
        "nombre": "Producto 6",
        "precio": 100,
    },
    {
        "id_producto": 7,
        "nombre": "Producto 7",
        "precio": 20,
    },
    {
        "id_producto": 8,
        "nombre": "Producto 8",
        "precio": 15,
    },
    {
        "id_producto": 9,
        "nombre": "Producto 9",
        "precio": 5,
    },
    {
        "id_producto": 10,
        "nombre": "Producto 10",
        "precio": 30,
    },
    {
        "id_producto": 11,
        "nombre": "Producto 11",
        "precio": 25,
    },
]

try:
    cliente = int(input("Ingrese su id de cliente: "))
except ValueError:
    while cliente is ValueError:
        print("Entrada inválida. Intente nuevamente")
        cliente = int(input("Ingrese su id de cliente: "))

cliente_encontrado = clientes.get("id_cliente")

if cliente_encontrado is KeyError:
    print("Cliente no encontrado. ¿Quieres agregarlo?")
    confirmacion = input("S = Sí / N = No: ")[0:1]
    confirmacion = confirmacion.upper()
    while confirmacion != "S" and confirmacion != "N":
        print("Entrada inválida. Ingrese nuevamente.")
        confirmacion = input("S = Sí / N = No: ")[0:1]
    if confirmacion == "S":
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        nuevo_cliente = {
            "id_cliente": cliente,
            "nombre": nombre,
            "edad": edad,
            "compras_hechas": 0
        }
        nuevo_cliente.append()

descuento = 0