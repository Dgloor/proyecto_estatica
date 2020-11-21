from utils.menu import dic_menu
from calculo_resultante.main import menu as resultante_menu
from calculo_momento.main import menu as momento_menu


def init():
    op = 0
    while op != '3':
        op = dic_menu[0]()

        if op == '1':
            resultante_menu()

        elif op == '2':
            momento_menu()

        elif op == '3':
            print("\n</> Programa finalizado. </>")


if __name__ == '__main__':
    init()
