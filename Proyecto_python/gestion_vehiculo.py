from validaciones import (
    validar_entero,
    validar_texto,
    validar_opcion
)
from gestion_json import cargar, reemplazar, generar_id


NOMBRE_ARCHIVO = "vehiculo.json"


def buscar_vehiculo(id_vehiculo):
    lista_vehiculos = cargar(NOMBRE_ARCHIVO)

    for vehiculo in lista_vehiculos:
        if vehiculo["id"] == id_vehiculo:
            return vehiculo

    return None


def buscar_por_placa(placa):
    lista_vehiculos = cargar(NOMBRE_ARCHIVO)

    for vehiculo in lista_vehiculos:
        if vehiculo["placa"].upper() == placa.upper():
            return vehiculo

    return None


def agregar():
    lista_vehiculos = cargar(NOMBRE_ARCHIVO)

    placa = validar_texto(
        "Ingrese la placa del vehículo: "
    ).upper()

    if buscar_por_placa(placa) is not None:
        print("Ya existe un vehículo con esa placa.")
        return

    vehiculo = {}

    vehiculo["id"] = generar_id(lista_vehiculos)
    vehiculo["placa"] = placa

    opcion_tipo = validar_opcion(
        """
Seleccione el tipo de vehículo:
1. Moto
2. Carro
Opción: """,
        ["1", "2"]
    )

    if opcion_tipo == "1":
        vehiculo["tipo"] = "moto"
    else:
        vehiculo["tipo"] = "carro"

    vehiculo["disponible"] = True

    lista_vehiculos.append(vehiculo)
    reemplazar(NOMBRE_ARCHIVO, lista_vehiculos)

    print("Vehículo registrado correctamente.")


def imprimir(vehiculo):
    if vehiculo.get("disponible"):
        estado = "Disponible"
    else:
        estado = "No disponible"

    print(f"""
        ******************************
        ID:         {vehiculo.get("id")}
        Placa:      {vehiculo.get("placa")}
        Tipo:       {vehiculo.get("tipo")}
        Estado:     {estado}
    """)


def listar_vehiculo():
    lista_vehiculos = cargar(NOMBRE_ARCHIVO)

    if len(lista_vehiculos) < 1:
        print("No existen vehículos registrados.")
        return

    for vehiculo in lista_vehiculos:
        imprimir(vehiculo)


def cambiar_disponibilidad(id_vehiculo):
    lista_vehiculos = cargar(NOMBRE_ARCHIVO)

    for vehiculo in lista_vehiculos:
        if vehiculo["id"] == id_vehiculo:
            vehiculo["disponible"] = not vehiculo["disponible"]

            reemplazar(
                NOMBRE_ARCHIVO,
                lista_vehiculos
            )

            print("Disponibilidad actualizada correctamente.")
            return

    print("El vehículo no existe.")


def menu_vehiculo():
    while True:
        opcion = validar_entero("""
            BIENVENIDO AL MÓDULO DE VEHÍCULOS

            1. Registrar vehículo
            2. Listar vehículos
            3. Cambiar disponibilidad
            4. Regresar

            Opción: """)

        match opcion:
            case 1:
                agregar()

            case 2:
                listar_vehiculo()

            case 3:
                listar_vehiculo()

                id_vehiculo = validar_entero(
                    "Ingrese el ID del vehículo: "
                )

                cambiar_disponibilidad(id_vehiculo)

            case 4:
                break

            case _:
                print("Opción no encontrada.")