# Condicionales

"""
if condicional:
    bloque de codigo a ejecutar si la condicion
    es verdadera
else:
    bloque de codigo a ejecutar si la condicion
    es falsa
"""

""" if anidados
if condicional1:
    bloque de codigo a ejecutar si la condicion1
    es verdadera
elif condicional2:
    bloque de codigo a ejecutar si la condicion2
    es verdadera
else:
    bloque de codigo a ejecutar si ninguna de las
    condiciones anteriores es verdadera
"""

x = 20

if x > 10:
    print("El número ingresado es mayor que 10")
elif x < 10:
    print("El número ingresado es menor que 10")
print("El valor de x es", x)

edad_infante = 4
if edad_infante < 2:
    print("El infante es un bebe")
elif edad_infante < 5:
    print("El infante es un infante")
elif edad_infante < 12:
    print("El infante es un niño")
elif edad_infante < 18:
    print("El infante es un adolescente")
else:
    print("El infante es un adulto")

# && -> and
temperatura = 20
esta_lloviendo = False # True o False, la primera letra es con mayúscula

if temperatura > 18 and not esta_lloviendo: # ! -> not -- not CONDICIONAL => condicional == False
    print("El clima es agradable")
else:
    print("El clima es malo")

# || -> or
edad_conductor = 17
permiso_padres = True

if edad_conductor < 18 or permiso_padres:
    print("Puedes obtener tu licencia de conducir")
else:
    print("No puedes obtener tu licencia de conducir")  

x = 1
y = 2
z = 3

if x > 2 or y > 2 or z > 2:
    print("Uno de los números es mayor a dos")

# Operadores de comparación:
# > (mayor que)
# < (menor que)
# >= (mayor o igual que)
# <= (menor o igual que)
# == (igual que)
# != (diferente de)
# and (y) / or (o) / not (no)