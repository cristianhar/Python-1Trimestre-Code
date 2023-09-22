import random
#Usuario escoge n y de lista es cuadrada nxn la llena de manera aleatoria con valores de 0 a 9
i,j,n = 0,0,10
matrizCuadrada = []

while i <10:
    
    j=0  
    
    while j<10:
        aux = random.randint(0,9)
        matrizCuadrada.append(aux)
        print(aux,end = " ")

        j+=1
    print()      
    i +=1     
