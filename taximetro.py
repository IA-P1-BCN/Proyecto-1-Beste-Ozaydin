import time
import logging
import json
import hashlib
import secrets
import hmac
import os

from getpass import getpass
from datetime import datetime


# -----------------------------
# LOGGING
# -----------------------------

logging.basicConfig(
    filename="taximetro.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -----------------------------
# TARIFAS
# -----------------------------

with open("tarifas.json", "r") as archivo:
    tarifas = json.load(archivo)

TARIFA_PARADO = tarifas["parado"]
TARIFA_MOVIMIENTO = tarifas["movimiento"]


# -----------------------------
# CÁLCULO DE PRECIO
# -----------------------------

def calcular_precio(tiempo, tarifa):
    return tiempo * tarifa


# -----------------------------
# CONTRASEÑA
# -----------------------------

def crear_hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        200000
    )


def guardar_password(password):
    salt = secrets.token_bytes(16)

    password_hash = crear_hash_password(
        password,
        salt
    )

    datos = {
        "salt": salt.hex(),
        "password_hash": password_hash.hex()
    }

    with open("auth.json", "w") as archivo:
        json.dump(datos, archivo)


def comprobar_password(password):
    if not os.path.exists("auth.json"):
        return False

    with open("auth.json", "r") as archivo:
        datos = json.load(archivo)

    salt = bytes.fromhex(
        datos["salt"]
    )

    password_hash_guardado = bytes.fromhex(
        datos["password_hash"]
    )

    password_hash_introducido = crear_hash_password(
        password,
        salt
    )

    return hmac.compare_digest(
        password_hash_introducido,
        password_hash_guardado
    )


def crear_password():
    print("Primera ejecución.")
    print("Crea una contraseña para acceder al taxímetro.")

    password = getpass("Nueva contraseña: ")
    password_repetida = getpass(
        "Repite la contraseña: "
    )

    if password != password_repetida:
        print("Las contraseñas no coinciden.")
        return False

    if password == "":
        print("La contraseña no puede estar vacía.")
        return False

    guardar_password(password)

    print("Contraseña creada correctamente.")

    return True


def verificar_password():
    password = getpass(
        "Introduce la contraseña: "
    )

    return comprobar_password(password)


# -----------------------------
# CLASE TAXÍMETRO
# -----------------------------

class Taximetro:

    def __init__(
        self,
        tarifa_parado,
        tarifa_movimiento
    ):
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
            return

        self.carrera_activa = True
        self.estado = "parado"

        self.inicio_estado = time.time()
        self.inicio_carrera = time.time()

        self.precio_total = 0.0

        print("Carrera iniciada.")
        print("Taxi parado.")

        logging.info("Carrera iniciada")


    def mover(self):

        if not self.carrera_activa:
            print(
                "Primero debes iniciar una carrera."
            )
            return

        tiempo_actual = time.time()

        if self.estado == "parado":

            tiempo_parado = (
                tiempo_actual
                - self.inicio_estado
            )

            precio_parado = calcular_precio(
                tiempo_parado,
                self.tarifa_parado
            )

            self.precio_total += precio_parado

            print(
                f"Tiempo parado: "
                f"{tiempo_parado:.2f} segundos"
            )

            print(
                f"Precio acumulado: "
                f"{self.precio_total:.2f} €"
            )

        self.estado = "movimiento"
        self.inicio_estado = tiempo_actual

        print("Taxi en movimiento.")

        logging.info(
            "Estado cambiado a movimiento"
        )


    def parar(self):

        if not self.carrera_activa:
            print(
                "Primero debes iniciar una carrera."
            )
            return

        tiempo_actual = time.time()

        if self.estado == "movimiento":

            tiempo_movimiento = (
                tiempo_actual
                - self.inicio_estado
            )

            precio_movimiento = calcular_precio(
                tiempo_movimiento,
                self.tarifa_movimiento
            )

            self.precio_total += precio_movimiento

            print(
                f"Tiempo en movimiento: "
                f"{tiempo_movimiento:.2f} segundos"
            )

            print(
                f"Precio acumulado: "
                f"{self.precio_total:.2f} €"
            )

        self.estado = "parado"
        self.inicio_estado = tiempo_actual

        print("Taxi parado.")

        logging.info(
            "Estado cambiado a parado"
        )


    def finalizar_carrera(self):

        if not self.carrera_activa:
            print(
                "No hay ninguna carrera activa."
            )
            return

        tiempo_actual = time.time()

        tiempo_estado = (
            tiempo_actual
            - self.inicio_estado
        )

        if self.estado == "parado":

            precio_estado = calcular_precio(
                tiempo_estado,
                self.tarifa_parado
            )

            self.precio_total += precio_estado

        elif self.estado == "movimiento":

            precio_estado = calcular_precio(
                tiempo_estado,
                self.tarifa_movimiento
            )

            self.precio_total += precio_estado

        duracion_total = (
            tiempo_actual
            - self.inicio_carrera
        )

        fecha = datetime.now()

        print("Carrera finalizada.")

        print(
            f"Duración: "
            f"{duracion_total:.2f} segundos"
        )

        print(
            f"Total a pagar: "
            f"{self.precio_total:.2f} €"
        )

        logging.info(
            f"Carrera finalizada - "
            f"Duración: {duracion_total:.2f} s - "
            f"Total: {self.precio_total:.2f} €"
        )

        with open(
            "historial.txt",
            "a"
        ) as archivo:

            archivo.write(
                f"Fecha: {fecha} - "
                f"Duración: "
                f"{duracion_total:.2f} segundos - "
                f"Total: "
                f"{self.precio_total:.2f} €\n"
            )

        self.carrera_activa = False
        self.estado = None

        self.inicio_estado = None
        self.inicio_carrera = None


# -----------------------------
# CLI
# -----------------------------

if __name__ == "__main__":

    if not os.path.exists("auth.json"):

        password_creada = crear_password()

        if not password_creada:
            print(
                "No se pudo crear la contraseña."
            )
            raise SystemExit

    acceso_permitido = False

    for intento in range(3):

        if verificar_password():

            print("Acceso permitido.")

            acceso_permitido = True

            break

        else:
            print(
                "Contraseña incorrecta."
            )

    if not acceso_permitido:

        print("Demasiados intentos.")

        raise SystemExit


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

        comando = input(
            "Escribe un comando: "
        )

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

            logging.info(
                "Programa cerrado"
            )

            break

        else:

            print("Comando no válido.")

            logging.warning(
                f"Comando no válido: {comando}"
            )