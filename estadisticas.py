# ==========================================
# MÓDULO: ESTADÍSTICAS
# ==========================================

from datos import pacientes, turnos
import utilidades

# La función mostrar_estadisticas() calcula y muestra información estadística de los turnos registrados.

def mostrar_estadisticas():

    utilidades.titulo("ESTADÍSTICAS")

    print(f"Pacientes registrados: {cantidad_pacientes()}")
    print(f"Turnos registrados: {cantidad_turnos()}")
    print(f"Turnos atendidos: {cantidad_atendidos()}")
    print(f"Turnos pendientes: {cantidad_pendientes()}")
    print(f"Turnos cancelados: {cantidad_cancelados()}")
    print(f"Porcentaje de turnos atendidos: {porcentaje_atendidos():.2f}%")
    print(f"\nEspecialidad más solicitada: {especialidad_mas_solicitada()}")
    print(f"Prioridad más frecuente: {prioridad_mas_frecuente()}")
    mostrar_turnos_por_prioridad()
    


def cantidad_pacientes():
    return len(pacientes)


def cantidad_turnos():
    return len(turnos)


def cantidad_atendidos():

    contador = 0

    for turno in turnos:

        if turno["estado"] == "Atendido":
            contador += 1

    return contador


def cantidad_pendientes():

    contador = 0

    for turno in turnos:

        if turno["estado"] == "Pendiente":
            contador += 1

    return contador


def cantidad_cancelados():

    contador = 0

    for turno in turnos:

        if turno["estado"] == "Cancelado":
            contador += 1

    return contador


def prioridad_mas_frecuente():

    prioridades = {
        "Baja": 0,
        "Media": 0,
        "Alta": 0
    }

    for turno in turnos:

        prioridades[turno["prioridad"]] += 1

    if len(turnos) == 0:
        return "Sin datos"

    return max(prioridades, key=prioridades.get)


def especialidad_mas_solicitada():

    especialidades = {}

    for turno in turnos:

        nombre = turno["especialidad"]

        if nombre in especialidades:
            especialidades[nombre] += 1
        else:
            especialidades[nombre] = 1

    if len(especialidades) == 0:
        return "Sin datos"

    return max(especialidades, key=especialidades.get)

def porcentaje_atendidos():

    if len(turnos) == 0:
        return 0

    return (cantidad_atendidos() / len(turnos)) * 100

def mostrar_turnos_por_prioridad():

    baja = 0
    media = 0
    alta = 0

    for turno in turnos:

        if turno["prioridad"] == "Baja":
            baja += 1

        elif turno["prioridad"] == "Media":
            media += 1

        elif turno["prioridad"] == "Alta":
            alta += 1

    print("\nTurnos por prioridad")
    print(f"Baja : {baja}")
    print(f"Media: {media}")
    print(f"Alta : {alta}")