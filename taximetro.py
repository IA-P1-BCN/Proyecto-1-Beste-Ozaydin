import time
import logging
import json
from datetime import datetime


logging.basicConfig(
    filename="taximetro.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


with open("tarifas.json", "r") as archivo:
    tarifas = json.load(archivo)

TARIFA_PARADO = tarifas["parado"]
TARIFA_MOVIMIENTO = tarifas["movimiento"]


def calcular_precio(tiempo, tarifa):
    return tiempo * tarifa


class Taximetro:

    def __init__(self, tarifa_parado, tarifa_movimiento):

        self.tarifa_parado = tarifa_parado
        self.tarifa_movimiento = tarifa_movimiento

        self.carrera_activa = False
        self.estado = None
        self.inicio_estado = None
        self.inicio_carrera = None
        self.precio_total = 0.0


    def iniciar_carrera(self):

        if self.carrera_activa:

            print("Ya hay una carrera activa.")

            logging.warning(
                "Intento de iniciar una carrera ya activa"
            )

        else:

            self.carrera_activa = True
            self.estado = "parado"
            self.inicio_estado = time.time()
            self.inicio_carrera = time.time()
            self.precio_total = 0.0

            print("Carrera iniciada.")
            print("Estado actual: parado.")

            logging.info("Carrera iniciada")
            logging.info("Estado del taxi: parado")


    def mover(self):

        if self.carrera_activa:

            tiempo_actual = time.time()

            tiempo_parado = (
                tiempo_actual - self.inicio_estado
            )

            if self.estado == "parado":

                precio_parado = calcular_precio(
                    tiempo_parado,
                    self.tarifa_parado
                )

                self.precio_total = (
                    self.precio_total + precio_parado
                )

                print(
                    f"Tiempo parado: "
                    f"{tiempo_parado:.2f} segundos"
                )

                print(
                    f"Precio acumulado: "
                    f"{self.precio_total:.2f} €"
                )

            self.estado = "movimiento"
            self.inicio_estado = time.time()

            print("Taxi en movimiento.")

            logging.info(
                "Estado del taxi: movimiento"
            )

        else:

            print(
                "Primero debes iniciar una carrera."
            )

            logging.warning(
                "Intento de mover el taxi "
                "sin carrera activa"
            )


    def parar(self):

        if self.carrera_activa:

            tiempo_actual = time.time()

            tiempo_movimiento = (
                tiempo_actual - self.inicio_estado
            )

            if self.estado == "movimiento":

                precio_movimiento = calcular_precio(
                    tiempo_movimiento,
                    self.tarifa_movimiento
                )

                self.precio_total = (
                    self.precio_total + precio_movimiento
                )

                print(
                    f"Tiempo en movimiento: "
                    f"{tiempo_movimiento:.2f} segundos"
                )

                print(
                    f"Precio acumulado: "
                    f"{self.precio_total:.2f} €"
                )

            self.estado = "parado"
            self.inicio_estado = time.time()

            print("Taxi parado.")

            logging.info(
                "Estado del taxi: parado"
            )

        else:

            print(
                "Primero debes iniciar una carrera."
            )

            logging.warning(
                "Intento de parar el taxi "
                "sin carrera activa"
            )


    def finalizar_carrera(self):

        if self.carrera_activa:

            tiempo_actual = time.time()

            if self.estado == "parado":

                tiempo_parado = (
                    tiempo_actual - self.inicio_estado
                )

                precio_parado = calcular_precio(
                    tiempo_parado,
                    self.tarifa_parado
                )

                self.precio_total = (
                    self.precio_total + precio_parado
                )

            elif self.estado == "movimiento":

                tiempo_movimiento = (
                    tiempo_actual - self.inicio_estado
                )

                precio_movimiento = calcular_precio(
                    tiempo_movimiento,
                    self.tarifa_movimiento
                )

                self.precio_total = (
                    self.precio_total + precio_movimiento
                )

            duracion_carrera = (
                tiempo_actual - self.inicio_carrera
            )

            fecha = datetime.now()

            print("Carrera finalizada.")

            print(
                f"Duración: "
                f"{duracion_carrera:.2f} segundos"
            )

            print(
                f"Total a pagar: "
                f"{self.precio_total:.2f} €"
            )

            logging.info(
                f"Carrera finalizada. "
                f"Total: {self.precio_total:.2f} €"
            )

            with open(
                "historial.txt",
                "a"
            ) as archivo:

                archivo.write(
                    f"Fecha: {fecha} - "
                    f"Duración: "
                    f"{duracion_carrera:.2f} segundos - "
                    f"Total: {self.precio_total:.2f} €\n"
                )

            self.carrera_activa = False
            self.estado = None
            self.inicio_estado = None
            self.inicio_carrera = None

        else:

            print(
                "No hay ninguna carrera activa."
            )

            logging.warning(
                "Intento de finalizar "
                "sin carrera activa"
            )


if __name__ == "__main__":

    taximetro = Taximetro(
        TARIFA_PARADO,
        TARIFA_MOVIMIENTO
    )

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

            taximetro.iniciar_carrera()

        elif comando == "move":

            taximetro.mover()

        elif comando == "stop":

            taximetro.parar()

        elif comando == "finish":

            taximetro.finalizar_carrera()

        elif comando == "exit":

            print("Programa cerrado.")

            logging.info("Programa cerrado")

            break

        else:

            print("Comando no válido.")

            logging.warning(
                f"Comando no válido: {comando}"
            )