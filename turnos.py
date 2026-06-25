# MÓDULO: turnos.py
# Este módulo administra los turnos médicos.
#
# - Asignar turnos.
# - Cancelar turnos.
# - Atender pacientes.
# - Mostrar turnos.
# - Buscar turnos.
# - Verificar disponibilidad.
#
# Cada turno tiene:
#   - DNI del paciente.
#   - Especialidad.
#   - Fecha.
#   - Hora.
#   - Prioridad.
#   - Estado (Pendiente, Atendido, Cancelado)
#
# Funciones del módulo:
#   - solicitar_turno()
#   - mostrar_turnos()
#   - atender_paciente()
#   - cancelar_turno()
#   - hay_turnos_disponibles()
#   - buscar_turno_por_dni()
#   - buscar_turno()

# ==========================================
# MÓDULO: TURNOS
# ==========================================

from datos import pacientes, turnos


def paciente_existe(dni):

    for paciente in pacientes:

        if paciente["dni"] == dni:
            return True

    return False


def turno_existente(dni):

    for turno in turnos:

        if turno["dni"] == dni and turno["estado"] == "Pendiente":
            return True

    return False


def solicitar_turno():

    print("\n===== SOLICITAR TURNO =====")

    try:

        dni = int(input("Ingrese DNI del paciente: "))

    except ValueError:

        print("Debe ingresar un número.")
        return

    if not paciente_existe(dni):

        print("Ese paciente no está registrado.")
        return

    if turno_existente(dni):

        print("Ese paciente ya posee un turno pendiente.")
        return

    print("\nEspecialidades")

    print("1. Clínica Médica")
    print("2. Pediatría")
    print("3. Cardiología")
    print("4. Traumatología")

    opcion = input("Seleccione una especialidad: ")

    if opcion == "1":
        especialidad = "Clínica Médica"

    elif opcion == "2":
        especialidad = "Pediatría"

    elif opcion == "3":
        especialidad = "Cardiología"

    elif opcion == "4":
        especialidad = "Traumatología"

    else:

        print("Especialidad inválida.")
        return

    hora = input("Ingrese horario (Ej: 09:30): ")

    print("\nPrioridad")

    print("1. Baja")
    print("2. Media")
    print("3. Alta")

    prioridad_opcion = input("Seleccione prioridad: ")

    if prioridad_opcion == "1":

        prioridad = "Baja"

    elif prioridad_opcion == "2":

        prioridad = "Media"

    elif prioridad_opcion == "3":

        prioridad = "Alta"

    else:

        print("Prioridad inválida.")
        return

    turno = {

        "dni": dni,
        "especialidad": especialidad,
        "hora": hora,
        "prioridad": prioridad,
        "estado": "Pendiente"

    }

    turnos.append(turno)

    print("\nTurno registrado correctamente.")


def mostrar_turnos():

    print("\n===== TURNOS =====")

    if len(turnos) == 0:

        print("No existen turnos registrados.")
        return

    for turno in turnos:

        print("-----------------------------")

        print("DNI:", turno["dni"])

        print("Especialidad:", turno["especialidad"])

        print("Hora:", turno["hora"])

        print("Prioridad:", turno["prioridad"])

        print("Estado:", turno["estado"])


def atender_paciente():

    print("\n===== ATENDER PACIENTE =====")

    try:

        dni = int(input("Ingrese DNI: "))

    except ValueError:

        print("Debe ingresar números.")
        return

    for turno in turnos:

        if turno["dni"] == dni and turno["estado"] == "Pendiente":

            turno["estado"] = "Atendido"

            print("\nPaciente atendido correctamente.")

            return

    print("No existe un turno pendiente para ese paciente.")