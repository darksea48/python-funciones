import time

class Mascota:
    def __init__(self, nombre, edad, raza, sexo, animal="Gato"):
        self.nombre = nombre
        self.animal = animal
        self.edad = edad
        self.raza = raza
        self.sexo = sexo
        
    def saludar(self):
        sexo = Mascota.valida_mascotas(self.sexo, self.animal)
        print(f"Hola, soy {self.nombre} y {sexo.lower()}.")
        print(f"Soy {self.sexo.lower()}, tengo {self.edad} años y soy de raza {self.raza}.")
        return self
        
    def onomatopeya(self):
        if self.animal == "Gato":
            print("Miau")
        elif self.animal == "Perro":
            print("Guau")
        else:
            pass
        print()
        time.sleep(3)
        return self
    
    @staticmethod
    def valida_mascotas(sexo, animal):
        if sexo == "Macho":
            if animal == "Gato":
                return "Soy un michi"
            elif animal == "Perro":
                return "Soy un lomito"
            else:
                return False
        elif sexo == "Hembra":
            if animal == "Gato":
                return "Soy una micha"
            elif animal == "Perro":
                return "Soy una lomito"
            else:
                return False
        else:
            return False