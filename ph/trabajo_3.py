# Captura del nombre del usuario
nombre = input("¡Hola! Por favor ingresa tu nombre: ")
print(f"\n{nombre}, este programa te mostrará diferentes tipos de datos en Python.\n")

# Entero
entero = int(input("1. INGRESA un NÚMERO ENTERO (ej: 8): "))
print(f"Valor: {entero} - Tipo: {type(entero)}\n")

# Flotante
flotante = float(input("2. INGRESA un NÚMERO DECIMAL (ej: 7,8): "))
print(f"Valor: {flotante} - Tipo: {type(flotante)}\n")

# Complejo
print("3. NÚMERO COMPLEJO")
real = float(input("  Parte real (ej: 5): "))
imag = float(input("  Parte imaginaria (ej: 3): "))
complejo = complex(real, imag)
print(f"Valor: {complejo} - Tipo: {type(complejo)}\n")

# Cadena
cadena = input("4. INGRESA un TEXTO : ")
print(f"Valor: '{cadena}' - Tipo: {type(cadena)}\n")

# Booleano
print("5. COMPARACIÓN BOOLEANA")
num1 = float(input("  Ingresa el primer número para comparar: "))
num2 = float(input("  Ingresa el segundo número para comparar: "))
resultado = num1 == num2
print(f"¿Son iguales? {resultado} - Tipo: {type(resultado)}")

print("\n¡Has completado todos los tipos de datos!")