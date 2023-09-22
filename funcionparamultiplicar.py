def multiplicarValue(numero):
   for i in range(1,11):
     print(f"Tabla de {numero} * {i} :", i*numero)

valor =int(input("Que tabla deseas operar : "))        
multiplicarValue(valor)