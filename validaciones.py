# ==========================================
# MÓDULO: VALIDACIONES
# ==========================================

# Este módulo se encarga de toda la entrada de datos.

# Funciones del módulo:
#   - validar_entero()
#   - validar_texto()
#   - validar_opcion()
#   - validar_nombre()
#   - validar_telefono()

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

def validar_nombre(texto):

    texto = texto.strip()

    if len(texto) == 0:
        return False

    for caracter in texto:

        if not (caracter.isalpha() or caracter == " "):
            return False

    return True

def validar_telefono(telefono):

    return telefono.isdigit() and len(telefono) >= 8