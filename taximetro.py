import time
import logging
from datetime import datetime


logging.basicConfig(
    filename="taximetro.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


TARIFA_PARADO = 0.02
TARIFA_MOVIMIENTO = 0.05

carrera_activa = False
estado = None
inicio_estado = None
inicio_carrera = None
precio_total = 0.0


print("=== TAXÍMETRO DIGITAL ===")
print("Comandos disponibles:")
print("start - Iniciar carrera")
print("move - Taxi en movimiento")
print("stop - Taxi parado")
print("finish - Finalizar carrera")
print("exit - Salir del programa")

logging.info("Programa iniciado")


while True:

    comando = input("Escribe un comando: ")

    if comando == "start":

        if carrera_activa:
            print("Ya hay una carrera activa.")
            logging.warning("Intento de iniciar una carrera ya activa")

        else:
            carrera_activa = True
            estado = "parado"

            inicio_estado = time.time()
            inicio_carrera = time.time()

            precio_total = 0.0

            print("Carrera iniciada.")
            print("Estado actual: parado.")

            logging.info("Carrera iniciada")
            logging.info("Estado del taxi: parado")


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

            logging.info("Estado del taxi: movimiento")

        else:
            print("Primero debes iniciar una carrera.")

            logging.warning(
                "Intento de mover el taxi sin carrera activa"
            )


    elif comando == "stop":

        if carrera_activa:

            tiempo_actual = time.time()
            tiempo_movimiento = tiempo_actual - inicio_estado

            if estado == "movimiento":

                precio_movimiento = (
                    tiempo_movimiento * TARIFA_MOVIMIENTO
                )

                precio_total = precio_total + precio_movimiento

                print(
                    f"Tiempo en movimiento: "
                    f"{tiempo_movimiento:.2f} segundos"
                )

                print(f"Precio acumulado: {precio_total:.2f} €")

            estado = "parado"
            inicio_estado = time.time()

            print("Taxi parado.")

            logging.info("Estado del taxi: parado")

        else:
            print("Primero debes iniciar una carrera.")

            logging.warning(
                "Intento de parar el taxi sin carrera activa"
            )


    elif comando == "finish":

        if carrera_activa:

            tiempo_actual = time.time()

            if estado == "parado":

                tiempo_parado = tiempo_actual - inicio_estado
                precio_parado = tiempo_parado * TARIFA_PARADO
                precio_total = precio_total + precio_parado

            elif estado == "movimiento":

                tiempo_movimiento = tiempo_actual - inicio_estado

                precio_movimiento = (
                    tiempo_movimiento * TARIFA_MOVIMIENTO
                )

                precio_total = precio_total + precio_movimiento


            duracion_carrera = tiempo_actual - inicio_carrera
            fecha = datetime.now()


            print("Carrera finalizada.")
            print(f"Duración: {duracion_carrera:.2f} segundos")
            print(f"Total a pagar: {precio_total:.2f} €")


            logging.info(
                f"Carrera finalizada. Total: {precio_total:.2f} €"
            )


            with open("historial.txt", "a") as archivo:

                archivo.write(
                    f"Fecha: {fecha} - "
                    f"Duración: {duracion_carrera:.2f} segundos - "
                    f"Total: {precio_total:.2f} €\n"
                )


            carrera_activa = False
            estado = None
            inicio_estado = None
            inicio_carrera = None


        else:
            print("No hay ninguna carrera activa.")

            logging.warning(
                "Intento de finalizar sin carrera activa"
            )


    elif comando == "exit":

        print("Programa cerrado.")

        logging.info("Programa cerrado")

        break


    else:

        print("Comando no válido.")

        logging.warning(
            f"Comando no válido: {comando}"
        )