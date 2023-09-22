def descomponer_en_factores_primos(numero):
    factores_primos = []
    divisor = 2

    while numero > 1:
        exponente = 0
        while numero % divisor == 0:
            numero //= divisor
            exponente += 1
        if exponente > 0:
            if exponente == 1:
                factores_primos.append(f"{divisor}")
            else:
                factores_primos.append(f"{divisor}**{exponente}")
        divisor += 1

    return " * ".join(factores_primos)

numero = int(input("Ingrese un número entero positivo: "))
if numero <= 0:
    print("El número debe ser positivo.")
else:
    resultado = descomponer_en_factores_primos(numero)
    print(f"La descomposición en factores primos de {numero} es: {resultado}")
