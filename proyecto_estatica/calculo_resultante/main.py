from calculo_resultante.inputs import *


def menu_1_2():
    op = 0
    while op != '8':
        op = menu2()


def menu():
    op = 0
    while op != '2':
        op = menu0()
        if op == '1':
            n = int(input("\nNúmero de vectores a trabajar: "))
            vectores = solicitar_vectores(n)
            menu_1_2()
