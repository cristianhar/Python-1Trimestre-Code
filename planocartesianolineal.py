X1 = int(input("Valor X1 : "))
Y1 = int(input("Valor Y1 : "))
X2 = int(input("Valor X2 : "))
Y2 = int(input("Valor Y2 : "))
X3 = int(input("Valor X3 : "))
Y3 = int(input("Valor Y3 : "))


pendienteuno = (Y2 - Y1) / (X2 - X1) if X2 - X1 != 0 else float('inf')  # Pendiente entre P1 y P2
pendientedos = (Y3 - Y1) / (X3 - X1) if X3 - X1 != 0 else float('inf')  # Pendiente entre P1 y P3

if pendienteuno == pendientedos:
    print("Los puntos son lineales.")
else:
    print("Los puntos no son lineales.")

