
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 11
    elif n == 2:
        return 12
    else:
        a, b = 11, 12
        for _ in range(3, n + 1):
            valor_siguiente = a+b # Se suman y se vuelve 23
            a = b # A se vuelve valor 12
            b = valor_siguiente  #este valor es 23 para que al iterar se vuelva 23+12 = 35 en caso de que la entrada sea 4
        return b

n = int(input("Ingrese un valor entero positivo 'n': "))
resultado = fibonacci(n)
print(f"Fb({n}): {resultado}")
