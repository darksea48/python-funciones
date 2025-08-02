# Clase Tamagotchi
from time import sleep
import random

class Tamagotchi:
    def __init__(self, nombre, color, duenio, tipo=(random.choice(["Kuchipatchi", "Mimitchi"]))):
        self.nombre = nombre
        self.color = color
        self.salud = 100
        self.energia = 100
        self.felicidad = 100
        self.tipo = tipo
        self.duenio = duenio
        
        print(f"¡Bienvenido, {self.nombre}! Has sido creado con éxito.")
        print(f"¡Espero que disfrutes conmigo!")
        print(f"El nombre de tu tamagotchi es {self.nombre}, y es un/a {self.tipo} de color {self.color}.")
    
    def presentarse(self):
        raise NotImplementedError
    
    def comer(self):
        self.energia += Tamagotchi.calcula_valor(self.energia, 10)
        self.felicidad += Tamagotchi.calcula_valor(self.felicidad, 5)
        self.salud += Tamagotchi.calcula_valor(self.salud, 10)
        print(f"{self.nombre} está comiendo. ¡Está muy contento!")
        
    def jugar(self, tiempo):
        if tiempo <= 30:
            self.energia -= Tamagotchi.calcula_valor(self.energia, 5)
            self.felicidad += Tamagotchi.calcula_valor(self.felicidad, 10)
        else:
            self.energia -= Tamagotchi.calcula_valor(self.energia, round(tiempo/6))
            self.felicidad += Tamagotchi.calcula_valor(self.felicidad, round(tiempo/3))
        self.salud -= Tamagotchi.calcula_valor(self.salud, 5)
        sleep(round(tiempo/6))
        print(f"{self.nombre} está jugando. ¡Está muy contento!")
        
    def curar(self):
        self.energia = 100
        self.felicidad = 100
        self.salud = 100
        print(f"¡Has curado a {self.nombre}! ¡Está muy sano y contento!")
        
    def consultar_datos(self):
        print(f"Datos de tu tamagotchi: {self.nombre}")
        print(f"Nombre: {self.nombre}")
        print(f"Color: {self.color}")
        print(f"Salud: {self.salud} / 100")
        print(f"Energía: {self.energia} / 100")
        return self
    
    @staticmethod
    def calcula_valor(valor, cambio_valor):
        suma = valor + cambio_valor
        if suma > 100:
            return 100
        else:
            return suma
    