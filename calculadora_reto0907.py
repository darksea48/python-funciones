# Reto Calculadora

counter = 0

def menu():
    print("==================================================")
    print("CALCULADORA PYTHONIRICA".center(50))
    print("==================================================")
    print("Elige una opción:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números (con validación de 0)")
    print("5. Calcular el cuadrado y cubo de un número")
    print("6. Contar cuántas letras tiene una palabra")
    print("7. Saber si una palabra es corta, media o larga")
    print("8. Calcular el promedio de tres números")
    print("9. Comparar tres números y decir cuál es el mayor")
    print("10. Convertir una palabra a MAYÚSCULAS, minúsculas y contar vocales")
    print("11. Salir de la Súper Calculadora")
    
    while True:
        try:
            opcion = int(input("Ingresa la opción deseada: "))
            return opcion
        except ValueError:
            print("Entrada inválida. Intente nuevamente")

opcion = menu()
counter += 1

def recibir_datos(opcion):
    if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 8 or opcion == 9:
        num1 = float(input("Ingrese el primer número: "))
        while num1 == ValueError:
            print("Entrada inválida. Intente nuevamente")
            num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        while num2 == ValueError:
            print("Entrada inválida. Intente nuevamente")
            num2 = float(input("Ingrese el segundo número: "))
        if num1.is_integer():
            num1 = int(num1)
        if num2.is_integer():
            num2 = int(num2)
        while opcion == 4 and num2 == 0:
            print("El divisor no puede ser cero. Ingresa otro número")
            num2 = float(input("Ingrese el segundo número: "))
            while num2 == ValueError:
                print("Entrada inválida. Intente nuevamente")
                num2 = float(input("Ingrese el segundo número: "))
                if num2.is_integer():
                    num2 = int(num2)
        if opcion == 8 or opcion == 9:
            num3 = float(input("Ingrese el tercer número: "))
            if num3.is_integer():
                num3 = int(num3)
            while num3 == ValueError:
                print("Entrada inválida. Intente nuevamente")
                num3 = float(input("Ingrese el tercer número: "))
                if num3.is_integer():
                    num3 = int(num3)
            return num1, num2, num3
        else:
            return num1, num2
    else:
        palabra = input("Ingrese la palabra deseada: ")
        validar_palabra = palabra.split()
        while palabra.isnumeric() or len(validar_palabra) > 1:
            if palabra.isnumeric():
                print("Entrada inválida. No debes ingresar números. Intente nuevamente")
            elif len(validar_palabra) > 1:
                print("Debes ingresar solo una palabra. Intente nuevamente")
            palabra = input("Ingrese la palabra deseada: ")
            validar_palabra = palabra.split(" ")
        palabra = palabra.lstrip()
        palabra = palabra.rstrip()
        if opcion == 10:
            cortar_vocales = palabra.replace("a", "")
            cortar_vocales = cortar_vocales.replace("e", "")
            cortar_vocales = cortar_vocales.replace("i", "")
            cortar_vocales = cortar_vocales.replace("o", "")
            cortar_vocales = cortar_vocales.replace("u", "")
            return palabra, cortar_vocales
        else:
            return palabra

