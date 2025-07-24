import time

class Mascota:
    def __init__(self, nombre, edad, raza, sexo, animal="Gato"):
        self.nombre = nombre
        self.animal = animal
        self.edad = edad
        self.raza = raza
        self.sexo = sexo
        
    def saludar(self):
        print(f"Hola, soy {self.nombre} y soy un {self.animal.lower()}.")
        print(f"Soy {self.sexo.lower()}, tengo {self.edad} años y soy de raza {self.raza}.")
        if self.animal == "Gato":
            print("Miau")
        elif self.animal == "Perro":
            print("Guau")
        else:
            pass
        print()
        time.sleep(3)