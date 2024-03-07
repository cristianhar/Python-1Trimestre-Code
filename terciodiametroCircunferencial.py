"""
Se requiere un DF que permita ingresar el tercio de diámetro de una circunferencia y que
muestre el valor de su volumen.
"""


a = int(input("Ingresa el tercio del diámetro de la circunferencia: "))

PI = 3.14159
terciodiametro = 0
radio = 0
volumen = 0

radio = a / 3
volumen = PI * radio * radio * radio* 2 
print("El volumen del cilindro es" , volumen)
