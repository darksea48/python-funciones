# Clase Persona
import random
from Tamagotchi import Tamagotchi

class Persona:
    
    def __init__(self, nombre, apellido, tamagotchi=""):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi
        # self.energia = 100
    
    def obtener_tamagotchi(self):
        nombre = input("Ingrese el nombre del tamagotchi: ")
        tamagotchi = Tamagotchi(nombre)
        self.tamagotchi.append(tamagotchi)
        return self
        
  
    def jugar_con_tamagotchi(self, tamagotchi):
        print(f"{self.nombre} está jugando con {tamagotchi.nombre}")
        tiempo = random.randint(1, 60) # Hace que la cantidad de minutos varíe aleatoriamente, entre 1 min y 1 hora
        tamagotchi.jugar(tiempo)
        return self
    
    def darle_comida(self, tamagotchi):
        print(f"{self.nombre} está comiendo con {tamagotchi.nombre}")
        tamagotchi.comer()
        return self
    
    def curarlo(self, tamagotchi):
        print(f"{self.nombre} está curando a {tamagotchi.nombre}")
        tamagotchi.curar()
        return self