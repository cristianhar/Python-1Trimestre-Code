def sum_ab(a,b):
    return a+b
#Fin funcion ssuma
evento ="si"
while evento != "no":
    p= int(input("Valor A:"))
    q= int(input("Valor b:"))
    print(sum_ab(p,q))    
    evento = str(input("Digita  -no- para salir : "))