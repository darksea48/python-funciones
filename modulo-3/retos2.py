import math

# Reto 3
"""
print("Reto 3")
print("")
input_num1 = float(input("Ingrese el primer número (entero o decimal): "))
input_num2 = float(input("Ingrese el segundo número (entero o decimal): "))

print("")
lista_reto3 = [input_num1, input_num2]
print(lista_reto3)
print("")
i = 1
for valor in lista_reto3:
    print(f"VALOR {i}: {valor}")
    print(f"Raiz cuadrada del valor absoluto: {math.sqrt(abs(valor))}")
    print(f"Valor elevado a la tercera potencia: {pow(valor, 3)}")
    print(f"Valor redondeado hacia arriba: {math.ceil(valor)}")
    print(f"Valor redondeado hacia abajo: {math.floor(valor)}")
    print("")
    i += 1

print("")
print(f"La suma de ambos es: {input_num1 + input_num2}")
print(f"La resta de ambos es: {input_num1 - input_num2}")
print(f"La multiplicación de ambos es: {input_num1 * input_num2}")

if (input_num2 != 0):
    print(f"La división de ambos es: {input_num1 / input_num2}")
else:
    print("El divisor no puede ser cero (0)")

print("")

print(f"El máximo de estos números es: {max(lista_reto3)}")
print(f"El mínimo de estos números es: {min(lista_reto3)}")
print(f"La potencia del primer número elevado al segundo es: {pow(input_num1, int(input_num2))}")

"""

# Reto 4
print("Reto 4")
print("")
input_numeros = int(input("Ingrese la cantidad de números que desea ingresar: "))
lista_reto4 = []

for i in range(input_numeros):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    lista_reto4.append(numero)
    if i == 0:
        resta = numero
    else:
        resta -= numero

print("")
print(f"La cantidad de números ingresados es: {len(lista_reto4)}")
print("")
print(lista_reto4)
print("")
i = 1
for valor in lista_reto4:
    print(f"VALOR {i}: {valor}")
    print(f"Raiz cuadrada del valor absoluto: {math.sqrt(abs(valor))}")
    print(f"Valor elevado a la tercera potencia: {pow(valor, 3)}")
    print(f"Valor redondeado hacia arriba: {math.ceil(valor)}")
    print(f"Valor redondeado hacia abajo: {math.floor(valor)}")
    print("")
    i += 1

print("")
print(f"La suma de todos los números es: {sum(lista_reto4)}")
print(f"La resta de todos los números es: {resta}")
print(f"La multiplicación de todos los números es: {math.prod(lista_reto4)}")
print(f"La división de todos los números es: {math.prod(lista_reto4) / sum(lista_reto4)}")
print("")
print(f"El máximo de estos números es: {max(lista_reto4)}")
print(f"El mínimo de estos números es: {min(lista_reto4)}")
print("")
if input_numeros > 1:
    print(f"La potencia del primer número elevado al segundo es: {pow(lista_reto4[0], int(lista_reto4[1]))}") # Tomará solo los dos primeros números para no complicarnos la vida
else:
    print(f"La potencia del número ingresado entre sí es: {pow(lista_reto4[0], int(lista_reto4[0]))}")
print("")
print(f"El promedio de estos números es: {sum(lista_reto4) / len(lista_reto4)}")