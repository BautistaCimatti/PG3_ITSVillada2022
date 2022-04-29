class Persona:
    def __init__(self):
        self.nombre = input("Nombre:")
        self.edad = int(input("Edad:"))

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Sueldo:"))

    def imprimir(self):
        super().imprimir()
        print("Sueldo:", self.sueldo)

    def impuestos(self):
        if self.sueldo > 3000:
            print("Paga impuestos")
        else:
            print("No paga impuestos")


p1 = Persona()
p1.imprimir()
e1 = Empleado()
e1.imprimir()
e1.impuestos()
