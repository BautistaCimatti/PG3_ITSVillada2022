meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
while True:
    try:
        fecha = int(input("Ingrese el numero de mes: "))
        print("El mes es: ", meses[fecha-1])
    except  IndexError:
        print("El nro de mes que ingresaste no existe")