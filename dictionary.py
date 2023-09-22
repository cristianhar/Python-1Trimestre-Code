# Algoritmo que mediante una función imprime el diccionario organizado alfabéticamente y separa por edades.
def printOrdenado(diccionario):
    # Ordena las claves del diccionario alfabéticamente
    claves_ordenadas = sorted(diccionario.keys())
    print("Listado ordenado Alfabeticamente ")

    for clave in claves_ordenadas:
        valor = diccionario[clave]
        print(f'{clave}: {valor}')

    menores_de_edad = {}
    mayores_de_edad = {}

    for clave, valor in diccionario.items():
        if int(valor) < 18:
            menores_de_edad[clave] = valor
        else:
            mayores_de_edad[clave] = valor

    print("Listado de Menores de Edad:")
    for clave, valor in menores_de_edad.items():
        print(f'{clave}: {valor}')

    print("Listado de Mayores de Edad:")
    for clave, valor in mayores_de_edad.items():
        print(f'{clave}: {valor}')

EdadAp = {'Johao': 25, 'Adrian': 16, 'Dayan': 31, 'Julian': 17, 'Ossa': 16}
printOrdenado(EdadAp)
