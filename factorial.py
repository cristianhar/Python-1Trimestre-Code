def factorialValor(numero):
   factor = 1
   for i in range(1,numero+1):
     factor *= i
   print(f"Factorial de  {numero} es  :", factor)

valor = int(input("El factorial de  : "))        
factorialValor(valor)     
