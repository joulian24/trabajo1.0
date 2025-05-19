import math
import sys

# --- MÓDULO CALCULADORA ---
def calculadora():
    while True:
        print("\n--- Calculadora ---")
        print("1) Suma")
        print("2) Resta")
        print("3) Multiplicación")
        print("4) División")
        print("5) Potencia")
        print("6) Raíz n-ésima")
        print("0) Volver al menú principal")
        op = input("Selecciona opción: ")
        if op == '0':
            break
        try:
            a = float(input("Ingresa primer número: "))
            b = float(input("Ingresa segundo número (o índice de raíz): "))
        except ValueError:
            print("Entrada inválida. Debes ingresar números.")
            continue
        if op == '1': print(f"Resultado: {a + b}")
        elif op == '2': print(f"Resultado: {a - b}")
        elif op == '3': print(f"Resultado: {a * b}")
        elif op == '4':
            if b != 0: print(f"Resultado: {a / b}")
            else: print("Error: división por cero.")
        elif op == '5': print(f"Resultado: {a ** b}")
        elif op == '6':
            if b != 0:
                root = a ** (1 / b)
                print(f"Resultado: {root}")
            else:
                print("Error: índice de raíz no puede ser cero.")
        else:
            print("Opción inválida.")

# --- MÓDULO CONTACTOS (memoria) ---
contactos = []  # lista de dicts: {'nombre','telefono','email'}

def gestion_contactos():
    while True:
        print("\n--- Gestión de Contactos ---")
        print("1) Añadir contacto")
        print("2) Mostrar contactos")
        print("3) Eliminar contacto")
        print("0) Volver al menú principal")
        op = input("Selecciona opción: ")
        if op == '0':
            break
        if op == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            contactos.append({'nombre': nombre, 'telefono': telefono, 'email': email})
            print("Contacto añadido.")
        elif op == '2':
            if not contactos:
                print("No hay contactos.")
            else:
                for i, c in enumerate(contactos, 1):
                    print(f"{i}) {c['nombre']} - {c['telefono']} - {c['email']}")
        elif op == '3':
            gestion_contactos()  # recursion safe?
            idx = input("Número de contacto a eliminar: ")
            if idx.isdigit() and 1 <= int(idx) <= len(contactos):
                removed = contactos.pop(int(idx)-1)
                print(f"Eliminado: {removed['nombre']}")
            else:
                print("Índice inválido.")
        else:
            print("Opción inválida.")

# --- MÓDULO INVENTARIO ---
inventario = {}  # clave: producto, valor: cantidad

def gestion_inventario():
    while True:
        print("\n--- Sistema de Inventario ---")
        print("1) Añadir producto")
        print("2) Actualizar stock")
        print("3) Mostrar inventario")
        print("4) Eliminar producto")
        print("0) Volver al menú principal")
        op = input("Selecciona opción: ")
        if op == '0': break
        if op == '1':
            prod = input("Nombre producto: ")
            qty = input("Cantidad inicial: ")
            if qty.isdigit(): inventario[prod] = int(qty); print("Producto añadido.")
            else: print("Cantidad inválida.")
        elif op == '2':
            prod = input("Producto a actualizar: ")
            if prod in inventario:
                qty = input("Nueva cantidad: ")
                if qty.isdigit(): inventario[prod] = int(qty); print("Stock actualizado.")
                else: print("Cantidad inválida.")
            else: print("Producto no existe.")
        elif op == '3':
            if not inventario: print("Inventario vacío.")
            else:
                for prod, qty in inventario.items(): print(f"{prod}: {qty}")
        elif op == '4':
            prod = input("Producto a eliminar: ")
            if prod in inventario: del inventario[prod]; print("Producto eliminado.")
            else: print("Producto no existe.")
        else: print("Opción inválida.")

# --- MÓDULO TAREAS ---
tareas = []  # lista de dicts: {'tarea','completada'}

def gestion_tareas():
    while True:
        print("\n--- Gestión de Tareas ---")
        print("1) Añadir tarea")
        print("2) Marcar completada")
        print("3) Mostrar pendientes")
        print("4) Mostrar completadas")
        print("0) Volver al menú principal")
        op = input("Selecciona opción: ")
        if op == '0': break
        if op == '1':
            desc = input("Descripción de la tarea: ")
            tareas.append({'tarea': desc, 'completada': False}); print("Tarea añadida.")
        elif op == '2':
            for i, t in enumerate(tareas,1): print(f"{i}) {t['tarea']} - {'✓' if t['completada'] else ' '}")
            idx = input("Número de tarea a marcar: ")
            if idx.isdigit() and 1 <= int(idx) <= len(tareas):
                tareas[int(idx)-1]['completada'] = True; print("Marcada.")
            else: print("Índice inválido.")
        elif op == '3':
            for t in tareas:
                if not t['completada']: print(f"- {t['tarea']}")
        elif op == '4':
            for t in tareas:
                if t['completada']: print(f"- {t['tarea']}")
        else: print("Opción inválida.")

# --- MÓDULO DIARIO/NOTAS ---
notas = []  # lista de dicts: {'fecha','texto'}

def gestion_diario():
    while True:
        print("\n--- Diario Personal ---")
        print("1) Añadir nota")
        print("2) Mostrar notas")
        print("3) Eliminar nota")
        print("0) Volver al menú principal")
        op = input("Selecciona opción: ")
        if op == '0': break
        if op == '1':
            fecha = input("Fecha (YYYY-MM-DD): ")
            texto = input("Texto de la nota: ")
            notas.append({'fecha': fecha, 'texto': texto}); print("Nota añadida.")
        elif op == '2':
            for n in notas: print(f"[{n['fecha']}] {n['texto']}")
        elif op == '3':
            for i, n in enumerate(notas,1): print(f"{i}) [{n['fecha']}] {n['texto']}")
            idx = input("Número de nota a eliminar: ")
            if idx.isdigit() and 1 <= int(idx) <= len(notas):
                notas.pop(int(idx)-1); print("Nota eliminada.")
            else: print("Índice inválido.")
        else: print("Opción inválida.")

# --- MENÚ PRINCIPAL ---
def main():
    while True:
        print("\n=== Aplicación General ===")
        print("1) Calculadora")
        print("2) Gestión de Contactos")
        print("3) Sistema de Inventario")
        print("4) Gestión de Tareas")
        print("5) Diario Personal")
        print("0) Salir")
        opc = input("Selecciona módulo: ")
        if opc == '0':
            print("¡Gracias por usar la aplicación!")
            sys.exit()
        elif opc == '1': calculadora()
        elif opc == '2': gestion_contactos()
        elif opc == '3': gestion_inventario()
        elif opc == '4': gestion_tareas()
        elif opc == '5': gestion_diario()
        else: print("Opción inválida.")

if __name__ == "__main__":
    main()
