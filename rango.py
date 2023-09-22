n = int(input("Valor Inicial : "))
m = int(input("Valor Final : "))
s = int(input("Multiplos de : "))

amount = 0 
for i in range (n,m,s):
    amount+=1
    if i%s==0:

     print(i)
print("Cantidad de iteraciones :",amount)
        
