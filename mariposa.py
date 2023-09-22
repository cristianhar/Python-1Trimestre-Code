n = int(input("Ingrese la dimensión cuadrada de la matriz: "))

# Inicializar una matriz de nxn con todos los elementos iguales a 0
matriz = [[0] * n for _ in range(n)]

# Rellenar las primeras y últimas líneas con 1
for j in range(n):
    matriz[0][j] = 1
    matriz[n - 1][j] = 1

# Rellenar el interior de la mariposa con 1
for i in range(1, n // 2):
    for j in range(i, n - i):
        matriz[i][j] = 1
        matriz[n - i - 1][j] = 1

# Imprimir la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
