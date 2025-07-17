#--------------------- Segmento de XXXXX
# Crear y gestionar listas de productos disponibles.


productos = {
"Cebolla morada": {"precio": 500, "descripción": "cebolla morada fresca directa de nuestra huerta", "cantidad": 100},
"Mandarina clementina": {"precio": 80, "descripción": "jugosa clementina llena de vitamina C", "cantidad": 300},
"Uva Verde": {"precio": 1000, "descripción": "uva verde sin pepass", "cantidad": 100}


}

def crear_producto (productos):
    nombre = input ("Ingrese el nombre del producto:")
    precio = float(input("Ingrese el precio del producto"))
    descripción = input ("Ingrese la descripción")
    disponibilidad = input ("Indica la cantidad disponible del producto")



# Implementar sets para evitar duplicados en las categorías de productos.
categorias = {"frutas", "verduras", "lacteos"}


# Usar diccionarios para registrar los pedidos de los clientes y su estado.
pedidos = {}

def crear_pedido():
    while True:
        try:
            cliente_buscar = int(input("Ingrese el RUT del cliente: "))
            break
        except ValueError:
            print("Entrada inválida. Intente nuevamente")
    cliente = clientes[]

# Iterar sobre las estructuras de datos para mostrar información actualizada.

# Permitir agregar y eliminar productos de la lista de inventario.

def modificar_inventario(producto):
    if producto not in productos:
        crear_producto(producto)
    else: 
        respuesta = input(f"Desea eliminar el producto {producto} del inventario? ").lower()
        if respuesta == "s":

# Contar el número total de productos disponibles y pedidos registrados.



#-------------------- Segmento de XXXXX





# Utilizar tuplas para almacenar información inmutable como los datos de cada cliente.
clientes = []
def creacion_clientes():
    nombre = input("Ingrese el nombre del cliente: ")
    rut = input("Ingrese el RUT del cliente: ")
    tupla_cliente = (nombre, rut)
    clientes.append(tupla_cliente)

#-------------------- Segmento de XXXXX




#-------------------- Segmento de XXXXX
