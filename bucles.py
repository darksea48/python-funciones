# Bucles:

# Bucle for
""" JavaScript
for (let i=2; i<7; i++) {
    codigo a ejecutar
}
"""
# Python
for i in range(5):
    print(i)

for x in range(2, 7):
    print(x)

for numero in range(1, 10, 2):
    print(numero)

print()

print("Prueba con for con variables")
inicio = 2
fin = 8
paso = 3

for num in range(inicio, fin, paso):
    print(num)

print()

print("Prueba")
for z in range(5, -1, 2):
    print(z)
# No lo imprimirá

# Range aplicado a listas o colecciones
lista_numeros = list(range(5))
print(lista_numeros)

print()
# Bucles while

y = 0

while y < 3:
    print(y)
    y += 1
else:
    print("Sentencia terminada", y)

print()

# Break -> termina el bucle independiente de su condición
while True:
    palabra = input("Ingrese una palabra: ")
    palabra = "salir" # lo agregamos para salir de inmediato
    if palabra == "salir":
        break # Termina el bucle

print()

# Continue -> salta una iteración
for letra in "Python":
    if letra == "h":
        continue
    print(letra)

print()

# Ciclos anidados
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

frase = input("Inserte una frase de su gusto: ")
palabras = frase.split()
for palabra in palabras:
    letra = palabra.split()
    for letra in palabra:
        print(letra)
    print("Cantidad de letras:", len(palabra))
    print()
print("Cantidad de palabras:", len(palabras))

print()