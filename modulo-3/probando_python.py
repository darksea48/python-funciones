import random
import datetime

nombre_persona = input('¿Cuál es tu nombre?')
print(f'¡Bienvenido a Python! {nombre_persona}')

print('Este es un bucle que imprime 10 veces')
for num in range(1, 11):
    print(f'num es: {num}')

semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
dia = random.choice(semana)

print(f'Hoy es: {dia}')

if dia == 'Lunes':
    print('¡Comenzamos la semana con toda la actitud!')
elif(dia == 'Miércoles'):
    print('Estamos a mitad de semana')
elif(dia == 'Viernes'):
    print('¡Listos para un fin de semana!')
else:
    print('¿Qué día es?')

print("")   
print("Aquí lo haré con el paquete datetime")
print("")
    
today = datetime.date.today()
numero_dia = today.weekday() # numero_dia = today.isoweekday() # Otra opción

dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
# dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"] # Otra opción con isoweekday

dia_hoy = dias_semana[numero_dia]

print(f"Hoy es {dia_hoy}.")

if dia_hoy == 'lunes':
    print('¡Comenzamos la semana con toda la actitud!')
elif(dia_hoy == 'miércoles'):
    print('Estamos a mitad de semana')
elif(dia_hoy == 'viernes'):
    print('¡Listos para un fin de semana!')
else:
    print(f'¿Qué día es? {dia_hoy}')

