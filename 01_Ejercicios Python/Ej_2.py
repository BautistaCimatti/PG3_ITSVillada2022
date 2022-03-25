def bisiesto(year):
    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")


bisiesto(int(input("Ingrese un año para saber si es bisiesto o no: ")))
