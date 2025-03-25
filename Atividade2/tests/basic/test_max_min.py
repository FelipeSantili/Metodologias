# import src.basic.geometria as geo # type: ignore
# import pytest
# import math
# from src.password.generate import encrypt_password

# data = [
#     (3, geo.math.pi * 3 * 3),
#     (-3, None),
#     (0, 0),
#     (1, pytest.approx(math.pi)),
# ]

# def test_calcular_area_quadrado():
#     assert geo.calcular_area_quadrado(4) == 16
#     assert geo.calcular_area_quadrado(-4) is None
#     assert geo.calcular_area_quadrado(0) == 0

# def test_calcular_area_circulo():
#     assert geo.calcular_area_circulo(3) == geo.math.pi * 3 * 3
#     assert geo.calcular_area_circulo(-3) is None
#     assert geo.calcular_area_circulo(0) == 0
#     assert geo.calcular_area_circulo(1) == pytest.approx(math.pi)

# def test_calcular_area_triangulo_equilatero():
#     assert geo.calcular_area_triangulo_equilatero(4, 6) == 12
#     assert geo.calcular_area_triangulo_equilatero(-4, 6) is None
#     assert geo.calcular_area_triangulo_equilatero(4, -6) is None
#     assert geo.calcular_area_triangulo_equilatero(0, 6) == 0
#     assert geo.calcular_area_triangulo_equilatero(4, 0) == 0

# def test_calcular_area_losango():
#     assert geo.calcular_area_losango(6, 8) == 24
#     assert geo.calcular_area_losango(-6, 8) is None
#     assert geo.calcular_area_losango(6, -8) is None
#     assert geo.calcular_area_losango(0, 8) == 0
#     assert geo.calcular_area_losango(6, 0) == 0

# def test_calcular_area_pentagono_regular_lado():
#     lado = 5
#     assert geo.calcular_area_pentagono_regular_lado(lado) == (1/4) * geo.math.sqrt(5 * (5 + 2 * geo.math.sqrt(5))) * lado ** 2
#     assert geo.calcular_area_pentagono_regular_lado(-5) is None
#     assert geo.calcular_area_pentagono_regular_lado(0) == 0 


# @pytest.mark.parametrize("val1, val2", data)
# def test_generate_list(self, val1, val2):
#     res = geo.calcular_area_circulo(val1, val2)
#     assert res == data