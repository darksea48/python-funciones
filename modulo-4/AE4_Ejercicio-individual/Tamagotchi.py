# Clase Tamagotchi
from time import sleep
import random

class Tamagotchi:
    
    colores = ["rojo", "amarillo", "verde", "azul", "violeta"]
    
    def __init__(self, nombre, duenio, color=random.choice(colores)):
        self.nombre = nombre
        self.color = color
        self.salud = 100
        self.energia = 100
        self.felicidad = 100
        self.duenio = duenio
        
        print(f"¡Un nuevo Tamagotchi llamado {self.nombre} ha nacido!")
    
    def presentarse(self):
        raise NotImplementedError
    
    def comer(self):
        self.energia += Tamagotchi.calcula_valor(self.energia, 10)
        self.felicidad += Tamagotchi.calcula_valor(self.felicidad, 5)
        self.salud += Tamagotchi.calcula_valor(self.salud, 10)
        print(f"{self.nombre} está comiendo.")
        sleep(random.randint(1, 5))
        print(f"{self.nombre} ha comido. ¡Está muy contento!")
        sleep(1)
        
    def jugar(self, tiempo):
        if tiempo <= 30:
            self.energia -= 5
            self.felicidad += Tamagotchi.calcula_valor(self.felicidad, 10)
        else:
            self.energia -= round(tiempo/6)
            self.felicidad += Tamagotchi.calcula_valor(self.felicidad, round(tiempo/3))
        self.salud -= 5
        print(f"{self.nombre} está jugando.")
        sleep(round(tiempo/6))
        print(f"{self.nombre} ha jugado por {tiempo} minutos. ¡Está muy contento!")
        sleep(1)
        
    def curar(self):
        energia_tiempo = (100 - self.energia) / 10
        felicidad_tiempo = (100 - self.felicidad) / 10
        salud_tiempo = (100 - self.salud) / 10
        print(f"¡Estás curando a {self.nombre}! Espera un momento...")
        sleep(round(energia_tiempo + felicidad_tiempo + salud_tiempo))
        self.energia = 100
        self.felicidad = 100
        self.salud = 100
        print(f"¡Has curado a {self.nombre}! ¡Está muy sano y contento!")
        print(f"Salud: {self.salud} / 100")
        print(f"Energía: {self.energia} / 100")
        print(f"Felicidad: {self.felicidad} / 100")
        sleep(1)
        
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
    