# 1. Imprime "Hola, mundo"

print("Hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable

nombre = "Valeria"

print("Hola,", nombre) # con una coma

print("Hola, " + nombre) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable

numero = 48

print("Hola ", numero, "!", sep="") # con una coma

print("Hola " + str(numero) + "!") # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "tacos"

comida2 = "arepas"

print("Me encanta comer {comida1} y {comida2}".format(comida1=comida1, comida2=comida2)) # con .format()

print(f"Me encanta comer {comida1} y {comida2}") # con una cadena f

# 5. Buscar nuevas formas de print (les cambiamos los nombres a las variables)

comida1 = "sopaipillas con pebre"

comida2 = "cazuela de ave"

print("Me encanta comer %s y %s" % (comida1, comida2)) # con el operador %

print("Me encanta comer {} y {}".format(comida1, comida2)) # con el método .format() sin darle nombre a las variables")