
class Animal():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def tipoAnimal(self):
        pass

    def sonidoAnimal(self):
        pass

class Perro(Animal):
    def tipoAnimal(self):
        print("Tipo: Perro")

    def sonidoAnimal(self):
        print("Sonido: Guau")

class Guacamaya(Animal):
    def tipoAnimal(self):
        print("Tipo: Guacamaya")

    def sonidoAnimal(self):
        print("Sonido: Guaca")

class Cerdo(Animal):
    def tipoAnimal(self):
        print("Tipo: Cerdo")

    def sonidoAnimal(self):
        print("Sonido: Oinch")

class Puma(Animal):
    def tipoAnimal(self):
        print("Tipo: Puma")

    def sonidoAnimal(self):
        print("Sonido: Grrr")

