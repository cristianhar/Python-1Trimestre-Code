"""que solicita al usuario cuatro valores enteros en cualquier orden y luego los imprime en
cuatro mensajes de mayor a menor y viceversa. Por ejemplo si el usuario ingresa los valores: 32,
76, 102, 23 el DF imrime mensaje1: 102 – 23, mensaje2: 76 – 32, mensaje3 32 – 76 y mensaje4
23 -102
"""


print("Escribe cuatro valores enteros")
a = int(input("Valor numero a : "))
b = int(input("Valor numero b : "))
c = int(input("Valor numero c : "))
d = int(input("Valor numero d : "))

if a < b :
    aux = a
    a = b
    b = aux

if a < c :
    aux = a 
    a = c
    c = aux

if a < d : 
    aux = a
    a = d 
    d = aux

if b < c : 
    aux = b 
    b = c
    c = aux

if b < d :
    aux = b
    b = d 
    d = aux        

if c < d : 
    aux = c
    c = d
    d = aux

print("Mensaje1: ",a , "-" , d)
print("Mensaje2: ",b  ,"-" , c)
print("Mensaje3: ",c , "-" , b)
print("Mensaje4: ",d , "-" , a)
