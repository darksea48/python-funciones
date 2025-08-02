# class Hijo(Padre)
from Animal import Animal

class Gato(Animal):
    
    def __init__(self, nombre, edad, raza, tipo_pelaje, color, sonido="Miau"):
        super().__init__(nombre=nombre, edad=edad, tipo="Gato")
        self.sonido = sonido
        self.raza = raza
        self.tipo_pelaje = tipo_pelaje
        self.color = color
    
    def maullar(self):
        print(f"¡{self.nombre} está maullando! {self.sonido}")
        return self
    
    def razcar_sofa(self):
        print(f"¡{self.nombre} está razcando el sofá!")
        return self
    
    def ir_al_bano(self):
        print(f"¡{self.nombre} fue al arenero!")
        return self