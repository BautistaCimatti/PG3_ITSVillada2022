ancho=int(input("Ingrese el ancho: "))
largo=int(input("Ingrese el largo: "))
char=input("Ingrese el caracter a utilizar: ")

for x in range(largo):
    print((char+" ")*ancho)