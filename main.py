"""Calculadora Básica"""

import time
import os


def get_integer(
    input_message: str, warning_message: str = "ATENCIÓN: Ingrese un número entero."
) -> int:
    """Solicita un valor entero y lo devuelve.
     Mientras el valor ingresado no sea entero, vuelve first_operand solicitarlo.

    :param str input_message: El mensaje de la entrada.
    :param str warning_message: El mensaje advertencia.
    :return: un número entero"""

    while True:
        valor = input(input_message)
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print(warning_message)


def get_option(
    expect_options: dict,
    input_message: str = "Opción: ",
    warning_message: str = "ATENCIÓN: Ingrese una opción válida.",
) -> int:
    """Solicita una opción de menú y la devuelve.

    :param str input_message: El mensaje de la entrada.
    :param str warning_message: El mensaje advertencia.
    :return: un número entero"""

    while True:
        option = input(input_message)
        if option in expect_options:
            return int(option)

        print(warning_message)
        continue


def menu(options: dict):
    """Muestra el menú de opciones

    :param dict options: Diccionario con las claves-valores de las opciones del menú.
    """

    print("🧮 Seleccione la operación deseada:")

    for key in options.keys():
        print(f"{key}. {options[key]}")


def calculator():
    """Implementación de la calculadora básica."""

    expect_options = {
        "1": "Suma",
        "2": "Resta",
        "3": "Multiplicación",
        "4": "Division",
        "5": "Division entera",
        "6": "Potencia",
        "7": "Salir",
    }

    wait = time.sleep
    os.system("clear")
    exit_program = False

    # Bucle
    while not exit_program:
        # Selección de operaciones
        menu(expect_options)

        option = get_option(expect_options.keys())

        # Apagar calculadora
        if option == 7:
            wait(1)
            exit_program = True

        elif option > 7:
            print("ATENCIÓN: Ingrese una opción válida.")

        # Selección de números
        else:
            first_operand = get_integer("Escriba el primer operando: ")
            second_operand = get_integer("Escriba el segundo operando: ")
            print("El resultado de", end=" ")

            # Suma
            if option == 1:
                print("la suma es: ", first_operand + second_operand)

            # Resta
            elif option == 2:
                print("la resta es: ", first_operand - second_operand)

            # Multiplicación
            elif option == 3:
                print("la multiplicación es: ", first_operand * second_operand)

            # División
            elif option == 4:
                print("la división es: ", first_operand / second_operand)

            # Division entera
            elif option == 5:
                print("la división entera es: ", first_operand // second_operand)

            # Potencia
            elif option == 6:
                print("la potencia es:", first_operand**second_operand)


if __name__ == "__main__":
    calculator()
