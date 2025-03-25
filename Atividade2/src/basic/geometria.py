import math

def calcular_area_quadrado(lado):
    if lado < 0:
        return None
    return lado * lado

def calcular_area_circulo(raio):
    if raio < 0:
        return None
    return math.pi * raio * raio

def calcular_area_triangulo_equilatero(base, altura):
    if base < 0 or altura < 0 :
        return None
    return base * altura / 2 

def calcular_area_losango(D, d):
    if D < 0 or d < 0:
        return None
    return D * d / 2

def calcular_area_pentagono_regular_lado(lado):
    if lado < 0:
        return None
    area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * lado ** 2
    return area