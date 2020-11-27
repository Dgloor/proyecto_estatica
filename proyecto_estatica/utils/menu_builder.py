def menu_builder(n_opciones: int, text: str):
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


def menu_v_builder(n_opciones: int, text: str, j):
    def menu():
        print(text)
        op_validas = [str(i + 1) for i in range(n_opciones)]
        op = 0

        while op not in op_validas:
            op = input(f'Ingrese forma del vector {j}: ')
            if op not in op_validas:
                print('\n<x> Error, opción inválida. <x>\n')

        return op

    return menu
