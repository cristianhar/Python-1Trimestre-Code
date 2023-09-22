"""""
def suma_ab():
    a=int(input("Ingresa a: ")) 
    b= int(input("Ingresa b: ")) 
    print("La suma es :  ", a+b)

suma_ab()
"""
import math
"""
def suma_ab():
    a=int(input("Ingresa a: ")) 
    b= int(input("Ingresa b: ")) 
    print("La suma es :  ", a+b)
"""

"""
def suma(p,n):
    print("la suma es : ",p+n)
"""
"""
def suma(a,b):
    print("La suma es : ",a+b)
    """
"""
def raiz(n):
    print("La raiz es :",math.sqrt(n)) 

g =int(input("Ingresa el valor a encontrar su raiz: "))

raiz(g)
"""

""""

def multiplicarValue(numero):
   for i in range(1,11):
     print(f"Tabla de {numero} * {i} :", i*numero)

valor =int(input("Que tabla deseas operar : "))        
multiplicarValue(valor)
"""

def factorialValor(numero):
   factor = 1
   for i in range(1,numero+1):
     factor = factor*i
   print(f"Factorial de  {numero} es  :", factor)

valor = int(input("El factorial de  : "))        
factorialValor(valor)     