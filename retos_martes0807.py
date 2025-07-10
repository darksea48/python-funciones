import random

# Reto 1
"""
print("Reto 1 - ADIVINA ADIVINADOR")
print("Adivina el número que estoy pensando\n")

contador = 1

def numero_usuario():
    while True:
        input_num_usuario = input("Escribe un número cualquiera del 1 al 10: ")[:2]
        if input_num_usuario.isnumeric():
            return int(input_num_usuario)
        else:
            print("Entrada no válida. Se permiten solo números.\n")

input_num_usuario = numero_usuario()
num_aleatorio = random.randint(1, 10)

while input_num_usuario != num_aleatorio:
    if input_num_usuario > 10:
        print("Entrada no válida. El número es del 1 al 10.\n")
    elif input_num_usuario == num_aleatorio + 1 or input_num_usuario == num_aleatorio - 1:
        print("Estuviste cerca por UNO!!!!\n")
    else:
        print("NOPE. No es el número que estoy pensando\n")
    contador += 1
    input_num_usuario = numero_usuario()

print("ACERTASTE!!! Era el número", num_aleatorio)
if contador == 1:
    print("LA ACERTASTE A LA PRIMERA!!! ¿ERES ORÁCULO O TIENES UNA BOLA DE CRISTAL?")
else:
    print("La acertaste después de", contador, "intentos")

print("")
"""

# Reto 2
"""
print("Reto 2 - MOOD DEL DÍA\n")

print("¿Cómo estás hoy?")
print("1. Feliz")
print("2. Triste")
print("3. Cansado")
print("4. Emocionado")
print("5. Enojado")
print("6. Hambriento")
print("7. Riendo")

opcion_elegida = input("¿Cómo te sientes?: ")[0:1]


while not opcion_elegida.isnumeric() or int(opcion_elegida) < 1 or int(opcion_elegida) > 7:
    print("No existe esa opción. Favor ingresar otra.")
    opcion_elegida = input("¿Cómo te sientes?: ")[0:1]

opcion_elegida = int(opcion_elegida)

if opcion_elegida == 1:
    print("Me alegro que estés feliz. Hoy el día te sonríe. Contagia tu felicidad al mundo")
elif opcion_elegida == 2:
    print("No estés triste. Un mundo te espera allá afuera con muchas buenas vibras para que disfrutes")
elif opcion_elegida == 3:
    print("¡ÁNIMOS! Ya queda poco para descansar. Tú puedes con todo.")
elif opcion_elegida == 4:
    print("Que bueno que estés emocionado. Espero el día te esté dando buenos momentos para vivir")
elif opcion_elegida == 5:
    print("Tranquilo. Todo lo malo va a pasar. No es bueno estar enojado para tu salud")
elif opcion_elegida == 6:
    print("Ya queda poco para la hora de la comida. No te preocupes. Aguanta un poquito más")
elif opcion_elegida == 7:
    print("Que bueno que estés riendo. Por favor, compartenos tu chiste para que todos podamos reir también contigo")

print("")
"""
# Reto 3
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

suma = num1 + num2 + num3

if num1 == num2 == num3 == 0: # Sería como num1 == 0 and num2 == 0 and num3 == 0
    print("Todos los números son cero.")
elif num1 < 0 or num2 < 0 or num3 < 0:
    print("Al menos uno de los números es negativo.")
elif num1 == num2 == num3 == 100:
    print("¡TRIPLE 100!")
elif num1 == num2 == num3:
    print("Todos los números son iguales.")
elif suma > 300:
    print("La suma es altísima")
elif suma > 200:
    print("La suma es alta")
elif suma > 100:
    print("La suma es media")
elif suma <= 100:
    print("La suma es baja")
else:
    print("Caso no contemplado. Misterio sin resolver.")