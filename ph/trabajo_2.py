# Captura del nombre del usuario
nombre = input("¡Hola! Por favor ingresa tu nombre: ")
print(f"\nBienvenido(a) {nombre}, este programa realiza operaciones aritméticas básicas.\n")

# Función para validar entrada numérica
def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un número válido.")

# Suma
print("1. SUMA (+)")
n1 = obtener_numero("Ingresa el primer número: ")
n2 = obtener_numero("Ingresa el segundo número: ")
print(f"{nombre}, el resultado de la suma es: {n1 + n2}\n")

# Resta
print("2. RESTA (-)")
n1 = obtener_numero("Ingresa el minuendo: ")
n2 = obtener_numero("Ingresa el sustraendo: ")
print(f"{nombre}, el resultado de la resta es: {n1 - n2}\n")

# Multiplicación
print("3. MULTIPLICACIÓN (*)")
n1 = obtener_numero("Ingresa el primer factor: ")
n2 = obtener_numero("Ingresa el segundo factor: ")
print(f"{nombre}, el resultado de la multiplicación es: {n1 * n2}\n")

# Exponente
print("4. EXPONENTE (**)")
base = obtener_numero("Ingresa la base: ")
exp = obtener_numero("Ingresa el exponente: ")
print(f"{nombre}, el resultado de la potencia es: {base ** exp}\n")

# Cuadrado
print("5. CUADRADO (**2)")
numero = obtener_numero("Ingresa un número para elevarlo al cuadrado: ")
print(f"{nombre}, el resultado del cuadrado es: {numero ** 2}\n")

# División con validación
print("6. DIVISIÓN (/)")
while True:
    try:
        dividendo = obtener_numero("Ingresa el dividendo: ")
        divisor = obtener_numero("Ingresa el divisor: ")
        print(f"{nombre}, el resultado de la división es: {dividendo / divisor}")
        break
    except ZeroDivisionError:
        print("¡Error! No se puede dividir por cero. Intenta nuevamente.\n")
print()

# Módulo
print("7. MÓDULO (%)")
while True:
    try:
        n1 = obtener_numero("Ingresa el primer número: ")
        n2 = obtener_numero("Ingresa el segundo número: ")
        print(f"{nombre}, el módulo de la división es: {n1 % n2}")
        break
    except ZeroDivisionError:
        print("¡Error! No se puede calcular módulo con cero. Intenta nuevamente.\n")
print()

# División entera
print("8. DIVISIÓN ENTERA (//)")
while True:
    try:
        n1 = obtener_numero("Ingresa el dividendo: ")
        n2 = obtener_numero("Ingresa el divisor: ")
        print(f"{nombre}, el resultado de la división entera es: {n1 // n2}")
        break
    except ZeroDivisionError:
        print("¡Error! No se puede dividir por cero. Intenta nuevamente.\n")

print("\n¡Gracias por usar el programa!")