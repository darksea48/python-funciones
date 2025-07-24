import random

# reto 1
print("Reto 1")
lista_reto1 = [random.randint(10, 10000) for _ in range(5)]
print(lista_reto1)
print("")
i = 1
for numero in lista_reto1:
    print(f"VALOR {i}")
    print(f"Valor: {numero}")
    print(f"Tipo de dato: {type(numero).__name__}")
    print(f"Cantidad de dígitos: {len(str(numero))}")
    print("")
    i += 1

print("")

# reto 2
print("Reto 2")
lista_reto2 = [random.uniform(-100, 100) for _ in range(3)]
print(lista_reto2)
print("")
i = 1
for numero in lista_reto2:
    print(f"VALOR {i}")
    print(f"Valor: {numero}")
    print(f"Tipo de dato: {type(numero).__name__}")
    print(f"Valor absoluto: {abs(numero)}")
    print(f"Valor con dos decimales: {round(numero, 2)}")
    print(f"Valor entero: {int(numero)}")
    print("")
    i += 1

print("")

print("La diferencia entre int() y round() es que la función int() trunca hasta el valor entero de un número decimal, con la función round() podemos aproximar ya sea a un numero entero o un numero con ciertos decimales deseados.")





