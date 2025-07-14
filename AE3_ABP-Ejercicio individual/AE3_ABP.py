from typing import Any, Hashable, Iterable, Optional
import sys
import json

CLIENTES_FILE = "clientes.json"
PRODUCTOS_FILE = "productos.json"

default_clientes = [
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
default_productos = [
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

# Funciones a usar
def cargar_datos(archivo: str, default_data: list) -> list:
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default_data

def guardar_datos(archivo: str, datos: list):
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error al guardar el archivo {archivo}: {e}")

def menu_productos():
    print("==================================================")
    print("PRODUCTOS DISPONIBLES:".center(50))
    print("==================================================")
    for producto in productos:
        print(producto["id_producto"], "-", producto["nombre"], "- Precio:", producto["precio"])

def buscar_dicc(it: Iterable[dict], clave: Hashable, valor: Any) -> Optional[dict]:
    for dicc in it:
        if dicc[clave] == valor:
            return dicc
    return None

def abrir_nueva_compra():
    ingresar_nueva_compra = input("¿Desea realizar otra compra? (S/N): ")[:1].upper().strip()
    while ingresar_nueva_compra not in ["S", "N"]:
        print("Entrada inválida. Por favor, ingrese 'S' para Sí o 'N' para No.")
        ingresar_nueva_compra = input("¿Desea realizar otra compra? (S/N): ")[:1].upper().strip()
    return ingresar_nueva_compra == "S"

# cargas de datos json
clientes = cargar_datos(CLIENTES_FILE, default_clientes)
productos = cargar_datos(PRODUCTOS_FILE, default_productos)

# inicio de programación
dia_promo = False

consulta_dia_promo = input("¿Hoy es día especial de promoción? (S/N): ")[:1].upper().strip()

while consulta_dia_promo not in ["S", "N"]:
    print("Entrada inválida. Por favor, ingrese 'S' para Sí o 'N' para No.")
    consulta_dia_promo = input("¿Hoy es día especial de promoción? (S/N): ")[:1].upper().strip()
if consulta_dia_promo == "S":
    dia_promo = True

nueva_compra = True

while nueva_compra == True:
    while True:
        try:
            cliente = int(input("Ingrese su id de cliente: "))
            break
        except ValueError:
            print("Entrada inválida. Intente nuevamente")

    cliente_encontrado = buscar_dicc(clientes, "id_cliente", cliente)

    if not cliente_encontrado:
        print("\nCliente no encontrado.")
        while True:
            confirmacion = input("¿Desea registrarse como nuevo cliente? (S/N): ").upper().strip()
            if confirmacion in ["S", "N"]:
                break
            print("Entrada inválida. Por favor, ingrese 'S' para Sí o 'N' para No.")

        if confirmacion == "S":
            nombre = input("Ingrese su nombre: ")
            while True:
                try:
                    edad = int(input("Ingrese su edad: "))
                    break
                except ValueError:
                    print("Edad inválida. Debe ser un número.")
            
            nuevo_cliente = {
                "id_cliente": cliente,
                "nombre": nombre,
                "edad": edad,
                "compras_hechas": 0
            }
            clientes.append(nuevo_cliente)
            guardar_datos(CLIENTES_FILE, clientes) # Guardamos el nuevo cliente
            cliente_encontrado = nuevo_cliente  # Asignar el nuevo cliente a la variable
            print(f"\n¡Bienvenido, {nombre}! Cliente registrado con éxito.")

    descuento = 0

    if cliente_encontrado:
        if cliente_encontrado.get("compras_hechas", 0) > 5:
            descuento = descuento + 5

    carrito = []
    compra = True
    cant_articulos = 0

    while compra == True:
        menu_productos()
        while True:
            try:
                producto_comprado = int(input("Ingrese el id del producto que desea comprar (Coloque 0 para terminar de ingresar productos): "))
                break
            except ValueError:
                print("Entrada inválida. Intente nuevamente")

        if producto_comprado != 0:
            producto = buscar_dicc(productos, "id_producto", producto_comprado)
            if not producto:
                print("Producto no encontrado. Ingrese otro producto.")
            else:
                while True:
                    try:
                        n_producto = int(input("Ingrese la cantidad que desea comprar: "))
                        if n_producto > 0:
                            break
                        print("La cantidad debe ser mayor que cero.")
                    except ValueError:
                        print("Entrada inválida. Intente nuevamente")
                producto_agregado = {"id_producto": producto["id_producto"], "nombre": producto["nombre"], "precio": producto["precio"], "cantidad": n_producto,}
                carrito.append(producto_agregado)
                print("Producto agregado al carrito.")
        elif producto_comprado == 0 and len(carrito) > 0: 
            print("==================================================")
            print("Carrito de compras".center(50))
            print(f"Cliente: {cliente_encontrado['nombre']}".center(50))
            print("==================================================")
            for indice, productos_carritos in enumerate(carrito):
                cant_articulos += productos_carritos["cantidad"]
                precio_item = productos_carritos["precio"] * productos_carritos["cantidad"]
                if indice != 0:
                    print("--------------------------------------------------")
                print(productos_carritos["id_producto"], " ", productos_carritos["nombre"], "-- Precio unitario:", productos_carritos["precio"])
                print("Cantidad:", productos_carritos["cantidad"], "- Precio:", precio_item)
            if cant_articulos > 10:
                descuento += 10
            subtotal = 0
            for productos_carritos in carrito:
                subtotal += (productos_carritos["precio"] * productos_carritos["cantidad"])
            if dia_promo:
                descuento += 15
            
            descuento = min(descuento, 30)
            precio_descuento = 0
            if descuento > 0:
                precio_descuento = round((subtotal * descuento) / 100)
            print("==================================================")
            print("Cantidad de artículos: ", cant_articulos)
            print("---------------------------------------------------")
            print("Subtotal:", subtotal)
            print(f"Dcto: {descuento}% - {precio_descuento}")
            print("TOTAL:", subtotal - precio_descuento)
            print("==================================================")
            if cliente_encontrado:    
                cliente_encontrado["compras_hechas"] += 1
                guardar_datos(CLIENTES_FILE, clientes)
            
            # Cerramos la compra
            carrito = []
            compra = False
            cant_articulos = 0
        else:
            print("==================================================")
            print("No hay productos en el carrito.")
            compra = False
        print("Gracias por su visita")
        print("==================================================")
    nueva_compra = abrir_nueva_compra()
else:
    print("Se cierran las ventas para hoy.")
    sys.exit()