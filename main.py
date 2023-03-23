# Pedir al usuario que ingrese varias entradas
nombre = input("Ingresa un nombre: ")
adjetivo = input("Ingresa un adjetivo: ")
verbo = input("Ingresa un verbo: ")
lugar = input("Ingresa un lugar: ")

# Construir la historia utilizando las entradas del usuario
historia = f"Había una vez un(a) {adjetivo} {nombre} que quería {verbo} en {lugar}."
# Por ejemplo: "Había una vez un(a) valiente Juan que quería volar en el cielo."

# Imprimir la historia construida
print(historia)

