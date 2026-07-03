# MÓDULO: utilidades.py
# En este módulo se encuentran funciones reutilizables.
# Funciones del módulo:
#   - limpiar_pantalla()
#   - pausa()
#   - mostrar_titulo()
#   - buscar_por_dni()
#   - confirmar()

import os


def limpiar_pantalla():

    os.system("cls" if os.name == "nt" else "clear")


def linea():

    print("=" * 50)


def titulo(texto):

    linea()
    print(texto.center(50))
    linea()


def pausa():

    input("\nPresione ENTER para continuar...")