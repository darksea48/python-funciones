#  1. Actualizar valores en diccionarios y listas
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

# Cambia el valor de 3 en matriz por 6.
def cambio_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 3:
                matriz[i][j] = 6
                break
    print(matriz)

cambio_matriz()

# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
def cambio_nombre_cantante():
    for i in range(len(cantantes)):
        if cantantes[i]["nombre"] == "Ricky Martin":
            cantantes[i]["nombre"] = "Enrique Martin Morales"
            break
    print(cantantes)

cambio_nombre_cantante()

# En ciudades, cambia “Cancún” por “Monterrey”
def cambio_ciudad():
    for i in ciudades:
        for j in range(len(ciudades[i])):
            if ciudades[i][j] == "Cancún":
                ciudades[i][j] = "Monterrey"
                break
    print(ciudades)

cambio_ciudad()

# En las coordenadas, cambia el valor de “latitud” por 9.9355431
def cambio_coordenadas(coordenada=9.9355431):
    for i in range(len(coordenadas)):
        if coordenadas[i]["latitud"] == 8.2588997:
            coordenadas[i]["latitud"] = coordenada
            break
    print(coordenadas)

cambio_coordenadas()
print()
# 2. Iterar a través de una lista de diccionarios: Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente.
cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"},
   {"nombre": "José José", "pais": "México"},
   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"},
   {"nombre": "Kaarija", "pais": "Finlandia"},
   {"apodo": "Er niño", "pais": "España"} # El nombre artístico es Raphael
]

def iterarDiccionario(lista):
    for i in lista:
        frase = ""
        for clave, valor in i.items():
            if frase == "":
                frase += f"{clave.title()} - {valor}"
            else:
                frase += f", {clave.title()} - {valor}"
        print(frase)

iterarDiccionario(cantantes)
print()
# 3. Obtener valores de una lista de diccionarios Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios. La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista
def iterarDiccionario2(llave, lista):
    for i in lista:
        try:
            print(i[llave])
        except KeyError:
            print("No existe este dato en este registro.")

iterarDiccionario2("nombre", cantantes)
print()
iterarDiccionario2("pais", cantantes)
print()

# 4. Iterar a través de un diccionario con valores de lista Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.
costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
chile = {
   "ciudades": ["Santiago", "Concepción", "Viña del Mar", "Punta Arenas", "Ñuble", "Valdivia", "Osorno"],
   "comidas": ["empanada de pino", "cazuela", "curanto", "mote con huesillos", "terremoto", "charquicán", "pastel de choclo"],
   "localidades": ["Torres del Paine", "Salto del Laja", "Cerro San Cristobal", "Cerro Santa Lucía"],
   "regiones": ["Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama", "Coquimbo", "Valparaíso", "Libertador Gral. Bernardo O’Higgins", "Maule", "Biobío", "Araucanía", "Los Ríos", "Los Lagos", "Aysén del Gral. Carlos Ibáñez del Campo", "Magallanes y Antártica Chilena", "Metropolitana de Santiago", "Ñuble"]
}

def imprimirInformacion(diccionario):
    for clave, lista_valores in diccionario.items():
        print(f"{len(lista_valores)} {clave.upper()}")
        for valor in lista_valores:
            print(valor)
        print()

imprimirInformacion(costa_rica)
imprimirInformacion(chile)

import locale

def imprimirInformacionOrdenada(diccionario):
    locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')

    for clave, lista_valores in diccionario.items():
        print(f"{len(lista_valores)} {clave.upper()}")
        for valor in sorted(lista_valores, key=lambda item: locale.strxfrm(item[0])):
            print(valor)
        print()
    

imprimirInformacionOrdenada(costa_rica)
imprimirInformacionOrdenada(chile)