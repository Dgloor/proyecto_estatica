from utils.menu_builder import menu_builder
from calculo_resultante.main import menu as resultante_menu
from calculo_momento.main import menu as momento_menu


menu = menu_builder(3, """
== PROYECTO DE ESTATICA ==\n
Bienvenido al sistema de calculo de fuerzas resultantes y momentos.\n
  1. Cálculo de Fuerza Resultante
  2. Cálculo de Momento respecto a un Eje
  3. Salir
""")

dic_opciones = {'1': resultante_menu,
                '2': momento_menu,
                '3': lambda: print("\n</> Programa finalizado. </>")}


def init():
    op = 0
    while op != '3':
        op = menu()
        dic_opciones.get(op)()


if __name__ == '__main__':
    init()
