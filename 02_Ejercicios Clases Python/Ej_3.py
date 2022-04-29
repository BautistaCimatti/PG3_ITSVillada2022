class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado mayor es el 1(" + str(self.lado1) + ")")
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("El lado mayor es el 2")
        elif self.lado3 > self.lado1 and self.lado3 > self.lado2:
            print("El lado mayor es el 3")
        elif self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Sus 3 lados son iguales, no hay mayor")

    def equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es equilatero")
        else:
            print("No es equilatero")


print("Triangulo 1")
t1 = Triangulo(8, 2, 0)
t1.lado_mayor()
t1.equilatero()

print("Triangulo 2")
t2 = Triangulo(5, 5, 5)
t2.lado_mayor()
t2.equilatero()
