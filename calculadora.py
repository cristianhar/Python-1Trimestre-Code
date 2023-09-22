#Calculadora Johao amiwinho 
import math

def operacion(valor):
    if  valor == 1:
        print("Bienvenido vas a sumar dos Valores :")
        a = int(input("Valor a  : "))
        b = int(input("Valor b  : "))
        return a+b
    
    elif valor == 2:
        print("Bienvenido vas a restar dos Valores :")
        a = int(input("Valor a  : "))
        b = int(input("Valor b  : "))
        return a-b 
    elif valor == 3:
        print("Bienvenido vas a multiplicar dos Valores :")
        a = int(input("Valor a  : "))
        b = int(input("Valor b  : "))
        return a*b
    elif valor == 4:
        print("Bienvenido vas a dividir dos Valores :")
        a = int(input("Valor a  : "))
        b = int(input("Valor b  : "))
        return a/b 
    elif valor == 5: 
        print("Bienvenido vas a potenciar dos Valores :")
        a = int(input("Valor a  : "))
        b = int(input("Valor b (Exponente)  : "))
        return a**b
    
    elif valor == 6: 
        print("Bienvenido vas a sacar porcentaje a dos Valores :")
        a = int(input("Valor a (Porcentaje)  : "))
        b = int(input("Valor b   : "))
        return a%b
    elif valor == 7: 
        print("Bienvenido vas a sacar el logarimo al valor:")
        a = int(input("Valor a  : "))
        return math.log10(a)
    elif valor == 8: 
        print("Bienvenido vas a sacar la raiz cuadrada  al valor:")
        a = int(input("Valor a  : "))
        return math.sqrt(a)
    
    else : print("Ingresaste una operacion no valida :")

print("1.Sumar , 2.Restar , 3.Multiplicar,4.Dividir , 5.Potenciacion,6.Modulo,7.Logaritmo,8.Raiz")
valor = int(input("Que quieres hacer digita un Numero : "))

print(operacion(valor))   