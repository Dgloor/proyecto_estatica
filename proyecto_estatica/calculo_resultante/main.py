from calculo_resultante.get_vectores import input_vectores
from utils.menu_builder import menu_builder
# from calculo_resultante.operacioens import *

opciones = menu_builder(2, """
  1. Ingresar n vectores a trabajar
  2. Regresar
""")

opciones_vector = menu_builder(8, """
**OPCIONES**
  1. Vector Resultante
  2. Gráfica del Vector Resultante
  3. Ángulo entre los Vectores y Vector Resultante
  4. Vector Perpendicular al Vector resultante
  5. Gráfica del Vector Perpendicular al Vector Resultante
  6. Proyección de un x Vector sobre el vector Resulante
  7. Gráfica de la Proyección de un x Vector sobre el Vector Resultante
  8. Salir
""")


def menu_vectores(vectores):
    op = 0
    while op != '8':
        op = opciones_vector()
        if op == '1':
            pass
        elif op == '2':
            pass
        elif op == '3':
            pass
        elif op == '4':
            pass
        elif op == '5':
            pass
        elif op == '6':
            pass
        elif op == '7':
            pass


def menu():
    op = 0
    while op != '2':
        op = opciones()
        if op == '1':
            vectores = input_vectores()
            menu_vectores(vectores)
