# ==========================================
# MÓDULO: MAIN.PY
# ==========================================

# Este módulo contiene el menú principal.

# Funciones del módulo:
#   - limpiar_pantalla()
#   - mostrar_menu()
#   - main()

import os

import pacientes
import turnos
import estadisticas
import utilidades

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():

    print("=" * 50)
    print("      SISTEMA DE TURNOS HOSPITALARIOS")
    print("=" * 50)
    print("1. Registrar paciente")
    print("2. Buscar paciente")
    print("3. Solicitar turno")
    print("4. Atender paciente")
    print("5. Cancelar turno")
    print("6. Mostrar pacientes")
    print("7. Mostrar turnos")
    print("8. Estadísticas")
    print("9. Salir")
    print("=" * 50)


def main():

    while True:

        utilidades.limpiar_pantalla()

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pacientes.registrar_paciente()

        elif opcion == "2":
            pacientes.buscar_paciente()

        elif opcion == "3":
            turnos.solicitar_turno()

        elif opcion == "4":
            turnos.atender_paciente()

        elif opcion == "5":
            turnos.cancelar_turno()

        elif opcion == "6":
            pacientes.mostrar_pacientes()

        elif opcion == "7":
            turnos.mostrar_turnos()

        elif opcion == "8":
            estadisticas.mostrar_estadisticas()

        elif opcion == "9":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción inválida.")

        utilidades.pausa()


if __name__ == "__main__":
    main()