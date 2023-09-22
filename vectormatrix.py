n = int(input("Ingresa la cantidad de filas: "))
m = int(input("Ingresa la cantidad de columnas: "))
matrix = []

for filas in range(n):
    row = []
    for columnas in range(m):
        valor = int(input(f"Ingresa el valor {filas}{columnas}: "))
        row.append(valor)
    matrix.append(row)

negativo = False
suma = 0

for fila in matrix:
    for valor in fila:
        if valor < 0:
            negativo = True
        suma += valor

if suma % 2 == 0 and negativo:
    for fila in matrix:
        fila.reverse()

print("Matriz:")
for fila in matrix:
    print(fila)
print("Suma:", suma)
