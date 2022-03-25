def vocales(word):
    num = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            num += 1
    print("Numero de vocales:" + str(num))


word = input("Ingrese una palabra para averiguar cuantas vocales tiene: ")

vocales(word)
