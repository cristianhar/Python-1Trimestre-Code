#Algoritmo que pide el 1er nombre y apellido de un aprendiz y luego pide
#el primer nombre y apellido de cada uno de sus padres
def concatena(nombre,apellidoP,appelidoM,nombreP,nombreM):

    print("El Aprendiz : " ,nombre,apellidoP,appelidoM)
    print("El padre : ",nombreP ,"y la Madre :",nombreM)

nombre = str(input("Ingresa primer Nombre : ")) 
apellido = str(input("Ingresa segundo Apellido : "))
nombre_padre =str(input("Ingresa nombre del padre : "))
apellido_padre =str(input("Ingresa apellido del padre : ")) 
nombre_madre = str(input("Ingresa nombre de la madre : "))
apellido_madre = str(input("Ingresa apellido de la madre : "))
concatena(nombre,apellido_padre,apellido_madre,nombre_padre,nombre_madre)



