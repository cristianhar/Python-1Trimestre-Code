"""""

numero = int(input("Ingresa la tabla que quieres operar"))

for valor in range (1,21):
    print(f"{numero} x {valor} = ",numero*valor)
"""

numero = int(input("Ingresa la tabla que quieres operar: "))
tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for factor in tabla:
    resultado = numero * factor
    print(f"{numero} * {factor} = {resultado}")