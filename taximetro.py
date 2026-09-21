import time

TARIFA_PARADO = 0.02
TARIFA_MOVIMIENTO = 0.05

carrera_activa = False
estado = None
inicio_estado = None
precio_total = 0.0

print("=== TAXÍMETRO DIGITAL ===")
print("Comandos disponibles:")
print("start - Iniciar carrera")
print("move - Taxi en movimiento")
print("stop - Taxi parado")
print("finish - Finalizar carrera")
print("exit - Salir del programa")

while True:
    comando = input("Escribe un comando: ")

    if comando == "start":
        if carrera_activa:
            print("Ya hay una carrera activa.")

        else:
            carrera_activa = True
            estado = "parado"
            inicio_estado = time.time()
            precio_total = 0.0

            print("Carrera iniciada.")
            print("Estado actual: parado.")

    elif comando == "move":
        if carrera_activa:
            tiempo_actual = time.time()
            tiempo_parado = tiempo_actual - inicio_estado

            if estado == "parado":
                precio_parado = tiempo_parado * TARIFA_PARADO
                precio_total = precio_total + precio_parado

                print(f"Tiempo parado: {tiempo_parado:.2f} segundos")
                print(f"Precio acumulado: {precio_total:.2f} €")

            estado = "movimiento"
            inicio_estado = time.time()

            print("Taxi en movimiento.")

        else:
            print("Primero debes iniciar una carrera.")

    elif comando == "stop":
        if carrera_activa:
            tiempo_actual = time.time()
            tiempo_movimiento = tiempo_actual - inicio_estado

            if estado == "movimiento":
                precio_movimiento = tiempo_movimiento * TARIFA_MOVIMIENTO
                precio_total = precio_total + precio_movimiento

                print(
                    f"Tiempo en movimiento: {tiempo_movimiento:.2f} segundos"
                )
                print(f"Precio acumulado: {precio_total:.2f} €")

            estado = "parado"
            inicio_estado = time.time()

            print("Taxi parado.")

        else:
            print("Primero debes iniciar una carrera.")

    elif comando == "finish":
        if carrera_activa:
            tiempo_actual = time.time()

            if estado == "parado":
                tiempo_parado = tiempo_actual - inicio_estado
                precio_parado = tiempo_parado * TARIFA_PARADO
                precio_total = precio_total + precio_parado

            elif estado == "movimiento":
                tiempo_movimiento = tiempo_actual - inicio_estado
                precio_movimiento = tiempo_movimiento * TARIFA_MOVIMIENTO
                precio_total = precio_total + precio_movimiento

            carrera_activa = False
            estado = None
            inicio_estado = None

            print("Carrera finalizada.")
            print(f"Total a pagar: {precio_total:.2f} €")

        else:
            print("No hay ninguna carrera activa.")

    elif comando == "exit":
        print("Programa cerrado.")
        break

    else:
        print("Comando no válido.")