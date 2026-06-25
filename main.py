# MÓDULO: main.py
# Este módulo contiene el menú.

while True:

    mostrar_menu()

    opcion = validar_opcion()

    if opcion == 1:
        registrar_paciente()

    elif opcion == 2:
        solicitar_turno()

    elif opcion == 3:
        atender_paciente()

    elif opcion == 4:
        mostrar_pacientes()

    elif opcion == 5:
        mostrar_turnos()

    elif opcion == 6:
        mostrar_estadisticas()

    elif opcion == 7:
        break