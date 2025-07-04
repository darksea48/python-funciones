print("Hola Mundo!")

# Comentario en línea

'''
Comentarios de más 
de una línea
donde puedes dejar comentado
más de una línea
'''

variable1 = 1
print(variable1)
variable1 = "uno" # Sobreescribiendo la variable, cambiando incluso el tipo de dato
print(variable1)

print(type(variable1)) # de clase Str

# Casteo: cambiar o setear la clase o tipo de dato al declarar o llamar
x = str(3)
print(x)
x = int(3.3)
print(x)
x = float(3)
print(x)

numero = 74
# print("El mejor grupo es el: " + numero) # Arrojará error porque se están concatenando datos de texto con números
print("El mejor grupo es el: " + str(numero))
print(f"El mejor grupo es el: {numero}")

# Variables válidos
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
myvar2 = "John"
MYVAR = "John" # Con mayúsculas se declaran constantes

''' Variables inválidas
2myvar = "John" / No puede iniciarse una variable con caracter numérico
my-var = "John" / No puede contener guiones
my var = "John" / No puede contener espacios
my!var = "John" / No puede contener caracteres especiales
my.var = "John" / No puede contener puntos, el punto denota una clase o módulo (paquete)
'''

# Declarar múltiples variables en una línea
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)
print(x)
print(y)
print(z)

'''
x = "Orange"
y = "Banana"
z = "Cherry"
'''

nombre1 = nombre2 = nombre3 = "Douglas Suárez"
print(nombre1, nombre2, nombre3)
print(nombre1)
print(nombre2)
print(nombre3)

'''
name1 = "Douglas"
name2 = "Douglas"
name3 = "Douglas"
'''

cantantes = ["Little V", "Tarja", "Till Lindemann"]
a, b, c = cantantes
print(a, b, c)
print(a)
print(b)
print(c)

'''
a, b = cantantes
print(a, b)

Arrojará error
'''
a, b = cantantes[0], cantantes[1]
print(a, b)
print(a)
print(b)