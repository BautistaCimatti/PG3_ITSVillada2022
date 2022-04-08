

def draw_square():
    ancho = int(input("Ingrese el ancho: "))
    largo = int(input("Ingrese el largo: "))
    char = input("Ingrese el caracter a utilizar: ")
    for x in range(largo):
        print((char + " ") * ancho)

draw_square()        

def draw_triangle()->None:
    largo = int(input("Ingrese el largo: "))
    char = input("Ingrese el caracter a utilizar: ")
    cont:int=1
    
    for x in range(largo):
        spaces:int=largo-cont
        print((" ") * spaces + (char + " ") * cont)
        cont+=1

draw_triangle()

