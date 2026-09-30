import tkinter as tk
import time
import os

from tkinter import simpledialog, messagebox

from src.taximetro import (
    Taximetro,
    TARIFA_PARADO,
    TARIFA_MOVIMIENTO,
    guardar_password,
    comprobar_password
)


# -----------------------------
# OBJETO TAXÍMETRO
# -----------------------------

taximetro = Taximetro(
    TARIFA_PARADO,
    TARIFA_MOVIMIENTO
)


# -----------------------------
# VENTANA
# -----------------------------

ventana = tk.Tk()

ventana.title(
    "Taxímetro Digital"
)

ventana.geometry(
    "400x550"
)


# Ocultamos la ventana mientras
# comprobamos la contraseña
ventana.withdraw()


# -----------------------------
# AUTENTICACIÓN
# -----------------------------

def autenticar_usuario():

    if not os.path.exists("auth.json"):

        password = simpledialog.askstring(
            "Crear contraseña",
            "Crea una contraseña:",
            show="*"
        )

        if password is None or password == "":

            messagebox.showerror(
                "Error",
                "Debes crear una contraseña."
            )

            return False


        password_repetida = (
            simpledialog.askstring(
                "Crear contraseña",
                "Repite la contraseña:",
                show="*"
            )
        )


        if password != password_repetida:

            messagebox.showerror(
                "Error",
                "Las contraseñas no coinciden."
            )

            return False


        guardar_password(password)


        messagebox.showinfo(
            "Contraseña",
            "Contraseña creada correctamente."
        )

        return True


    for intento in range(3):

        password = simpledialog.askstring(
            "Acceso",
            "Introduce la contraseña:",
            show="*"
        )


        if password is None:
            return False


        if comprobar_password(password):

            messagebox.showinfo(
                "Acceso",
                "Acceso permitido."
            )

            return True


        else:

            messagebox.showerror(
                "Error",
                "Contraseña incorrecta."
            )


    messagebox.showerror(
        "Acceso bloqueado",
        "Demasiados intentos."
    )

    return False


if not autenticar_usuario():

    ventana.destroy()

    raise SystemExit


# Mostramos la ventana después
# de iniciar sesión correctamente
ventana.deiconify()


# -----------------------------
# ETIQUETAS
# -----------------------------

label_estado = tk.Label(
    ventana,
    text="Estado: sin carrera",
    font=("Arial", 16)
)

label_estado.pack(
    pady=10
)


label_precio = tk.Label(
    ventana,
    text="Precio: 0.00 €",
    font=("Arial", 20)
)

label_precio.pack(
    pady=10
)


label_mensaje = tk.Label(
    ventana,
    text="",
    font=("Arial", 12)
)

label_mensaje.pack(
    pady=10
)


# -----------------------------
# ACTUALIZAR INTERFAZ
# -----------------------------

def actualizar_interfaz():

    if taximetro.estado is None:

        texto_estado = "sin carrera"

    else:

        texto_estado = taximetro.estado


    label_estado.config(
        text=f"Estado: {texto_estado}"
    )


    label_precio.config(
        text=(
            f"Precio: "
            f"{taximetro.precio_total:.2f} €"
        )
    )


# -----------------------------
# PRECIO EN VIVO
# -----------------------------

def actualizar_precio_en_vivo():

    if taximetro.carrera_activa:

        tiempo_actual = time.time()

        tiempo_actual_estado = (
            tiempo_actual
            - taximetro.inicio_estado
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
            text=(
                f"Precio: "
                f"{precio_mostrado:.2f} €"
            )
        )


    ventana.after(
        500,
        actualizar_precio_en_vivo
    )


# -----------------------------
# FUNCIONES DE LOS BOTONES
# -----------------------------

def iniciar_desde_gui():

    if taximetro.carrera_activa:

        label_mensaje.config(
            text=(
                "Ya hay una carrera activa."
            )
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
            text=(
                "Primero debes iniciar "
                "una carrera."
            )
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
            text=(
                "Primero debes iniciar "
                "una carrera."
            )
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
            text=(
                "No hay ninguna "
                "carrera activa."
            )
        )


    actualizar_interfaz()


def mostrar_historial():

    ventana_historial = tk.Toplevel(ventana)
    ventana_historial.title("Historial de carreras")
    ventana_historial.geometry("650x350")

    texto_historial = tk.Text(
        ventana_historial,
        wrap=tk.WORD
    )

    texto_historial.pack(
        fill=tk.BOTH,
        expand=True,
        padx=10,
        pady=10
    )

    if os.path.exists("historial.txt"):

        with open(
            "historial.txt",
            "r"
        ) as archivo:

            contenido = archivo.read()

        if contenido == "":
            contenido = "No hay carreras guardadas."

    else:
        contenido = "No hay carreras guardadas."

    texto_historial.insert(
        tk.END,
        contenido
    )

    texto_historial.config(
        state=tk.DISABLED
    )


def salir():

    ventana.destroy()


# -----------------------------
# BOTONES
# -----------------------------

boton_start = tk.Button(
    ventana,
    text="Iniciar carrera",
    command=iniciar_desde_gui,
    width=20,
    height=2
)

boton_start.pack(
    pady=5
)


boton_move = tk.Button(
    ventana,
    text="En movimiento",
    command=mover_desde_gui,
    width=20,
    height=2
)

boton_move.pack(
    pady=5
)


boton_stop = tk.Button(
    ventana,
    text="Parado",
    command=parar_desde_gui,
    width=20,
    height=2
)

boton_stop.pack(
    pady=5
)


boton_finish = tk.Button(
    ventana,
    text="Finalizar carrera",
    command=finalizar_desde_gui,
    width=20,
    height=2
)

boton_finish.pack(
    pady=5
)


boton_history = tk.Button(
    ventana,
    text="Historial",
    command=mostrar_historial,
    width=20,
    height=2
)

boton_history.pack(
    pady=5
)


boton_exit = tk.Button(
    ventana,
    text="Salir",
    command=salir,
    width=20,
    height=2
)

boton_exit.pack(
    pady=10
)


# -----------------------------
# INICIAR ACTUALIZACIÓN
# -----------------------------

actualizar_precio_en_vivo()


# -----------------------------
# MANTENER GUI ABIERTA
# -----------------------------

ventana.mainloop()
