
def menu_builder(n_opciones, text):
    def menu():
        print(text)
        opValidas = [str(i+1) for i in range(n_opciones)]
        op = 0

        while op not in opValidas:
            op = input(f"Ingrese una opción: ")
            if op not in opValidas:
                print("\n<x> Error, opción inválida. <x>\n")

        return op

    return menu


def menu_1_1(n):
    print("""
** Formas de Ingresar un Vector **
  1. Magnitud y cosenos directores
  2. Vector Cartesiano
  3. Magnitud y dirección a partir de 2 puntos
""")
    opValidas = ['1', '2', '3']
    op = 0

    while op not in opValidas:
        op = input(f"Forma Vector {n}: ")
        if op not in opValidas:
            print("\n<x> Error, opción inválida. <x>\n")

    return op


menu_0 = menu_builder(3, """
== PROYECTO DE ESTATICA ==\n
Bienvenido al sistema de calculo de fuerzas resultantes y momentos.\n
  1. Cálculo de Fuerza Resultante
  2. Cálculo de Momento respecto a un Eje
  3. Salir
""")

menu_1 = menu_builder(2, """
  1. Ingresar n vectores a trabajar
  2. Regresar
""")

menu_1_2 = menu_builder(8, """
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

dic_menu = {0: menu_0, 1: menu_1, 1.1: menu_1_1, 1.2: menu_1_2}
