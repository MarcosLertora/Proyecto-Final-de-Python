# MÓDULO: pacientes.py
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
#   - buscar_paciente_por_dni()
#   - modificar_paciente()
#   - eliminar_paciente()
# Cada paciente tiene:
#   - DNI
#   - Nombre
#   - Apellido
#   - Edad
#   - Teléfono
#   - Obra social
#
# ==========================================
# MÓDULO: pacientes.py
# ==========================================

# Lista donde se almacenarán todos los pacientes

from datos import pacientes
import validaciones

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

    print("\n===== REGISTRO DE PACIENTE =====")

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

        nombre = validaciones.validar_texto("Nombre: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue

        break
    # -----------------------------
    # Apellido 
    # -----------------------------
    
    while True: 
        apellido = validaciones.validar_texto("Apellido: ").strip()

        if apellido == "":
            print("El apellido no puede estar vacío.")
            continue
        break
        
    # -----------------------------
    # Edad
    # -----------------------------

    while True:

        try:

            edad = int(input("Edad: "))

            if edad <= 0 or edad > 120:
                print("Edad inválida.")
                continue

            break

        except ValueError:
            print("Debe ingresar un número.")

    # -----------------------------
    # Teléfono
    # -----------------------------

    telefono = input("Teléfono: ")

    # -----------------------------
    # Obra Social
    # -----------------------------

    obra_social = input("Obra Social: ")

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

    print("\nPaciente registrado correctamente.")


def mostrar_pacientes():

    print("\n===== PACIENTES REGISTRADOS =====")

    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
        return

    for paciente in pacientes:

        print("----------------------------")
        print("DNI:", paciente["dni"])
        print("Nombre:", paciente["nombre"])
        print("Apellido:", paciente["apellido"]) 
        print("Edad:", paciente["edad"])
        print("Teléfono:", paciente["telefono"])
        print("Obra Social:", paciente["obra_social"])
