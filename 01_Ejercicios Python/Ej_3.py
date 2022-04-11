def draw_square():
    ancho = int(input("Ingrese el ancho: "))
    largo = int(input("Ingrese el largo: "))
    char = input("Ingrese el caracter a utilizar: ")
    for x in range(largo):
        print((char + " ") * ancho)

def draw_triangle()->None:
    largo = int(input("Ingrese el largo: "))
    char = input("Ingrese el caracter a utilizar: ")
    cont:int=1
    for x in range(largo):
        spaces:int=largo-cont
        print((" ") * spaces + (char + " ") * cont)
        cont+=1

def draw_triangleud()->None:
    largo = int(input("Ingrese el largo: "))
    char = input("Ingrese el caracter a utilizar: ")
    cont:int=largo
    for x in range(largo):
        spaces:int=largo-cont
        print((" ") * spaces + (char + " ") * cont)
        cont-=1

draw_square()       
draw_triangle()
draw_triangleud()
