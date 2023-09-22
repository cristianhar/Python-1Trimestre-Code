import random

Dicc_lot = {'Lunes':'Bucaramangas','Martes':'Astroluna','Miercoles':'Cafetero','Jueves':'Baloto','Viernes':'Medellin','Sabado':'Atr'}

dia_semana = random.choice(list(Dicc_lot.keys()))
loteria = Dicc_lot[dia_semana]

print(f"Día de la semana: {dia_semana}")
print(f"Lotería: {loteria}")

