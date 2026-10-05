from validaciones import validar_entero
from gestion_cliente import menu_cliente
from gestion_instructor import menu_instructor
from gestion_vehiculo import menu_vehiculo
from gestion_cita import menu_cita


def menu():
    while True:
        opcion_general = validar_entero("""
            BIENVENIDO A LA ACADEMIA DRIVESAFE

            1. Gestionar clientes
            2. Gestionar instructores
            3. Gestionar vehículos
            4. Gestionar citas y prácticas
            5. Salir

            Opción: """)

        match opcion_general:
            case 1:
                menu_cliente()

            case 2:
                menu_instructor()

            case 3:
                menu_vehiculo()

            case 4:
                menu_cita()

            case 5:
                print("Gracias por utilizar DriveSafe.")
                break

            case _:
                print("Opción no encontrada.")