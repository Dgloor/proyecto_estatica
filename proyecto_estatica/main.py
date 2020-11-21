from clases import Vector, Punto
from menu import print_menu, print_menu_1, print_menu_1_1, print_menu_1_2


def menu_1_1(n):
    l = []

    for i in range(n):
        op = print_menu_1_1(i+1)

        v = None

        if op == '1':
            v = Vector.from_magnitud_cosenos(10, 30, 60, 85)
        elif op == '2':
            v = Vector.from_vector_cartesiano(Punto(12, 14, 16))
        elif op == '3':
            print("coming soon...")
        
        l.append(v)

    return l


def menu_1_2():
    op = 0
    while op != '8':
        op = print_menu_1_2()


def menu_1():
    op = 0
    while op != '2':
        op = print_menu_1()
        if op == '1':
            n = int(input("\nNúmero de vectores a trabajar: "))
            coleccion_vectores = menu_1_1(n)
            print(coleccion_vectores)
            menu_1_2()

def inicio():
    op = 0
    while op != '3':
        op = print_menu()

        if op == '1':
            menu_1()

        elif op == '2':
            pass

        elif op == '3':
            print("\n</> Programa finalizado. </>")


if __name__ == '__main__':
    inicio()

