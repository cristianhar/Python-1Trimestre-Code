"""
DF para sumar los N número enteros positivos y que arroje el resultado (se debe usar bucle
FOR).
"""
i= 1
x = int(input("Ingresa un numero entero positivo para ser sumado : "))
suma = 0
for i  in range (1,x):
    suma = suma + i   

print("El valor de la suma es :", suma)
