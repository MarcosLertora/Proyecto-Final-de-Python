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
    pass

def validar_nombre():
    pass

def validar_edad():

    while True:

        edad = input("Edad: ")

        if edad.isdigit():
            
            edad = int(edad)

            if edad > 0 and edad < 120:
                return edad
        
        print("Edad inválida.")

def validar_telefono():
    pass

def validar_opcion_menu():
    pass

def validar_especialidad():
    pass