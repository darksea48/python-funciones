# 1. Básico: imprime todos los números enteros del 0 al 100.
print("Ejercicio 1")
for a in range(101):
    print(a)

print("------------------------------------------------------------------------")
# 2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
print("Ejercicio 2")
for b in range(2, 501, 2):
    print(b)

print("------------------------------------------------------------------------")
# 3. Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
print("Ejercicio 3")
for c in range(1, 101):
    if c % 10 == 0:
        print("baby")
    elif c % 5 == 0:
        print("ice ice")
    else:
        print(c)

print("------------------------------------------------------------------------")
# 4. Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
print("Ejercicio 4")
suma_d = 0
for d in range (0, 500001, 2):
    suma_d += d

print(f"El resultado final es: {suma_d}")

print("------------------------------------------------------------------------")
# 5. Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
print("Ejercicio 5")
for e in range(2024, 2, -3):
    print(e)
print(f"Terminamos en el número: {e}")

print("------------------------------------------------------------------------")
# 6. Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
print("Ejercicio 6")
numInicial = 3
numFinal = 10
multiplo = 2
for f in range(numInicial, numFinal + 1):
    if f % multiplo == 0:
        print(f)
    else:
        continue