
def palindromo(p):
    if(p==p[::-1]):
        print("Es palindromo")
    else:
        print("NO es palindromo")

word=input("Ingrese una palabra: ")
palindromo(word)