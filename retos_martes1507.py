# Reto 1
#Función que reciba un lista y que regrese la suma de los valores mayores a 10
#Ej. [1, 2, 3, 11, 12]. Regresar 23
def sumar_mayores_a_10(lista=[1, 2, 3, 11, 12]):
    suma = 0
    for numero in lista:
        if numero > 10:
            suma += numero
    return suma

resultado = sumar_mayores_a_10()
print(f"La suma entregada por la función sumar_mayores_a_10 es: {resultado}")

lista_reto1 = [4, 9, 18, 13, 10, 1, 52]
resultado = sumar_mayores_a_10(lista_reto1)
print(f"La suma entregada por la función sumar_mayores_a_10 es: {resultado}")

# Reto 2
#Función que reciba un lista y que regrese los dos números mayores
#Ej. [4, 5, 1, 2, 6]. Regresar (6, 5)
def dos_mayores(lista=[4, 5, 1, 2, 6]):
    lista.sort(reverse=True)
    return lista[0], lista[1]

mayor1, mayor2 = dos_mayores()
print(f"Los dos números mayores son: {mayor1} y {mayor2}")

lista_reto2 = [10, 8, 6, 9, 12, 15, 23]
mayor1, mayor2 = dos_mayores(lista_reto2)
print(f"Los dos números mayores son: {mayor1} y {mayor2}")

# Reto 3
#Función que reciba un lista y reemplace cualquier número negativo por 0. Regresa el lista SIN números negativos. Ej. Recibes: [1,5,10,-2], Regresas [1,5,10,0]
def reemplazar_nums_negativos(lista=[1,5,10,-2]):
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = 0
    return lista

print(f"La lista sin números negativos quedaría así: {reemplazar_nums_negativos()}")

lista_reto3 = [14, -5, -10, 12, 15, 1, 2]
print(f"La lista sin números negativos quedaría así: {reemplazar_nums_negativos(lista_reto3)}")

# Reto 4
#Función que reciba una lista y un número, y regrese todas las posiciones (índices) donde aparece ese número Ej. recibe ([1, 5, 3, 5, 2, 5], 5) regresa [1, 3, 5]
def encontrar_indices(lista=[1, 5, 3, 5, 2, 5], numero=5):
    indices = []
    for i in range(len(lista)):
        if lista[i] == numero:
            indices.append(i)
    return indices

print(f"Los índices donde aparece el número 5 son: {encontrar_indices()}")

lista_reto4 = [10, 8, 7, 4, 5, 6, 5 ,8, 9, 5, 4, 6, 5, 1, 8, 2, 1]
print(f"Los índices donde aparece el número 5 son: {encontrar_indices(lista_reto4)}")

numero = 8
print(f"Los índices donde aparece el número {numero} son: {encontrar_indices(lista_reto4, numero)}")