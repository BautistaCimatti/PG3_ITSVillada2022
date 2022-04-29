class Familia:
    def __init__(self):
        self.padre = str(input("Nombre del padre: "))
        self.madre = str(input("Nombre de la Madre: "))
        self.cont = int(input("Cantidad de hijos: "))
        self.hijos = []
        for i in range(self.cont):
            self.hijos.append(str(input("Nombre del hijo: ")))

    def __str__(self) -> str:
        return f"Padre: {self.padre} \nMadre: {self.madre} \nHijos:  {self.hijos}"


f1 = Familia()
print(f1)
