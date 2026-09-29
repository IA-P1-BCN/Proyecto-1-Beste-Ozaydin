import tkinter as tk
import time

from taximetro import Taximetro, TARIFA_PARADO, TARIFA_MOVIMIENTO


taximetro = Taximetro(
    TARIFA_PARADO,
    TARIFA_MOVIMIENTO
)


ventana = tk.Tk()
ventana.title("Taxímetro Digital")
ventana.geometry("400x550")


label_estado = tk.Label(
    ventana,
    text="Estado: sin carrera",
    font=("Arial", 16)
)
label_estado.pack(pady=10)


label_precio = tk.Label(
    ventana,
    text="Precio: 0.00 €",
    font=("Arial", 20)
)
label_precio.pack(pady=10)


label_mensaje = tk.Label(
    ventana,
    text="",
    font=("Arial", 12)
)
label_mensaje.pack(pady=10)


def actualizar_interfaz():
    if taximetro.estado is None:
        texto_estado = "sin carrera"
    else:
        texto_estado = taximetro.estado

    label_estado.config(
        text=f"Estado: {texto_estado}"
    )

    label_precio.config(
        text=f"Precio: {taximetro.precio_total:.2f} €"
    )


def actualizar_precio_en_vivo():
    if taximetro.carrera_activa:

        tiempo_actual = time.time()

        tiempo_actual_estado = (
            tiempo_actual - taximetro.inicio_estado
        )

        if taximetro.estado == "parado":
            precio_actual_estado = (
                tiempo_actual_estado
                * taximetro.tarifa_parado
            )

        elif taximetro.estado == "movimiento":
            precio_actual_estado = (
                tiempo_actual_estado
                * taximetro.tarifa_movimiento
            )

        else:
            precio_actual_estado = 0.0

        precio_mostrado = (
            taximetro.precio_total
            + precio_actual_estado
        )

        label_precio.config(
            text=f"Precio: {precio_mostrado:.2f} €"
        )

    ventana.after(
        500,
        actualizar_precio_en_vivo
    )


def iniciar_desde_gui():
    if taximetro.carrera_activa:
        label_mensaje.config(
            text="Ya hay una carrera activa."
        )
    else:
        taximetro.iniciar_carrera()

        label_mensaje.config(
            text="Carrera iniciada."
        )

    actualizar_interfaz()


def mover_desde_gui():
    if taximetro.carrera_activa:
        taximetro.mover()

        label_mensaje.config(
            text="Taxi en movimiento."
        )
    else:
        label_mensaje.config(
            text="Primero debes iniciar una carrera."
        )

    actualizar_interfaz()


def parar_desde_gui():
    if taximetro.carrera_activa:
        taximetro.parar()

        label_mensaje.config(
            text="Taxi parado."
        )
    else:
        label_mensaje.config(
            text="Primero debes iniciar una carrera."
        )

    actualizar_interfaz()


def finalizar_desde_gui():
    if taximetro.carrera_activa:
        taximetro.finalizar_carrera()

        label_mensaje.config(
            text="Carrera finalizada."
        )
    else:
        label_mensaje.config(
            text="No hay ninguna carrera activa."
        )

    actualizar_interfaz()


def salir():
    ventana.destroy()


boton_start = tk.Button(
    ventana,
    text="Iniciar carrera",
    command=iniciar_desde_gui,
    width=20,
    height=2
)
boton_start.pack(pady=5)


boton_move = tk.Button(
    ventana,
    text="En movimiento",
    command=mover_desde_gui,
    width=20,
    height=2
)
boton_move.pack(pady=5)


boton_stop = tk.Button(
    ventana,
    text="Parado",
    command=parar_desde_gui,
    width=20,
    height=2
)
boton_stop.pack(pady=5)


boton_finish = tk.Button(
    ventana,
    text="Finalizar carrera",
    command=finalizar_desde_gui,
    width=20,
    height=2
)
boton_finish.pack(pady=5)


boton_exit = tk.Button(
    ventana,
    text="Salir",
    command=salir,
    width=20,
    height=2
)
boton_exit.pack(pady=10)


actualizar_precio_en_vivo()

ventana.mainloop()