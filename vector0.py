#Algoritmo que pide un valor n (n x n ) e imprime la matriz de nxn llena de 0 
n = int(input("Valor de N :"))
matriz = [[n]]


for filas in range(n):
 for columnas in range(n):
    valor = int(input(f"Valor de {filas}'{columnas} :"))
    matriz.append(valor)
    

print(matriz)    