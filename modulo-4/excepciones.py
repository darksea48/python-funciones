'''
SINTAXIS
try:
    # Bloque de código que se intenta realizar
    
    
except Error: # En otros lenguajes de programación es el equivalente a "catch"
    # Bloque de código que se ejecuta si ocurre una excepción
'''

x = 10
y = 0
#resultado = x / y
#print("El resultado de la división es:", resultado)

try:
    resultado = x / y
    print("El resultado de la división es:", resultado)
except ZeroDivisionError: # Error que aparece al dividir entre 0
    print("Error: El divisor no puede ser cero.")

# ValueError: cuando se ingresa un valor distinto al que se
try: 
    edad = int("treinta")
    print(f"La edad es: {edad}")
except ValueError:
    print("Error: La edad debe ser un número entero válido.")

# TypeError: al querer concatenar de mala forma dos datos distintos
try:
    texto = "Hola como estás?"
    numero = 22
    frase = texto + numero
except TypeError:
    print("Error: Se está concatentando de forma incorrecta.")

# IndexError
frutas = ["manzana", "banana", "cereza"]
try:
    fruta = frutas[3]
    print(fruta)
except IndexError:
    print("Error: No se encuentra el índice solicitado en la lista.")

# KeyError
estudiante = {
    "nombre": "Juan",
    "apellido": "Paredes",
    "edad": 20,
    "carrera": "Ingeniería de Software"
}
try:
    email = estudiante["email"]
    print(email)
except KeyError:
    print("Error: La clave solicitada no existe en el diccionario.")

def dividir():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    # Error ZeroDivisionError
    except ZeroDivisionError:
        print(f"Error: El divisor no puede ser cero.")
    # Error ValueError
    except ValueError:
        print("Error: Los valores ingresados deben ser números enteros")
    # Error TypeError
    except TypeError:
        print("Error: Los valores ingresados deben ser números enteros")
    # Errores generales
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally: # Se ejecuta para cerrar el código, independiente si este arrojó excepciones o no
        print("¡Hasta pronto!") # Cerrar conexiones o archivos, liberar recursos, mensajes de cierre, etc.

dividir()

try:
    bebidas = ["Cafe con leche", "Chocolate", "Te", "Latte Macchiatto"]
    bebida_deseada = input("Ingrese la bebida deseada: ")
    if bebida_deseada not in bebidas:
        raise ValueError(f"Esa bebida no está disponible")
    else:
        print(f"Tu bebida {bebida_deseada} está lista")
except ValueError as e:
    print(f"Error: {e}")