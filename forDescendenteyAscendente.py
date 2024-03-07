"""
DF para solicitar al usuario dos números enteros, luego mediante el uso de bucle For debe
imprimir los primeros 10 múltiplos e imprimirlos a la vez, unos en forma ascendente y los otros
múltiplos de forma descendente.
"""

a = int(input("Ingresa el primer valor entero : "))
b = int(input("Ingresa el segundo valor entero : "))
i = 1
j = 11

for i in range (1,11):
    j = j -1 
    productoa = a * i
    productob = b * j
    print("Multiplos del primer valor : " ,productoa, "Multiplos del Segundo valor",productob)

