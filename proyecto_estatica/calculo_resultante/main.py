from utils.menu import dic_menu
from model.punto import Punto
from model.vector import Vector
from model.vectores import Vectores


def solicitar_vectores(n):
    vectores = Vectores()

    for i in range(n):
        op = dic_menu[1.1](i+1)

        v = None

        if op == '1':
            v = Vector.from_magnitud_cosenos(10, 30, 60, 85)
        elif op == '2':
            v = Vector.from_vector_cartesiano(Punto(12, 14, 16))
        elif op == '3':
            print("coming soon...")

        vectores.addVector(v)

    return vectores


def menu_1_2():
    op = 0
    while op != '8':
        op = dic_menu[1.2]()


def menu():

    op = 0
    while op != '2':
        op = dic_menu[1]()
        if op == '1':
            n = int(input("\nNúmero de vectores a trabajar: "))
            vectores = solicitar_vectores(n)
            menu_1_2()
