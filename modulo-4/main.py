from Animal import Animal

firulais = Animal("Firulais", "Perro", 15)
oreo = Animal("Oreo Timon Omatopopih Cilantrillo", "Gato", 2)
kiki = Animal("Kiki del Sascachetun", "Gato", 6)

print(firulais.nombre)
print(oreo.nombre)
print(kiki.nombre)

kiki.nombre = "Kikilin"
print(kiki.nombre)