def division_segura():
    """Ejercicio: División segura"""
    try:
        a = float(input("1) División segura - Ingresa el dividendo: "))
        b = float(input("   Ingresa el divisor: "))
    except ValueError:
        print("Entrada inválida. Debes ingresar números.")
        return
    if b != 0:
        print(f"Resultado: {a / b}\n")
    else:
        print("No se puede dividir entre cero.\n")


def promedio_estudiante():
    """Ejercicio: Cálculo de promedio de un estudiante"""
    nombre = input("2) Promedio - Ingresa el nombre del estudiante: ")
    notas = []
    for i in range(1, 6):
        try:
            nota = float(input(f"   Ingresa la nota de la materia {i}: "))
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")
            return
        notas.append(nota)
    promedio = sum(notas) / len(notas)
    if promedio >= 3.0:
        print(f"¡Felicidades {nombre}! Tu promedio es {promedio:.2f}\n")
    else:
        print(f"{nombre}, tu promedio es {promedio:.2f}. Sigue esforzándote.\n")


def conversion_temperaturas():
    """Ejercicio: Conversión de temperaturas"""
    try:
        c = float(input("3) Conversión - Ingresa temperatura en Celsius: "))
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")
        return
    f = (c * 9/5) + 32
    k = c + 273.15
    print(f"{c:.2f} °C equivale a {f:.2f} °F y {k:.2f} K.\n")


def area_figura():
    """Ejercicio: Cálculo de área de figuras geométricas"""
    opcion = input("4) Área - Elige figura (círculo/cuadrado/rectángulo): ").lower()
    if opcion in ['círculo', 'circulo']:
        try:
            r = float(input("   Ingresa el radio del círculo: "))
            area = 3.1416 * r**2
        except ValueError:
            print("Entrada inválida.")
            return
    elif opcion == 'cuadrado':
        try:
            l = float(input("   Ingresa el lado del cuadrado: "))
            area = l**2
        except ValueError:
            print("Entrada inválida.")
            return
    elif opcion in ['rectángulo', 'rectangulo']:
        try:
            largo = float(input("   Ingresa el largo: "))
            ancho = float(input("   Ingresa el ancho: "))
            area = largo * ancho
        except ValueError:
            print("Entrada inválida.")
            return
    else:
        print("Opción no válida.\n")
        return
    print(f"El área del {opcion} es {area:.2f}\n")


def conversor_numero():
    """Ejercicio: Conversor de número a texto"""
    try:
        n = int(input("5) Conversor número - Ingresa un número entre 1 y 5: "))
    except ValueError:
        print("Entrada inválida. Debes ingresar un entero.\n")
        return
    mapping = {1: 'UNO', 2: 'DOS', 3: 'TRES', 4: 'CUATRO', 5: 'CINCO'}
    texto = mapping.get(n, None)
    if texto:
        print(f"El número es '{texto}'\n")
    else:
        print("El número seleccionado no está registrado.\n")


def main():
    """Menú principal para elegir ejercicio"""
    opciones = {
        '1': division_segura,
        '2': promedio_estudiante,
        '3': conversion_temperaturas,
        '4': area_figura,
        '5': conversor_numero
    }
    while True:
        print("Selecciona un ejercicio:")
        print(" 1) División segura")
        print(" 2) Promedio de estudiante")
        print(" 3) Conversión de temperaturas")
        print(" 4) Área de figura geométrica")
        print(" 5) Conversor de número a texto")
        print(" 0) Salir")
        elec = input("Tu elección: ")
        if elec == '0':
            print("¡Hasta luego!")
            break
        ejercicio = opciones.get(elec)
        if ejercicio:
            ejercicio()
        else:
            print("Opción inválida, intenta nuevamente.\n")


if __name__ == "__main__":
    main()
