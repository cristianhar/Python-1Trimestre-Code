import match
def obtener_dia_semana(numero):
    nombre_dia = match numero:
        case 1:
            "Lunes"
        case 2:
            "Martes"
        case 3:
            "Miércoles"
        case 4:
            "Jueves"
        case 5:
            "Viernes"
        case 6:
            "Sábado"
        case 7:
            "Domingo"
        case _:
            "Número inválido"
    return nombre_dia

numero = 3
dia_semana = obtener_dia_semana(numero)
print(f"El número {numero} corresponde a {dia_semana}")
