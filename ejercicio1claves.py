#Escriba un programa python para devolver todos los elementos unicos de un conjunto el cual
#debe tener una cantidad n aleatorio y los valores de cada elemento deben estar entre 0 y 9

import random
x = set()
y =set()
n = random.randint(100,5000)
m = random.randint(100,5000)
#x={random.randint(0,9) * n for i in range(n)}
#y= {random.randint(0,9) * n for i in range(n)}
conjunto1={}
conjunto2={}
con

for i in range(n):
    ale1=random.randint(0,9)
    conjunto1.add(ale1)
    conjunto1[ale1]+=1

for i in range(m):
    ale2=random.randint(0,9)
    conjunto2.add(ale2)
    conjunto2[ale2]+=1   
    

print(x)
print(y)
print(conjunto1)
print(conjunto2)