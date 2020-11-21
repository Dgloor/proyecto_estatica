
opciones = """
== PROYECTO DE ESTATICA ==\n
Bienvenido al sistema de calculo de fuerzas resultantes y momentos.\n
  1. Cálculo de Fuerza Resultante
  2. Cálculo de Momento respecto a un Eje
  3. Salir
"""

opciones_1 = """
  1. Ingresar n vectores a trabajar
  2. Regresar
"""

opciones_1_1 = """
** Formas de Ingresar un Vector **
  1. Magnitud y cosenos directores
  2. Vector Cartesiano
  3. Magnitud y dirección a partir de 2 puntos
"""

opciones_1_2 = """
OPCIONES
  1. Vector Resultante
  2. Gráfica del Vector Resultante
  3. Ángulo entre los Vectores y Vector Resultante
  4. Vector Perpendicular al Vector resultante
  5. Gráfica del Vector Perpendicual al Vector Resultante
  6. Proyección de un x Vector sobre el vector Resulante
  7. Gráfica de la Proyección de un x Vector sobre el Vector Resultante
  8. Salir
"""


def print_menu():
    print(opciones)
    opValidas = ['1', '2', '3']
    op = 0

    while op not in opValidas:
        op = input("Ingrese una opción: ")
        if op not in opValidas:
            print("\n<x> Error, opción inválida. <x>\n")

    return op


def print_menu_1():
    print(opciones_1)
    opValidas = ['1', '2']
    op = 0

    while op not in opValidas:
        op = input("Ingrese una opción: ")
        if op not in opValidas:
            print("\n<x> Error, opción inválida. <x>\n")

    return op


def print_menu_1_1(n):
    print(opciones_1_1)
    opValidas = ['1', '2', '3']
    op = 0

    while op not in opValidas:
        op = input(f"Ingrese una opción (Vector {n}): ")
        if op not in opValidas:
            print("\n<x> Error, opción inválida. <x>\n")

    return op


def print_menu_1_2():
    print(opciones_1_2)
    opValidas = ['1', '2', '3', '4', '5', '6', '7', '8']
    op = 0

    while op not in opValidas:
        op = input(f"Ingrese una opción: ")
        if op not in opValidas:
            print("\n<x> Error, opción inválida. <x>\n")

    return op
