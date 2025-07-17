# Juego ahorcado
import random
import json
import sys

# Las palabras serán un set de palabras, separadas en categorías cargadas en un JSON.
set_palabras_json = "set_palabras_ahorcado.json"

def cargar_datos(archivo: str) -> list:
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        """diccionario_default = {
            "frutas": ["manzana", "pera", "durazno", "uva", "sandia", "frutilla", "piña", "naranja"],
            "animales": ["gato", "perro", "leon", "tigre", "elefante", "jirafa", "gorila", "hipopotamo", "leopardo", "oso pardo", "oso panda", "oso polar"],
            "colores": ["rojo", "verde", "azul", "amarillo", "morado", "blanco", "negro", "gris", "celeste", "naranja"],
            "paises": ["chile", "argentina", "brasil", "uruguay", "mexico", "francia", "estados unidos", "italia", "alemania", "japon", "colombia", "ecuador", "bolivia", "peru", "venezuela", "paraguay"]
        }
        return diccionario_default"""
        print("Error en la carga del JSON. Favor contactar con el administrador.")
        sys.exit()

set_palabras_ahorcado = cargar_datos(set_palabras_json)

puntuacion = 0
vidas = 10
letras_adivinadas = []

def jugar_ahorcado():
    global puntuacion, vidas, categoria, palabra
    letras_adivinadas = []
    categoria = random.choice(list(set_palabras_ahorcado.keys()))    
    palabra = random.choice(set_palabras_ahorcado[categoria])
    palabra = palabra.replace(" ", "")  # Elimina los espacios de la palabra
    errores = 0
    print(f"\nLa categoría es {categoria.upper()}")
    print(f"La palabra tiene {len(palabra)} letras")

    while vidas > 0:
        print(f"Tienes {vidas} vidas")
        if puntuacion > 0:
            print(f"Tu puntuación es {puntuacion}")
        print()
        print("Palabra: ", end="")
        palabra_oculta = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_oculta += letra
                print(letra, end=" ")
            else:
                palabra_oculta += "_"
                print("_", end=" ")
        print()

        if palabra_oculta == palabra:
            print("\n¡FELICIDADES! Adivinaste la palabra:", palabra.upper(), end=" ")
            print()
            return True, errores == 0  # True si no hubo errores, False en caso contrario

        letra_usuario = input("Adivina una letra: ")[:1].lower()

        if not letra_usuario.isalpha():
            print("Entrada no válida. Ingresa una letra.")
            continue

        if letra_usuario in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue

        if letra_usuario in palabra:
            print("¡CORRECTO!")
            letras_encontradas = palabra.count(letra_usuario)
            puntos_ganados = letras_encontradas * 10
            letras_adivinadas.append(letra_usuario)
            puntuacion += puntos_ganados
        else:
            print("Incorrecto. Pierdes una vida.")
            errores += 1
            vidas -= 1
        print(f"\nLa categoría es {categoria.upper()}")

    print("\n¡Te quedaste sin vidas! La palabra era:", palabra)
    return False, errores != 0  # Indica que se acabaron las vidas


print("AHORCADO")
puntuacion = 0
while True:
    bonificacion = 100  # Puntos extra por no tener errores
    ganado, sin_errores = jugar_ahorcado()
    if sin_errores:
        puntuacion += bonificacion  # Bonificación por no tener errores
        print("\n¡ADIVINASTE LA PALABRA SIN ERRORES! Obtienes una bonificación de", bonificacion, "puntos.")
    print("\nPuntuación actual:", puntuacion)
    if vidas > 0:
        print(f"Vidas restantes: {vidas}")
    print()
    if vidas > 0:
        jugar_nuevo = input("¿Seguir jugando?\nSi sales del juego antes de quedar sin vidas, tendrás una penalización de 25 puntos. (s/n): ")[:1].lower()
        while jugar_nuevo != 's' and jugar_nuevo != 'n':
            print("Entrada no válida. Ingresa 's' o 'n'.")
            jugar_nuevo = input("¿Seguir jugando?\nSi sales del juego antes de quedar sin vidas, tendrás una penalización de 25 puntos. (s/n): ")[:1].lower()
        if jugar_nuevo == 'n':
            penalizacion = vidas * 5
            print(f"¡Gracias por jugar! Por salir antes del juego, tendrás una penalización de {penalizacion} puntos.")
            puntuacion -= penalizacion # Penalización por salir del juego sin acabar sus vidas
            break
    else:
        print("¡Gracias por jugar!")
        break
print("Tu puntuación final:", puntuacion, "puntos")