from Animal import Animal

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