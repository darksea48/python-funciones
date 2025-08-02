from Animal import Animal
from Gato import Gato
from Perro import Perro
firulais = Animal("Firulais", "Perro", 15)
oreo = Animal("Oreo Timon Omatopopih Cilantrillo", "Gato", 2)
kiki = Animal("Kiki del Sascachetun", "Gato", 6)
miu = Animal("Miusita", "Gato", 7)

print(firulais.nombre)
print(oreo.nombre)
print(kiki.nombre)

kiki.nombre = "Kikilin"
print(kiki.nombre)

firulais.presentarse()

miu.comer("Croquetas")

# Encadenar métodos
kiki.presentarse().comer("Croquetas").jugar(10).dormir(12)

print(Animal.nombre_veterinaria)
Animal.imprimir_lista_animales()

print("".rjust(100, "-"))

garfield = Gato("Garfield", 5, "¡Odio los lunes!", "Atigrado", "Largo", "Naranja")

garfield.razcar_sofa()
garfield.presentarse()

oddie = Perro("Oddie", 5, "Mestizo", "Guau")

oddie.ladrar()
oddie.mover_colita()

print("".rjust(100, "-"))

Animal.imprimir_lista_animales()

print("".rjust(100, "-"))