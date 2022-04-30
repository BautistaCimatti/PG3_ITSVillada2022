while True:
    try:
        n1 = int(input("Ingrese un numero: "))
        n2 = int(input("Ingrese otro numero: "))
        div=n1/n2
        print("El resultado de la division de los numeros es: ",div)
    except ZeroDivisionError:
        print("Error Matematico: No es posible dividir en 0")
    