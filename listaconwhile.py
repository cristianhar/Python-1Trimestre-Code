#Algoritmo que llena manual/te una lista de 4 numeros
#De manera manual
"""
n,i,lista = 4 ,1,[]

while i<=n:
    aux = int(input(f"Ingresa el valor #{i} :"))
    lista.append(aux)
    i = i +1
print(lista)"""
n,lista = 4 ,[]
i = 1
while len(lista)< n:
    aux = int(input(f"Ingresa el valor #{i} :"))
    lista.append(aux)
    i=i+1

print(lista)