n = int(input("Ingrese la dimensión cuadrada de la matriz (debe ser múltiplo de 4): "))

if n % 4 != 0:
    print("La dimensión de la matriz debe ser un múltiplo de 4.")
else:

    matriz = [[0] * n for _ in range(n)]

    for fila in range(n):
        for columna in range(n):
            if (fila // 4) % 2 == 0:
                if (columna // 4) % 2 == 0:
                    matriz[fila][columna] = 1
            else:
                if (columna // 4) % 2 != 0:
                    matriz[fila][columna] = 1

    # Imprimir la matriz en el formato deseado
    for fila in range(n):
        for columna in range(n):
            print(matriz[fila][columna], end=" ")
        print()
