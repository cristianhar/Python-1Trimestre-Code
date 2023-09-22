# Algoritmo que solicita un nombre al usuario y cuenta cuántas veces se repiten las vocales
# y las agrega a un diccionario de vocales, luego las imprime verticalmente.

vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
nombre = input("Ingresa el Nombre: ")

for letra in nombre:  
    if letra in 'aeiou':
        vocales[letra] += 1

print("Diccionario de Vocales:")
for vocal, cantidad in vocales.items():
    if cantidad > 0:
        if cantidad ==1:
            print(f'{vocal}: {cantidad} Vez')
        else : print(f'{vocal}: {cantidad} Veces')



