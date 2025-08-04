from Tamagotchi import Tamagotchi
from time import sleep

class Kuchipatchi(Tamagotchi):
    def __init__(self, nombre, duenio):
        super().__init__(nombre, duenio)
    
    def presentarse(self):
        print(f"Hola {self.duenio.nombre}, soy {self.nombre} y soy un Kuchipatchi.")
        print(f"Soy de color {self.color}")
        print(f"¡¡DAME COMIDA!!")
        sleep(1)
        return self

class Mimitchi(Tamagotchi):
    def __init__(self, nombre, duenio):
        super().__init__(nombre, duenio)
    
    def presentarse(self):
        print(f"Hola amiguito {self.duenio.nombre}, soy {self.nombre} y soy un Mimitchi.")
        print(f"Soy de color {self.color}")
        print(f"¡¡JUGUEMOS!!")
        sleep(1)
        return self