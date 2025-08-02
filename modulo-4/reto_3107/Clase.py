from random import *
from time import *

class Completo:
    
    def __init__(self, tipo, ingredientes=[], proteina="Vienesa", tamano=18, pan="pan de completo"):
        self.tipo = tipo
        self.ingredientes = ingredientes
        self.proteina = proteina
        self.tamano = tamano
        self.pan = pan
        self.ingrediente_listo = False
        self.adereso_listo = False
        
    def colocar_ingredientes(self, proteina, ingredientes):
        print(f"Colocando {proteina}")
        sleep(1)
        for i in ingredientes:
            print(f"Colocando {i}")
            sleep(1)
        print("Listo")
        self.ingrediente_listo = True
        return self
    
    def colocar_adereso(self):
        aderesos = ["ketchup", "mostaza", "mayonesa"]
        for i in aderesos:
            while True:
                adereso_consulta = input(f"¿Quieres colocarle {i}? (s/n): ")[:1].lower()
                if adereso_consulta not in ["s", "n"]:
                    print("Por favor ingresa una opción válida")
                else:
                    break
            if adereso_consulta == "s":
                print(f"Colocando el adereso {i}")
                sleep(1)
        print("Listo")
        self.adereso_listo = True
        return self
    
    def servir(self):
        while self.ingrediente_listo == False:
            print(f"No están listos los ingredientes")
            sleep(1)
            self.colocar_ingredientes(self.proteina, self.ingredientes)        
        if self.adereso_listo == False:
            print("No te pregunté si querías colocarle aderesos")
            sleep(1)
            self.colocar_adereso()
        print(f"Aquí tienes tu {self.tipo}")
        print()
        sleep(1)
       
class Italiano(Completo):
    
    def __init__(self, tipo="Completo Italiano", ingredientes=["tomate","palta","mayo casera"], proteina="vienesa", tamano=18, pan="pan de completo"):
        super().__init__(tipo, ingredientes, proteina, tamano, pan)
    
class AlPlato(Completo):
    
    def __init__(self, tipo="Completo Al Plato", ingredientes=["tomate", "palta", "mayo casera"], proteina="vienesa", tamano=0, pan="Sin pan", plato="Plato de loza"):
        super().__init__(tipo, ingredientes, proteina, tamano, pan)
        self.plato = plato
    
    def colocar_ingredientes(self, proteina, ingredientes):
        print(f"Tomando el {self.plato}")
        sleep(1)
        super().colocar_ingredientes(proteina, ingredientes)
        return self
        