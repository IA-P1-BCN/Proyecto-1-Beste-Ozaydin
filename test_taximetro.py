from src.taximetro import calcular_precio


def test_precio_parado():
    resultado = calcular_precio(10, 0.02)
    assert resultado == 0.20


def test_precio_movimiento():
    resultado = calcular_precio(10, 0.05)
    assert resultado == 0.50
