# Proyecto Taxímetro

Proyecto realizado como parte de la formación de Factoría F5.

## Objetivo

Crear un taxímetro digital básico en Python que permita gestionar una carrera desde la terminal y calcular el precio según el tiempo que el taxi está parado o en movimiento.

## Tarifas

- Taxi parado: 0.02 €/segundo
- Taxi en movimiento: 0.05 €/segundo

## Funcionalidades actuales

- Iniciar una carrera
- Cambiar el estado a movimiento
- Cambiar el estado a parado
- Calcular el precio acumulado
- Finalizar la carrera y mostrar el total
- Iniciar una nueva carrera sin cerrar el programa
- Evitar iniciar una segunda carrera mientras otra está activa
- Salir del programa

## Comandos

- `start` - Iniciar una carrera
- `move` - Taxi en movimiento
- `stop` - Taxi parado
- `finish` - Finalizar la carrera
- `exit` - Cerrar el programa

## Cómo ejecutar el programa

Desde la terminal:

```bash
python3 taximetro.py