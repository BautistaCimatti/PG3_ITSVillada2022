list = []

for x in range(6):
    a = input("Ingrese un numero: ")
    list.append(int(a))


def bubblesort(elements):
    for n in range(len(elements) - 1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]


print(list)
print("Ordenando...")
bubblesort(list)
print(list)
