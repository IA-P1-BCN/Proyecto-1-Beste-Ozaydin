TARIFA_PARADO = 0.02
TARIFA_MOVIMIENTO = 0.05

carrera_activa = False
estado = None

print("=== TAXÍMETRO DIGITAL ===")
print("Comandos disponibles:")
print("start - Iniciar carrera")
print("stop - Taxi parado")
print("move - Taxi en movimiento")
print("finish - Finalizar carrera")
print("exit - Salir del programa")

while True:
    comando = input("Escribe un comando: ")

    if comando == "start":
        carrera_activa = True
        estado = "parado"
        print("Carrera iniciada.")
        print("Estado actual: parado.")

    elif comando == "stop":
        if carrera_activa:
            estado = "parado"
            print("Taxi parado.")
        else:
            print("Primero debes iniciar una carrera.")

    elif comando == "move":
        if carrera_activa:
            estado = "movimiento"
            print("Taxi en movimiento.")
        else:
            print("Primero debes iniciar una carrera.")

    elif comando == "finish":
        if carrera_activa:
            carrera_activa = False
            estado = None
            print("Carrera finalizada.")
        else:
            print("No hay ninguna carrera activa.")

    elif comando == "exit":
        print("Programa cerrado.")
        break

    else:
        print("Comando no válido.")