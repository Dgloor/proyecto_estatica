from utils.menu_builder import menu_builder
from model.punto import Punto
from model.vector import Vector
from model.vectores import Vectores

menu0 = menu_builder(2, """
  1. Ingresar n vectores a trabajar
  2. Regresar
""")

menu2 = menu_builder(8, """
OPCIONES
  1. Vector Resultante
  2. Gráfica del Vector Resultante
  3. Ángulo entre los Vectores y Vector Resultante
  4. Vector Perpendicular al Vector resultante
  5. Gráfica del Vector Perpendicual al Vector Resultante
  6. Proyección de un x Vector sobre el vector Resulante
  7. Gráfica de la Proyección de un x Vector sobre el Vector Resultante
  8. Salir
""")


def menu1(n):
    print("""
** Formas de Ingresar un Vector **
  1. Magnitud y cosenos directores
  2. Vector Cartesiano
  3. Magnitud y dirección a partir de 2 puntos
""")
    op_validas = ['1', '2', '3']
    op = 0

    while op not in op_validas:
        op = input(f"Forma Vector {n}: ")
        if op not in op_validas:
            print("\n<x> Error, opción inválida. <x>\n")

    return op


def solicitar_vectores(n):
    vectores = Vectores()

    for i in range(n):
        op = menu1(i + 1)

        v = None

        if op == '1':
            v = Vector.from_magnitud_cosenos(10, 30, 60, 85)
        elif op == '2':
            v = Vector.from_vector_cartesiano(Punto(12, 14, 16))
        elif op == '3':
            print("coming soon...")

        vectores.add_vector(v)

    return vectores
