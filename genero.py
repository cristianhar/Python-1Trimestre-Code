genero =  str(input("Ingresa F o M segun el genero :"))
edad = int(input("Ingresa la edad : "))

if "F" in genero:
    if edad >18 :
        print(f"Mujer con {edad} años")
    else : print (f"Niña con {edad} años")    
else :
    if edad > 18 :
        print(f"Hombre con : {edad} años")
    else : print (f"Niño con {edad} años")