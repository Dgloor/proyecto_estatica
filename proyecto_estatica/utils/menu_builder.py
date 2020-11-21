def menu_builder(n_opciones, text):
    def menu():
        print(text)
        op_validas = [str(i + 1) for i in range(n_opciones)]
        op = 0

        while op not in op_validas:
            op = input(f"Ingrese una opción: ")
            if op not in op_validas:
                print("\n<x> Error, opción inválida. <x>\n")

        return op

    return menu


menu = menu_builder(3, """
== PROYECTO DE ESTATICA ==\n
Bienvenido al sistema de calculo de fuerzas resultantes y momentos.\n
  1. Cálculo de Fuerza Resultante
  2. Cálculo de Momento respecto a un Eje
  3. Salir
""")
