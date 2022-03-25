def isStep(num):
    if int(len(num) % 2 != 0):
        return False

    for i in range(0, len(num), 2):
        if not (
            int(num[i : i + 2][0]) + 1 == int(num[i : i + 2][1])
            or int(num[i : i + 2][0]) - 1 == int(num[i : i + 2][1])
        ):
            return False
    return True


nmbr = input("Ingrese un numero para averiguar si es STEP: ")

if isStep(nmbr):
    print("Es numero STEP.")
elif isStep(nmbr) == False:
    print("No es numero STEP.")
