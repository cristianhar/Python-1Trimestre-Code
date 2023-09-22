import random

while True:
    valor = int(input("¿Qué quieres hacer? 1.Sumar , 2.Restar, 3.Salir: "))
    if valor == 3:
        print("Has salido del programa")
        break
    elif valor ==1 :
        a = random.randint(1, 100000)
        b = random.randint(1, 100000)
        resultado = a + b 
        print(f"Resultado de la suma de {a} + {b}: ", resultado)
    elif valor == 2 :
        a = random.randint(1, 100000)
        b = random.randint(1, 100000)
        resultado = a - b 
        print(f"Resultado de la resta de {a} - {b}: ", resultado)   
    else:
        print("Has introducido un valor inválido, vuelve a digitar")
