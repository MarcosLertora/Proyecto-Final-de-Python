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
import validaciones
import utilidades


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

def horario_disponible(especialidad, fecha, hora):

    for turno in turnos:

        if (
            turno["especialidad"] == especialidad
            and turno["fecha"] == fecha
            and turno["hora"] == hora
            and turno["estado"] == "Pendiente"
        ):
            return False
    
    return True

def solicitar_turno():

    utilidades.titulo("SOLICITAR TURNO")

    try:

        dni = validaciones.validar_entero("Ingrese DNI del paciente: ")

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

    opcion = validaciones.validar_opcion(
        "Seleccione especialidad (1-4): ",
        ["1", "2", "3", "4"]
    )

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

    while True:

        fecha = input("Ingrese la fecha (dd/mm/aaaa): ").strip()

        partes = fecha.split("/")

        if len(partes) != 3:
            print("Formato incorrecto.")
            continue

        dia, mes, anio = partes

        if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
            print("La fecha debe contener únicamente números.")
            continue

        dia = int(dia)
        mes = int(mes)
        anio = int(anio)

        if dia < 1 or dia > 31:
            print("Día inválido.")
            continue

        if mes < 1 or mes > 12:
            print("Mes inválido.")
            continue

        if anio < 2025:
            print("Año inválido.")
            continue

        break

    while True:

        hora = input("Ingrese horario (Ej: 09:30): ")

        if horario_disponible(especialidad, fecha, hora):
            break

        print("\nEse horario ya se encuentra ocupado para esa especialidad.")

    print("\nPrioridad")

    print("1. Baja")
    print("2. Media")
    print("3. Alta")

    prioridad_opcion = validaciones.validar_opcion(
        "Seleccione prioridad (1-3): ",
        ["1", "2", "3"]
    )

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
        "fecha": fecha,
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

        utilidades.linea()

        print(f"DNI           : {turno['dni']}")
        print(f"Especialidad  : {turno['especialidad']}")
        print(f"Fecha         : {turno['fecha']}")
        print(f"Hora          : {turno['hora']}")
        print(f"Prioridad     : {turno['prioridad']}")
        print(f"Estado        : {turno['estado']}")

        utilidades.linea()


def atender_paciente():

    utilidades.titulo("ATENDER PACIENTE")

    try:

        dni = validaciones.validar_entero("Ingrese DNI del paciente: ")

    except ValueError:

        print("Debe ingresar números.")
        return

    for turno in turnos:

        if turno["dni"] == dni and turno["estado"] == "Pendiente":

            turno["estado"] = "Atendido"

            print("\nPaciente atendido correctamente.")

            return

    print("No existe un turno pendiente para ese paciente.")

def cancelar_turno():

    utilidades.titulo("CANCELAR TURNO")

    try:
        dni = int(input("Ingrese el DNI del paciente: "))

    except ValueError:
        print("Debe ingresar un número.")
        return

    for turno in turnos:

        if turno["dni"] == dni and turno["estado"] == "Pendiente":

            confirmar = input(
                "¿Está seguro que desea cancelar el turno? (S/N): "
            ).upper()

            if confirmar == "S":

                turno["estado"] = "Cancelado"

                print("\nTurno cancelado correctamente.")

            else:

                print("\nOperación cancelada.")

            return

    print("\nNo existe un turno pendiente para ese paciente.")