# Listas (en JS: Arrays o Arreglos)
lista_vacia = []
lista_compras = ["leche", "manzanas", "pan"]

print(lista_compras[1])

print(lista_compras)

lista_compras[2] = "marraqueta"

print(lista_compras)

# lista_compras.pop() # Elimina el ultimo valor de la lista si no se le dió un indice indicado a borrar

# print(lista_compras)

lista_compras.append("pollo")

print(lista_compras)

lista_compras.insert(1, "queso")

print(lista_compras)

lista_compras.insert(1, "queso")

print(lista_compras)

# for lista_compra in lista_compras:
#     compra = lista_compra
#     if compra == "manzanas":
#         lista_compras.remove(compra)

print(lista_compras)

print(lista_compras.index("leche"))

lista_con_varios_valores = [1, True, 1.2, "Hola Mundo", [1, 2, 3], {"clave": "valor"}]

print(lista_con_varios_valores)

lista_grande = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista_grande[3:]) # Imprimir desde el indice indicado hasta el final
print(lista_grande[:6]) # Imprimir desde el inicio hasta el indice indicado
print(lista_grande[3:6]) # Imprimir desde el indice indicado hasta el segundo indice indicado

lista_numeros = [6, 2, 3, 3, 5, 4, 9, 8, 5, 7, 3, 1]

print(len(lista_numeros))

print(min(lista_numeros))
print(max(lista_numeros))

print(max(lista_compras))
print(min(lista_compras))

print(sorted(lista_numeros))
lista_numeros.sort()

print(lista_grande[1])

print(lista_grande[-1])

# Tupla -> se definen con paréntesis["()"] o con los valores separados con coma[","]

tupla = ("a", "e", "i", "o", "u")
tupla_sin_parentesis = "a", "e", "i", "o", "u"

print(tupla)
print(tupla_sin_parentesis)

tupla = tupla + ("j", "k", "l")
print(tupla)
print(tupla[2:5])

# Diccionario: pares clave-valor, se define bajo llaves ("{}")

# estudiante = ["Elena", "De Troya", 22, "elena@skillnest.com", "Python", False] # Lista

estudiante1 = {"nombre": "Elena", "apellido": "De Troya", "email": "elena@skillnest.com", "edad": 22}
estudiante2 = {
    "nombre": "Juana",
    "apellido": "De Arco",
    "email": "juana@skillnest.com",
    "edad": 30
}
print(estudiante2["edad"])

estudiante2["edad"] = 31
print(estudiante2)

estudiante2["curso"] = "Python" #Agregando un nuevo par de clave-valor
print(estudiante2)

estudiante1.pop("edad") #Eliminar el elemento con clave "edad"
print(estudiante1)

skillnest = {
    "nombre": "Skillnest",
    "fecha_inicial": "2025-07-11",
    "cursos": [
        {"nombre": "Python", "duracion": 24, "modulos": ["Modulo 1", "Modulo 2", "Modulo 3", "Modulo 4", "Modulo 5"]},
        {"nombre": "Java", "duracion": 16, "modulos": ["Fundamentos de Java", "POO", "Spring", "MVC"]}
    ]
}

skillnest["cursos"][0]["modulos"][2] = "Fundamentos de Python"

#Impresión linda
from pprint import pprint
pprint(skillnest)

# Sets 

ids = {1, 2, 3, 4, 5, 1}
print(ids)

set1 = {2, 3, 4, 5, 6}
set2 = {3, 5, 6, 7, 8}

# Union
print(set1 | set2) # Unión |
print(set1.union(set2)) # Unión .union()

# Interseccion
print(set1 & set2) # Intersección &
print(set1.intersection(set2)) # Intersección .intersection()

# Diferencia
print(set1 - set2) # Diferencia -
print(set1.difference(set2)) # Diferencia .difference()

# Diferencia anidada
print(set1.difference(set2) | set2.difference(set1)) # Diferencia