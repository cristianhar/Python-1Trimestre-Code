def ingresar_vector(numero):
    vector = []
    print(f"Ingrese los elementos del vector {numero} (ordenados ascendentemente):")
    for i in range(5):
        while True:
            try:
                elemento = int(input(f"Ingrese el elemento {i+1}: "))
                if i > 0 and elemento <= vector[i-1]:
                    print("Error: El elemento debe ser mayor al anterior.")
                else:
                    vector.append(elemento)
                    break
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")
    return vector

vector1 = ingresar_vector(1)
vector2 = ingresar_vector(2)

indice1 = 0
indice2 = 0
resultado = []

while indice1 < len(vector1) and indice2 < len(vector2):
    if vector1[indice1] < vector2[indice2]:
        resultado.append(vector1[indice1])
        indice1 += 1
    else:
        resultado.append(vector2[indice2])
        indice2 += 1

resultado.extend(vector1[indice1:])
resultado.extend(vector2[indice2:])

print("\nResultado de la mezcla de vectores ordenados:")
print(resultado)
