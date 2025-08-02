from Animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad,  raza, sonido="Guau"):
        super().__init__(nombre=nombre, edad=edad, tipo="Perro")
        self.sonido = sonido
        self.raza = raza
        
    def ladrar(self):
        print(f"¡{self.nombre} está ladrando! {self.sonido}")
        return self
    
    def mover_colita(self):
        print(f"¡{self.nombre} está moviendo la colita súper feliz!")
        #super().presentarse()
        self.presentarse()
        return self
    
    def ir_al_bano(self):
        print(f"¡{self.nombre} está paseando con su dueño y su dueño le está recogiendo las heces!")
        return self