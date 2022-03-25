lista = [6, 12, 45, 5, 1]


def buscar(list, search):
    for x in list:
        if search == x:
            print("El indice del numero ingresado es: " + str(list.index(search)))


print(lista)
search = int(input("Ingrese un numero: "))
buscar(lista, search)
