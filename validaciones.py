# MÓDULO: validaciones.py
# Este módulo se encarga de toda la entrada de datos.
# Funciones del módulo:
#   - validar_dni()
#   - validar_nombre()
#   - validar_edad()
#   - validar_telefono()
#   - validar_opcion_menu()
#   - validar_especialidad()

def validar_dni():
    print("Se llamó a validar_dni.")

def validar_nombre():
    print("Se llamó a validar_nombre.")

def validar_edad():

    while True:

        edad = input("Edad: ")

        if edad.isdigit():
            
            edad = int(edad)

            if edad > 0 and edad < 120:
                return edad
        
        print("Edad inválida.")

def validar_telefono():
    print("Se llamó a validar_telefono.")

def validar_opcion_menu():
    print("Se llamó a validar_opcion_menu.")

def validar_especialidad():
    print("Se llamó a validar_especialidad.")