class Operacion:
    def __init__(self, n1,n2):
        self.n1 = n1
        self.n2 = n2
    def operaciones(self):
        print("Suma: "+str(self.n1+self.n2))
        print("Resta: "+str(self.n1-self.n2))
        print("Multiplicacion: "+str(self.n1*self.n2))
        print("Division: "+str(self.n1/self.n2))

print("Numeros: 3 y 2")
o1=Operacion(3,2)
o1.operaciones()