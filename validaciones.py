# MÓDULO: validaciones.py
# Este módulo se encarga de toda la entrada de datos.
# Funciones del módulo:
#   - validar_dni()
#   - validar_nombre()
#   - validar_edad()
#   - validar_telefono()
#   - validar_opcion_menu()
#   - validar_especialidad()


# ==========================================
# MÓDULO: VALIDACIONES
# ==========================================


def validar_entero(mensaje):

    while True:

        try:
            valor = int(input(mensaje))

            if valor <= 0:
                print("Debe ser un número mayor a 0.")
                continue

            return valor

        except ValueError:
            print("Error: debe ingresar un número entero.")


def validar_texto(mensaje):

    while True:

        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el campo no puede estar vacío.")
            continue

        if texto.isdigit():
            print("Error: no puede contener solo números.")
            continue

        return texto


def validar_opcion(mensaje, opciones):

    while True:

        opcion = input(mensaje)

        if opcion in opciones:
            return opcion

        print("Opción inválida. Intente nuevamente.")