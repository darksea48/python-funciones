#Vas a crear un programa que registre usuarios para un sistema, donde se solicitan varios datos personales. Los datos deben ser validados estrictamente y, si hay algún error, el programa debe lanzar y manejar excepciones específicas. *Nombre: Debe contener solo letras y espacios, Si el nombre está vacío o contiene números o símbolos, lanzar ValueError con mensaje específico. *Edad:Debe ser un número entero entre 18 y 120.Si no es un número, lanzar TypeError.Si está fuera del rango, lanzar ValueError. *Correo electrónico: Debe contener un "@" y un "."Si no cumple, lanzar una excepción. *Contraseña: Debe tener al menos 8 caracteres, incluir al menos una mayúscula, una minúscula, un número y un símbolo especial. Si no cumple, lanzar una excepcion. * Teléfono: debe ser un número de 10 dígitos. Si ingresa algo diferente, lanzar ValueError.
#BONUS: excepcion personalizada InvalidEmailError. excepción personalizada WeakPasswordError. Al final, mostrar un resumen con todos los datos válidos ingresados. permita al usuario intentar de nuevo.
from sys import exit

class InvalidEmailError(Exception):
    def __init__(self, mensaje=None):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class WeakPasswordError(Exception):
    def __init__(self, mensaje=None):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def consulta_intento():
    consulta_intento = input("¿Desea intentar de nuevo? (s/n): ")[:1]
    if consulta_intento.lower() != "s":
        print("¡Hasta pronto!")
        exit()

while True:
    try:
        nombre = input("Ingrese su nombre: ")
        if not nombre.isalpha():
            raise ValueError("El nombre debe contener solo letras y espacios.")
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
    except ValueError as e:
        print(f"Error: {e}")
        consulta_intento()
        continue
    else:
        break
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 18 or edad > 120:
            raise ValueError("La edad debe estar entre 18 y 120 años.")
        if edad is not int:
            raise TypeError("La edad debe ser un número entero.")
    except ValueError as e:
        print(f"Error: {e}")
        consulta_intento()
        continue
    except TypeError as e:
        print(f"Error: {e}")
        consulta_intento()
        continue
    else:
        break
while True:
    try:
        correo = input("Ingrese su correo electrónico: ")
        if "@" not in correo or "." not in correo:
            raise InvalidEmailError("El correo debe tener un formato válido. Ejemplo: example@example.com")
    except InvalidEmailError as e:
        print(f"Error: {e}")
        consulta_intento()
        continue
    else:
        break
while True:
    try:
        contraseña = input("Ingrese su contraseña: ")
        if len(contraseña) < 8:
            raise WeakPasswordError("La contraseña debe tener al menos 8 caracteres.")
        if not any(char.isupper() for char in contraseña) or not any(char.islower() for char in contraseña) or not any(char.isdigit() for char in contraseña) or not any(char in contraseña for char in "!@#$%^&*()"):
            raise WeakPasswordError("La contraseña debe contener al menos una letra mayúscula, una minúscula, un número y un caracter especial.")
    except WeakPasswordError as e:
        print(f"Error: {e}")
        consulta_intento()
        continue
    else:
        break
while True:
    try:
        telefono = input("Ingrese su número de teléfono: ")
        if not telefono.isdigit() or len(telefono) != 10:
            raise ValueError("El número de teléfono debe ser un número de 10 dígitos.")
    except ValueError as e:
        print(f"Error: {e}")
        consulta_intento()
        continue
    else:
        break

print("".center(50, "-"))
print("DATOS DEL USUARIO".center(50, " "))
print("".center(50, "-"))
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Correo electrónico: {correo}")
print(f"Teléfono: {telefono}")
print(f"Su contraseña es muy fuerte, contiene {len(contraseña)} caracteres y contiene uno o más caractéres requeridos.")