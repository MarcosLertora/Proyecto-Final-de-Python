# ==========================================
# MÓDULO: PACIENTES.PY
# ==========================================

# Este módulo administra toda la información relacionada con los pacientes.
# - Registrar pacientes.
# - Buscar pacientes.
# - Modificar datos de un paciente.
# - Mostrar uno o todos los pacientes.
# - Verificar si un DNI ya existe.

# Funciones del módulo:
#   - registrar_paciente()
#   - buscar_paciente()
#   - mostrar_pacientes()
#   - existe_dni()

# Cada paciente tiene:
#   - DNI
#   - Nombre
#   - Apellido
#   - Edad
#   - Teléfono
#   - Obra social

from datos import pacientes
import validaciones
import utilidades

def existe_dni(dni):
    
    """
    Verifica si un DNI ya está registrado.
    Devuelve True si existe, False en caso contrario.

    """
    for paciente in pacientes:
        if paciente["dni"] == dni:
            return True

    return False


def registrar_paciente():

    utilidades.titulo("REGISTRAR PACIENTE")

    # -----------------------------
    # DNI
    # -----------------------------

    while True:

        try:
            dni = validaciones.validar_entero("DNI: ")

            if dni <= 0:
                print("El DNI debe ser mayor que cero.")
                continue

            if existe_dni(dni):
                print("Ese DNI ya está registrado.")
                return

            break

        except ValueError:
            print("Debe ingresar únicamente números.")

    # -----------------------------
    # Nombre
    # -----------------------------

    while True:

        nombre = input("Nombre: ").strip()

        if validaciones.validar_nombre(nombre):
            break

        print("El nombre solo puede contener letras y espacios.")

    # -----------------------------
    # Apellido
    # -----------------------------

    while True:
        
        apellido = input("Apellido: ").strip()

        if validaciones.validar_nombre(apellido):
            break

        print("El apellido solo puede contener letras y espacios.")

    # -----------------------------
    # Edad
    # -----------------------------

    while True:

        try:

            edad = validaciones.validar_entero("Edad: ")

            if edad <= 0 or edad > 120:
                print("Edad inválida.")
                continue

            break

        except ValueError:
            print("Debe ingresar un número.")

    # -----------------------------
    # Teléfono
    # -----------------------------

    while True:

        telefono = input("Teléfono: ").strip()

        if validaciones.validar_telefono(telefono):
            break

        print("Ingrese un teléfono válido.")

    # -----------------------------
    # Obra Social
    # -----------------------------

    while True:

        obra_social = input("Obra Social: ").strip()

        if validaciones.validar_obra_social(obra_social):
            break

        print("La obra social solo puede contener letras y espacios.")

    # -----------------------------
    # Crear paciente
    # -----------------------------

    paciente = {

        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "telefono": telefono,
        "obra_social": obra_social

    }

    pacientes.append(paciente)

    print(f"Paciente {nombre} {apellido} registrado correctamente.")


def mostrar_pacientes():

    print("\n===== PACIENTES REGISTRADOS =====")

    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
        return

    for paciente in sorted(pacientes, key=lambda paciente: paciente["nombre"]):

        utilidades.linea()

        print(f"DNI         : {paciente['dni']}")
        print(f"Nombre      : {paciente['nombre']}")
        print(f"Apellido      : {paciente['apellido']}")
        print(f"Edad        : {paciente['edad']}")
        print(f"Teléfono    : {paciente['telefono']}")
        print(f"Obra Social : {paciente['obra_social']}")

        utilidades.linea()

def buscar_paciente():

    print("\n===== BUSCAR PACIENTE =====")

    try:
        dni = int(input("Ingrese el DNI del paciente: "))
    except ValueError:
        print("Debe ingresar un número.")
        return

    for paciente in pacientes:

        if paciente["dni"] == dni:

            print("\nPaciente encontrado")
            print("-" * 30)
            print("DNI: ", paciente["dni"])
            print(f"Nombre : {paciente['nombre']}")
            print(f"Apellido : {paciente['apellido']}")            
            print("Edad :", paciente["edad"])
            print("Teléfono :", paciente["telefono"])
            print("Obra Social :", paciente["obra_social"])

            return

    print("\nNo existe un paciente con ese DNI.")