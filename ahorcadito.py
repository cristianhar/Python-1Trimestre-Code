import random

def seleccionar_palabra():
    palabras = ["clase", "banano", "computadora", "desarrollo", "juego", "codigo", "teclado"]
    return random.choice(palabras)

def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    palabra_adivinada = ["_"] * len(palabra_secreta)
    intentos_restantes = 6
    letras_intentadas = []

    print("¡Bienvenido al juego de Ahorcado!")
    print("Estoy pensando en una palabra. Adivina las letras una por una.")
    print(" ".join(palabra_adivinada))

    while "_" in palabra_adivinada and intentos_restantes > 0:
        letra = input("\nIngresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una sola letra válida.")
            continue

        if letra in letras_intentadas:
            print("Ya has intentado esta letra antes.")
            continue

        letras_intentadas.append(letra)

        if letra in palabra_secreta:
            print("¡Correcto! La letra está en la palabra.")
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_adivinada[i] = letra
        else:
            print("Incorrecto. La letra no está en la palabra.")
            intentos_restantes -= 1

        print(" ".join(palabra_adivinada))
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras intentadas: {' '.join(letras_intentadas)}")

    if "_" not in palabra_adivinada:
        print("¡Felicidades! Has adivinado la palabra: " + "".join(palabra_adivinada))
    else:
        print("¡Agotaste tus intentos! La palabra era: " + palabra_secreta)

jugar_ahorcado()
