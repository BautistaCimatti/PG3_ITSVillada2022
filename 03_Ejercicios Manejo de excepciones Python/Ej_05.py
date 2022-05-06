try:
    f = open("demofile.txt", "w")
    i= int(input("Ingresa lo que quieras guardar en el txt: "))
    if i.isnumeric()==True:
        int(i)
    else:
        str(i)

    f.write(i)
    f.close()

    f = open("demofile.txt", "r")
    print(f.read()) 

except TypeError:
        f.write(str(i))
        f.close()
        f = open("demofile.txt", "r")
        print(f.read()) 

except ValueError:
        f.write(str(i))
        f.close()
        f = open("demofile.txt", "r")
        print(f.read()) 