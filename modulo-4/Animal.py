# clases

# Para declarar la clase, usamos la palabra reservada "class". El nombre de la clase debe ser en singular y con PascalCase
class Animal:
    
    nombre_veterinaria = "Mi Vet"
    lista_animalitos = []
    
    # __init__ es el construcctor, inicializa/crea el objeto.
    # Se ejecuta de manera automática cuando creo el objeto.
    #self representa al objeto mismo que se está inicializando
    def __init__(self, nombre="Firulais", tipo="Perro", edad=15):
        # todos los atributos con los que voy a crear el objeto
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.energia = 100
        self.felicidad = 100
        Animal.lista_animalitos.append(self)
        
    # Método: función/acción que el objeto puede realizar
    def presentarse(self):
        print(f"¡Hola, soy {self.nombre}, un {self.tipo}, y tengo {self.edad}!")
        return self # permite que se pueda encadenar los métodos
        
    def comer(self, comida):
        self.energia = Animal.calcula_valor(self.energia, 5)
        self.felicidad += 5
        print(f"¡{self.nombre} está comiendo {comida.lower()}!")
        return self # permite que se pueda encadenar los métodos
        
    def jugar(self, tiempo):
        self.energia -= (tiempo * .5)
        self.felicidad += (tiempo * .5)
        print(f"¡{self.nombre} estuvo jugando por {tiempo} minutos!")
        return self # permite que se pueda encadenar los métodos
    
    def acariciar(self):
        self.felicidad += 10
        print(f"¡{self.nombre} está siendo acariciado!")
        return self # permite que se pueda encadenar los métodos
    
    def dormir(self, horas):
        if horas < 2:
            self.energia = Animal.calcula_valor(self.energia, 10)
        elif horas < 4:
            self.energia = Animal.calcula_valor(self.energia, 20)
        else:
            self.energia = 100
            self.felicidad = 100 
        print(f"¡{self.nombre} está durmiendo por {horas} horas! Su energía actual es de {self.energia}")
        return self # permite que se pueda encadenar los métodos
    
    # Método de clase es algo PROPIO de la clase, es decir, que NO tiene acceso a la información de un objeto específico.
    @classmethod
    def imprimir_lista_animales(cls): # cls = Animal
        print(" Lista de Animales en la Veterinaria ".center(50, "-"))
        for mascota in cls.lista_animalitos:
            print(f"- Nombre: {mascota.nombre} - Tipo: {mascota.tipo} - Edad: {mascota.edad}")
        print("".center(50, "-"))
    
    # Método estático es una acción/función que no tiene acceso a la información de un objeto o clase específicos.
    @staticmethod
    def calcula_valor(valor, cambio_valor):
        suma = valor + cambio_valor
        if suma > 100:
            return 100
        else:
            return suma
    
    def ir_al_bano(self):
        raise NotImplementedError