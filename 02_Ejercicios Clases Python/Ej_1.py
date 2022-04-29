class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def imprimir(self):
        print(self.nombre)


p1 = Persona("Jorge")
p1.imprimir()

p2 = Persona("Pedro")
p2.imprimir()
