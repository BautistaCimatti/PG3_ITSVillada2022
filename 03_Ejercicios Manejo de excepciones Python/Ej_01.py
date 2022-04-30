while True:
    try:
        n1 = int(input("Ingrese un numero: "))
        n2 = int(input("Ingrese otro numero: "))
        sum=n1+n2
        print("El resultado de la suma de los numeros es: ",sum)
    except ValueError:
        print("Porfavor, ingrese un numero")
    