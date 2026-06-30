# MÓDULO: main.py
# Este módulo contiene el menú.

import os

import pacientes
import turnos
import estadisticas

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():

    print("=" * 50)
    print("      SISTEMA DE TURNOS HOSPITALARIOS")
    print("=" * 50)
    print("1. Registrar paciente")
    print("2. Solicitar turno")
    print("3. Atender paciente")
    print("4. Mostrar pacientes")
    print("5. Mostrar turnos")
    print("6. Estadísticas")
    print("7. Salir")
    print("=" * 50)


def main():

    while True:

        limpiar_pantalla()

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pacientes.registrar_paciente()

        elif opcion == "2":
            turnos.solicitar_turno()

        elif opcion == "3":
            turnos.atender_paciente()

        elif opcion == "4":
            pacientes.mostrar_pacientes()

        elif opcion == "5":
            turnos.mostrar_turnos()

        elif opcion == "6":
            estadisticas.mostrar_estadisticas()

        elif opcion == "7":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción inválida.")

        input("\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()