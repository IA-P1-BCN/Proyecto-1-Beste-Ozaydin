TARIFA_PARADO = 0.02
TARIFA_MOVIMIENTO = 0.05

print("=== TAXÍMETRO DIGITAL ===")
print("Comandos disponibles:")
print("start - Iniciar carrera")

comando = input("Escribe un comando: ")

if comando == "start":
    print("Carrera iniciada.")
else:
    print("Comando no válido.")