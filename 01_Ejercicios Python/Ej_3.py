largo = int(input("Ingrese el largo: "))
char = input("Ingrese el caracter a utilizar: ")

def draw_triangle(largo:int, char:str)->None:
    cont:int=1
    
    for x in range(largo):
        spaces:int=largo-cont
        print((" ") * spaces + (char + " ") * cont)
        cont+=1
        

draw_triangle(largo,char)