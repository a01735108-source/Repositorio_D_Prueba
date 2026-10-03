##Este es el archivo principal en donde se llevaran a cabo las funciones de la entrega

def hi(nombre):
    print("Holaa! Bienvenido", nombre ,"\n ¿que vamos a hacer hoy?")

print(hi("Danny"))

def art():
    fecha=int(input("¿Para que fecha te gustaria?"))

    if fecha in range(1,10):
        print("MCR esta disponible!")

    elif fecha in range(11,18):
        print("5sos esta en la ciudad!")

    elif fecha in range(18,26):
        print("FallOutBoy aun tiene boletos!")

    elif fecha in range(27,31):
        print("Twenty One Pilots se presenta cerca!")

    else:
        print("Upps no hay eventos disponibles :(")
        
print(art())