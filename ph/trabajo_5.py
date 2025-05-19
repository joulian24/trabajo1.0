# cadena_y_menu.py
# Actividades de manipulación de cadenas y menú interactivo en Python

import re

def conversor_numero_a_palabra(n):
    mapping = {1: 'UNO', 2: 'DOS', 3: 'TRES', 4: 'CUATRO', 5: 'CINCO'}
    return mapping.get(n, None)


def conversor_palabra_a_numero(palabra):
    palabra = palabra.lower()
    mapping = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5}
    return mapping.get(palabra, None)


def registro_usuario():
    """Registra nombre, edad y correo con validación."""
    # Nombre: solo letras
    nombre = input("Ingresa tu nombre: ")
    if not nombre.isalpha():
        print("Nombre inválido. Solo se permiten letras.")
        return
    # Edad: solo dígitos
    edad = input("Ingresa tu edad: ")
    if not edad.isnumeric():
        print("Edad inválida. Solo se permiten números.")
        return
    edad = int(edad)
    # Correo: debe contener @ y .
    correo = input("Ingresa tu correo electrónico: ")
    if correo.find('@') == -1 or correo.find('.') == -1:
        print("Correo inválido. Debe contener '@' y '.'.")
        return
    print(f"Registro exitoso:\n Nombre: {nombre}\n Edad: {edad}\n Correo: {correo}")


def menu_conversor():
    print("=================")
    print("=== Conversor ===")
    print("=================\n")
    print("1) Número a palabra")
    print("2) Palabra a número")
    try:
        opcion = int(input("Selecciona opción: "))
    except ValueError:
        print("Opción inválida. Debes ingresar un número.")
        return
    if opcion == 1:
        try:
            num = int(input("Ingresa número (1-5): "))
        except ValueError:
            print("Debes ingresar un número.")
            return
        palabra = conversor_numero_a_palabra(num)
        if palabra:
            print(f"El número es '{palabra}'")
        else:
            print("Número no registrado.")
    elif opcion == 2:
        palabra = input("Ingresa palabra (uno-cinco): ")
        num = conversor_palabra_a_numero(palabra)
        if num:
            print(f"El número es '{num}'")
        else:
            print("Palabra no registrada.")
    else:
        print("Opción no válida.")


def main_menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1) Conversor número<->palabra")
        print("2) Registro de usuario")
        print("0) Salir")
        choice = input("Selecciona opción: ")
        if choice == '1':
            menu_conversor()
        elif choice == '2':
            registro_usuario()
        elif choice == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main_menu()
