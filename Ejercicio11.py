"""
11.  para ingresar valores enteros hasta encontrar un múltiplo de 17.

"""



while True :
        try:
            
            numero = int(input("Ingresa un valor entero :"))
            if numero % 17 == 0:

                print(f"{numero} es un múltiplo de 17. ¡Encontraste uno!")
                break  # Sale del ciclo while si se encuentra un múltiplo de 17

            else:
                 print(f"{numero} no es un múltiplo de 17. Sigue intentando.")
        except ValueError:
         print("Por favor, ingresa un valor entero válido.")

