"""
Se requiere un DF que solicita ingresar tres valores numericos enteros, y que
determine/muestre al usuario si son numeros consecutivos o no.
"""

print("Escribe 3 valores enteros distintos consecutivos.")

a = int(input("Valor 1 :"))
b = int(input("Valor 2 :"))
c = int(input("Valor 3 :"))

if a > b :
    aux = a
    a = b 
    b = aux

if a > c :
    aux = a 
    a = c 
    c = aux

if a > c :
    b = c
    c = aux


if b == a+1 and c == b+1 :
    print("Los tres valores son numeros consecutivos")
else : 
    print("Los tres valores ingresados no son numeros consecutivos.")
     

