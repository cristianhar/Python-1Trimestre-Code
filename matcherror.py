error = input("Introduzca un codigo de error:\n")

match error:
    case '200':
        print("todo ok")
    case '301':
        print ("Movimiento permanente de la pagina")
    case '302':
        print("Movimiento temporal de la página.")
    case '404':
        print("Página no encontrada.")
    case '500':
        print("Error interno del servidor")
    case '503':
        print("Servicio no disponible")
    case _:
        print("Error no disponible")