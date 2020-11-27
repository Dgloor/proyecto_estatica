from utils.menu_builder import menu_v_builder
from model.punto import Punto
from model.vector import Vector


def get_vector_a():
    magnitud:float = float(input("Ingrese magnitud: "))
    cos2: int = int(input("Ingrese coseno director 2: "))
    cos3: int = int(input("Ingrese coseno director 3: "))
    cos1: int = int(input("Ingrese coseno director 1: "))
    return None


def get_vector_b():
    print("coming soon...")
    return None


def get_vector_c():
    magnitud: float = float(input("Ingrese magnitud: "))
    return None


def input_vectores():
    n = int(input("\nNúmero de vectores a trabajar: "))

    vectores = []

    for i in range(n):
        menu1 = menu_v_builder(3, """
** Formas de Ingresar un Vector **
  1. Magnitud y cosenos directores
  2. Vector Cartesiano
  3. Magnitud y dirección a partir de 2 puntos
""", i+1)

        op = menu1()

        if op == '1':
            v = get_vector_a()
        elif op == '2':
            v = get_vector_b()
        elif op == '3':
            v = get_vector_c()

        vectores.append(v)

    return vectores
