import operator
dicc_aprendices= {'Johao': 25, 'Adrian': 16, 'Dayan': 31, 'Julian': 17, 'Ossa': 16}
diccordenado = dict(sorted(dicc_aprendices.items(),key = operator.itemgetter(0)))
menores_de_edad ={}
mayores_de_edad ={}
for llave , valor in diccordenado.items():
    print(f"Aprendiz {llave}, tiene {valor} años.")
    if int(valor) < 18 :
        menores_de_edad[llave] = valor
    else : mayores_de_edad[llave] =valor

print("Listado de Menores de Edad:")
for clave, valor in menores_de_edad.items():
    print(f'{clave}: {valor}')

print("Listado de Mayores de Edad:")
for clave, valor in mayores_de_edad.items():
    print(f'{clave}: {valor}')