while opcion != 11:
    if opcion == 1:
        print("SUMAR DOS NÚMEROS\n")
        num1, num2 = recibir_datos(opcion)
        suma = num1 + num2
        if suma.is_integer():
            suma = int(suma)
        print(f"La suma de {num1} y {num2} es {suma}\n")
    elif opcion == 2:
        print("RESTAR DOS NÚMEROS\n")
        num1, num2 = recibir_datos(opcion)
        resta = num1 - num2
        if resta.is_integer():
            resta = int(resta)
        print(f"La resta de {num1} y {num2} es {resta}\n")
    elif opcion == 3:
        print("MULTIPLICAR DOS NÚMEROS\n")
        num1, num2 = recibir_datos(opcion)
        multiplicacion = num1 * num2
        if multiplicacion.is_integer():
            multiplicacion = int(multiplicacion)
        print(f"La multiplicación de {num1} y {num2} es {multiplicacion}\n")
    elif opcion == 4:
        print("DIVIDIR DOS NÚMEROS\n")
        num1, num2 = recibir_datos(opcion)
        division = num1 / num2
        if division.is_integer():
            division = int(division)
        print(f"La división de {num1} y {num2} es {division}\n")
    elif opcion == 5:
        print("CALCULAR EL CUADRADO Y EL CUBO DE UN NÚMERO\n")
        num1 = float(input("Ingrese el número deseado: "))
        if num1.is_integer():
            num1 = int(num1)
        cuadrado = num1 ** 2
        if cuadrado.is_integer():
            cuadrado = int(cuadrado)
        cubo = num1 ** 3
        if cubo.is_integer():
            cubo = int(cubo)
        print(f"El cuadrado de {num1} es {cuadrado}")
        print(f"El cubo de {num1} es {cubo}\n")
        print("¿Quieres elevarlo a otro número?")
        elevar = input("S = Sí / N = No: ")[0:1]
        elevar = elevar.upper()
        while elevar != "S" and elevar != "N":
            print("Entrada inválida. Ingrese nuevamente.")
            elevar = input("S = Sí / N = No: ")[0:1]
            elevar = elevar.upper()
        if elevar == "S":
            num2 = float(input("Ingrese el exponente: "))
            if num2.is_integer():
                num2 = int(num2)
            potencia = num1 ** num2
            if potencia.is_integer():
                potencia = int(potencia)
            print(f"{num1} elevado a {num2} es {potencia}\n")
    elif opcion == 6:
        print("CONTAR LAS LETRAS DE UNA PALABRA\n")
        palabra = recibir_datos(opcion)
        print(f"La palabra {palabra} tiene {len(palabra)} letras")
    elif opcion == 7:
        print("SABER SI UNA PALABRA ES CORTA, MEDIA O LARGA\n")
        palabra = recibir_datos(opcion)
        if len(palabra) < 5:
            print(f"La palabra {palabra} es corta\n")
        elif len(palabra) < 9:
            print(f"La palabra {palabra} es media\n")
        else:
            print(f"La palabra {palabra} es larga\n")
    elif opcion == 8:
        print("CALCULAR EL PROMEDIO DE TRES NÚMEROS\n")
        num1, num2, num3 = recibir_datos(opcion)
        promedio = (num1 + num2 + num3) / 3
        promedio = round(promedio)
        print(f"El promedio de {num1}, {num2} y {num3} es {promedio}\n")        
    elif opcion == 9:
        print("COMPARAR TRES NÚMEROS Y DECIR CUÁL ES EL MAYOR\n")
        """num1, num2, num3 = recibir_datos(opcion)
        lista = [num1, num2, num3]"""
        lista = recibir_datos(opcion)
        mayor = max(lista)
        if mayor.is_integer():
            mayor = int(mayor)
        print(f"El número mayor es {mayor}\n")
    elif opcion == 10:
        print("CONVERTIR UNA PALABRA A MAYÚSCULAS, MINÚSCULAS Y CONTAR VOCALES\n")
        palabra, cortar_vocales = recibir_datos(opcion)
        print(f"La palabra {palabra} en mayúsculas es {palabra.upper()}")
        print(f"La palabra {palabra} en minúsculas es {palabra.lower()}")
        print(f"La palabra {palabra} sin vocales es {cortar_vocales}\n")
    else:
        print("OPCION INVALIDA")
        print("Estas son las opciones disponibles:")
    opcion = menu()
    counter += 1

if opcion == 11:
    print("SALIR DE LA SÚPER CALCULADORA")
    print("¡¡Gracias por usar nuestra SÚPER CALCULADORA!!")
    print("Se ingresó al menú", counter, "veces")