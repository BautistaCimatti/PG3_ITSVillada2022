def draw_triangleud()->None:
    largo = int(input("Ingrese el largo: "))
    char = input("Ingrese el caracter a utilizar: ")
    cont:int=largo
    
    for x in range(largo):
        spaces:int=largo-cont
        print((" ") * spaces + (char + " ") * cont)
        cont-=1
        
draw_triangleud()