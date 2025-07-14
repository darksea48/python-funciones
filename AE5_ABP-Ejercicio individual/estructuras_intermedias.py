# Ejercicio Individual AE5_ABP

# 1. Actualizar valores en diccionarios y listas: A continuación se presentan varias estructuras de datos. Realiza los siguientes cambios directamente:
matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambia el valor 3 en matriz por 6.
matriz[1][0] = 6
print(matriz)

# Cambia el nombre del primer cantante por "Enrique Martin Morales".
for cantante in cantantes:
    if cantante["nombre"] == "Ricky Martin":
        cantante["nombre"] = "Enrique Martin Morales"
        break
    else:
        continue
print(cantantes)

# En el diccionario ciudades, reemplaza "Cancún" por "Monterrey".
lista_ciudades_mexico = ciudades["México"]
indice_cancun = lista_ciudades_mexico.index("Cancún")
lista_ciudades_mexico[indice_cancun] = "Monterrey"
print(ciudades)

# En la lista coordenadas, cambia el valor de "latitud" por 9.9355431.
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

print()
# 2. Recorrer una lista de diccionarios:  Utiliza estructuras de control para iterar la lista cantantes. Muestra el nombre y país de cada cantante.
for cantante in cantantes:
    print(f"Nombre: {cantante['nombre']}, País: {cantante['pais']}")

print()
# 3. Obtener valores específicos desde una lista de diccionarios:  Utilizando la lista cantantes, imprime por separado todos los valores correspondientes a la clave "nombre". Luego, imprime todos los valores correspondientes a la clave "pais".
for cantante in cantantes:
    print(f"Nombre: {cantante['nombre']}")
print()
for cantante in cantantes:
    print(f"País: {cantante['pais']}")

print()
# 4. Recorrer un diccionario con listas como valores:  Dado el siguiente diccionario:
costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
# Realiza un recorrido del diccionario que imprima lo siguiente:

# La cantidad de elementos en cada lista seguida del nombre de la clave en mayúsculas.
for clave, lista_valores in costa_rica.items():
    print(f"{len(lista_valores)} {clave.capitalize()}")

print()

# Cada elemento de la lista correspondiente, en líneas separadas.
for i in costa_rica.keys():
    print(i.capitalize())
    for j in costa_rica[i]:
        print(j)
    print()