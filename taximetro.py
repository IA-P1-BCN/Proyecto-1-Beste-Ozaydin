TARIFA_PARADO = 0.02
TARIFA_MOVIMIENTO = 0.05

print("=== TAXÍMETRO DIGITAL ===")
print("Comandos disponibles:")
print("1 - Taxi parado")
print("2 - Taxi en movimiento")
print("Introduce los segundos para calcular el precio.")

estado = input("Selecciona el estado: ")

segundos = float(input("¿Cuántos segundos?: "))

if estado == "1":
    precio = segundos * TARIFA_PARADO
elif estado == "2":
    precio = segundos * TARIFA_MOVIMIENTO
else:
    precio = 0

print(f"Precio: {precio:.2f} €")