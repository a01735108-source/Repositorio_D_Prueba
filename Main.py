##Este es el archivo principal en donde se llevaran a cabo las funciones de la entrega

def hi(nombre):
    print("Holaa! Bienvenido", nombre ,"\n ¿que vamos a hacer hoy?")

print(hi("Danny"))

def art():
    fecha=int(input("¿Para que fecha te gustaria?"))

    if fecha in range(1,10):
        print("5sos esta disponible!")

    elif fecha in range(11,18):
        print("MCR esta en la ciudad!")

    elif fecha in range(18,28):
        print("FallOutBoy aun tiene boletos!")

    else:
        print("Twenty One Pilots se presenta cerca!")