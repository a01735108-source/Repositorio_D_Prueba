##Este es el archivo principal en donde se llevaran a cabo las funciones de la entrega

#FUNCIONES DEL MAIN##
def hi():
    nombre=str(input("Ingresa tu nombre: "))   #Modifique esta funcion para que tambien sea un input
    print("Holaa! Bienvenido", nombre ,"\n ¿que vamos a hacer hoy?")

#Quitamos el print para que no genere el none
hi()

#FUNCIONES DEL FRONTEND!##
def edad():
    #Le pedimos al usuario que ingrese su edad
    edad=int(input("Ingresa tu edad: "))

    if edad >=16:
        print("¿Estas listo para la mejor noche de tu vida?")
        print("Continuemos con tu proceso >>>")
    else:
        print("Upps, no cuentas con la edad minima requerida :(")

#Quitamos el print porque si no nos genera en none
edad()