"""Realice un DF que solicite al usuario 3 valores enteros positivos. El DF debe mostrar un mensaje
bien sea el caso en el que se afirme que la suma de los cuadrados de los dos primeros valores
equivale al cuadrado del entero mayor ingresado."""



print("Escribe 3 valores enteros positivos")

a = int(input("Escribe el primer entero: "))
b = int(input("Escribe el segundo entero: "))
c = int(input("Escribe el tercer entero: "))

if a >= 0 and b >= 0 and c >= 0:
    aux = 0
    if a > b and a > c:
        aux = a
        SumaCuadrados = b**2 + c**2
    else:
        
        aux = c
        SumaCuadrados = a**2 + b**2
    
    if aux**2 == SumaCuadrados:
        print("La suma de los cuadrados de los dos primeros valores equivale al cuadrado del entero mayor.")
    else:
        print("La suma de los cuadrados de los dos primeros valores no equivale al cuadrado del entero mayor.")
else:
    print("Los valores ingresados no son enteros positivos.")
    
