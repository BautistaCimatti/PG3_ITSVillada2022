class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: "+str(self.nombre))
        print("Nota: "+str(self.nota))

    def estado(self):
        if self.nota>=6:
            print("Regular")
        else:
            print("Desaprobado")

Alumno1 = Alumno("Jorge", 5)
Alumno2 = Alumno("Pepe", 8)
Alumno1.imprimir()
Alumno1.estado()
Alumno2.imprimir()
Alumno2.estado()