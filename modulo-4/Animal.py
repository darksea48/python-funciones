# clases

# Para declarar la clase, usamos la palabra reservada "class". El nombre de la clase debe ser en singular y con PascalCase
class Animal:
    
    # __init__ es el construcctor, inicializa/crea el objeto.
    # Se ejecuta de manera automática cuando creo el objeto.
    #self representa al objeto mismo que se está inicializando
    def __init__(self, nombre="Firulais", tipo="Perro", edad=15):
        # todos los atributos con los que voy a crear el objeto
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        