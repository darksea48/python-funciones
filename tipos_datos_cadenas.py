# Cadenas

nombre = "Juana"
edad = 30

# Métodos para manipular cadenas
frase = f"Hola soy {nombre} de Arco y hoy es 4 de Julio"
print(frase.title()) # Primera letra de cada palabra en mayúsculas
print(frase.capitalize()) # Primera letra de la frase en mayúscula
print(frase.upper()) # Todas las letras en mayúsculas
print(frase.lower()) # Todas las letras en minúsculas
print(frase.count("oy")) # Regresa cuántas veces se repite el parámetro entregado, en este caso "oy"
print(frase.replace("oy", "ay")) # Reemplaza el primer parámetro por el segundo en todos los lugares que se encuentre
print(frase.find("juana")) # Devuelve el índice donde comienza el valor dado. Es case-sensitive
print(frase.find(nombre))

texto = "Elena!Juana!Pablo!Pedro"
print(texto.split("!")) # Crea una lista con la división de mi cadena en base al caracter dado
print(frase.isalpha()) # Devuelve un valor booleano según si es una cadena de solo texto
print("123".zfill(5)) # Completa con ceros a la izquierda según la cantidad de caracteres que debe tener

saludo = "     ¡Hola Python!       "
print(saludo.strip()) # Elimina los espacios vacíos del principio y del final

print(saludo.lstrip()) # Elimina los espacios vacíos del principio
print(saludo.rstrip()) # Elimina los espacios vacíos del final

print("Hola".rjust(10)) # Ajusta hacia la derecha segun la cantidad de caracteres solicitados
print("Hola".ljust(10)) # Ajusta hacia la izquierda
print("Hola".center(10)) # Centra

frase = "Hola"
print(f"{frase:>10}")  # Justificar a la derecha
print(f"{frase:<10}")  # Justificar a la izquierda
print(f"{frase:^10}")  # Centrado