
n = int(input("Ingresa la cantidad de filas : "))
m = int(input("Ingresa la cantidad de columnas : "))

matrix = [[n],[m]]


# for con indice i para las filas
for filas in range(n):
 #For para las columnas
 for columnas in range(m):
    valor = int(input("Ingresa el valor : "))
    matrix.append(valor)

print(matrix,end=" ")    


