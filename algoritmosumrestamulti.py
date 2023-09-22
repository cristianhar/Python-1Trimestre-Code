#Algoritmo que realiza suma , resta , multiplicacion dentro de una sola funcion


def m_calculo(a,b):
    
    produ = a*b
    suma = a+b
    resta = a-b
    return produ , suma , resta

r=int(input("Ingresa el primer valor",))
s=int(input("Ingresa el segundo valor",))
producto,sumaRes,restaRes = m_calculo(r,s) 
print("El resultado del producto es : ",producto)
