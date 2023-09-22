"""
DF que solicita al usuario un valor entero mayor a tres cifras y muestra impreso en orden
inverso. Por ejemplo se ingresa el 20345 y se imprime el 54302.
"""

print("Escribir un valor entero mayor a tres cifras")
a = int(input("Valor numero a : "))


numeroinverso = 0 
largo = 0 

while a > 0 : #Mientras a sea mayor que 0 Hacer....
    digito = a % 10 
    a //= 10
    numeroinverso = numeroinverso * 10 + digito
    largo = largo + 1
   
print(numeroinverso)
print(largo)
