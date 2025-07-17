# Funciones
def mt_a_cm(metros):
    cm = metros * 100
    return cm

def saludar():
    print("¡Hola!")

def saludar_nombre(nombre):
    print(f"¡Hola {nombre}!")

saludar()
saludar()
saludar()
saludar()
saludar()
saludar()
saludar()
saludar()
saludar()
saludar()
saludar_nombre("Douglas")
saludar_nombre("Valeria")

saludar_nombre(str(saludar_nombre("Douglas")))

def mt_a_cm_y_mm(metros):
    cm = mt_a_cm(metros)
    if cm % 1 == 0:
        cm = int(cm)
    mm = cm * 10
    if mm % 1 == 0:
        mm = int(mm)
    return cm, mm

centimetros, milimetros = mt_a_cm_y_mm(1.75)
print(centimetros, milimetros)