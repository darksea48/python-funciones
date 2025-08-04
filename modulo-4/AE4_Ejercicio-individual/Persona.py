# Clase Persona
import random
from TipoTamagotchi import *

class Persona:
    
    def __init__(self, nombre, apellido, tamagotchi = []):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi
        # self.energia = 100
    
    def obtener_tamagotchi(self):
        nombre = input("Ingrese el nombre del tamagotchi: ")
        
        # Lista de clases de Tamagotchi disponibles
        tipos_disponibles = [Kuchipatchi, Mimitchi]
        # Elegir una clase al azar
        clase_tamagotchi = random.choice(tipos_disponibles)
        # Crear una instancia de la clase elegida
        tamagotchi = clase_tamagotchi(nombre, self)
        
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
    
    def consultar_datos(self, tamagotchi):
        print(f"{self.nombre} está consultando los datos de {tamagotchi.nombre}")
        tamagotchi.consultar_datos()
        return self