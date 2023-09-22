
def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a


def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)

a = int(input("Valor a para hallar mcm : "))
b = int(input("Valor b para hallar mcm : "))
mcm = minimo_comun_multiplo(a, b)
print(f"El mínimo común múltiplo de {a} y {b} es {mcm}")

