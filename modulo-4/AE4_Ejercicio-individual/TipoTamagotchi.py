from Tamagotchi import Tamagotchi

class Kuchipatchi(Tamagotchi):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        self.tipo = tipo
    
    def presentarse(self):
        print(f"Hola {self.duenio.nombre}, soy {self.nombre} y soy un {self.tipo}")
        print(f"Soy de color {self.color}")
        print(f"¡¡DAME COMIDA!!")
        return self

class Mimitchi(Tamagotchi):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        self.tipo = tipo
    
    def presentarse(self):
        print(f"Hola amiguito {self.duenio.nombre}, soy {self.nombre} y soy un {self.tipo}")
        print(f"Soy de color {self.color}")
        print(f"¡¡JUGUEMOS!!")
        return self