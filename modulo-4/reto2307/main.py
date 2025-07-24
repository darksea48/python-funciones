import time # Colocaremos un temporizador a ciertos lugares de impresión
import os
from Mascota import Mascota

tomate = Mascota("Tomate Beñeño", 10, "Tuxedo", "Macho")
kiki = Mascota("Kiki del Sascachetun", 6, "Común Pelo Corto", "Macho")
cleo = Mascota("Cleopatra Patricia", 5, "Tuxedo", "Hembra")
oreo = Mascota("Oreo Timon (Alias: Omatopopih Cilantrillo)", 2, "Común Pelo Largo", "Macho")
ebano = Mascota("Ébano", 9, "Kiltro", "Macho", "Perro")
cinta = Mascota("Cinta Catalina", 15, "Calicó", "Hembra")
rebelde = Mascota("Rebelde Subenestrujenbajen", 7, "Común Pelo Corto", "Macho")
tigrito = Mascota("Tigrito Wenceslao Simpicarpio", 7, "Europeo", "Macho")
champinon = Mascota("Champiñon", "∞ (me encuentro en el cielo de los gatos y en el corazón de mis amos)", "Tuxedo", "Macho")


os.system('cls') # Limpiamos la pantalla de la consola para correr la sintaxis
print("Presentamos a las mascotas de la familia.")
print("-----------------------------------------")
time.sleep(1)
print("Primero pasarán las mascotas de los Suárez Jara")
time.sleep(2)
print()
tomate.saludar()
kiki.saludar()
cleo.saludar()
oreo.saludar()
print("Ahora pasarán las mascotas de los Jara Bugueño")
print()
time.sleep(2)
ebano.saludar()
cinta.saludar()
rebelde.saludar()
tigrito.saludar()

print("-----------------------------------------")
print("Y no me olvido de tí, pequeño amigo")
print()
time.sleep(1)
champinon.saludar()
print("-----------------------------------------")

print("¡¡¡ Gracias por pasar a saludar a las mascotas de la familia !!!")
time.sleep(2)