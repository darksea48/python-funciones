import random
# Retos

# Reto 1
'''
print("Reto 1\n")

input_nombre = input("Ingrese su nombre: ")
input_numero = int(input("Ingrese su número favorito: "))
input_lugar = input("Ingrese su lugar favorito: ")

frases_random = [
    "Hoy es un buen día para ti en {lugar}. Confía en tu número {numero}.",
    "Tal vez hoy no sea el mejor día para visitar {lugar}. Evita pensar en el número {numero}."
    ]

print("")
print(f"¡Hola {input_nombre}!")
print(random.choice(frases_random).format(lugar=input_lugar, numero=input_numero))

print("\n")
'''

# Reto 2
print("Reto 2\n")

input_frase = input("Ingrese una frase: ")
input_letra = input("Ingrese una letra: ")[:1]

while not input_letra.isalpha():
    input_letra = input("Entrada no válida. Por favor, ingrese una letra: ")[:1]

print("")
print("Original:", input_frase)
frase_censurada = input_frase.replace(input_letra.lower(), "X")
frase_censurada = frase_censurada.replace(input_letra.upper(), "X")
print("Censurada:", frase_censurada, "\n")
print("Cantidad de caracteres:", len(input_frase), "\n")

# Reto 3
print("Reto 3\n")

