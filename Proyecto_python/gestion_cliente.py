from validaciones import (
    validar_entero,
    validar_texto,
    validar_documento,
    validar_opcion
)
from gestion_json import cargar, reemplazar, generar_id


NOMBRE_ARCHIVO = "cliente.json"


def buscar_cliente(id_cliente):
    lista_clientes = cargar(NOMBRE_ARCHIVO)

    for cliente in lista_clientes:
        if cliente["id"] == id_cliente:
            return cliente

    return None


def buscar_por_documento(documento):
    lista_clientes = cargar(NOMBRE_ARCHIVO)

    for cliente in lista_clientes:
        if cliente["documento"] == documento:
            return cliente

    return None


def agregar():
    lista_clientes = cargar(NOMBRE_ARCHIVO)

    documento = validar_documento(
        "Ingrese el documento del cliente: "
    )

    if buscar_por_documento(documento) is not None:
        print("Ya existe un cliente con ese documento.")
        return

    cliente = {}

    cliente["id"] = generar_id(lista_clientes)
    cliente["nombre"] = validar_texto(
        "Ingrese el nombre del cliente: "
    )
    cliente["documento"] = documento

    opcion_tipo = validar_opcion(
        """
Seleccione el tipo de vehículo:
1. Moto
2. Carro
Opción: """,
        ["1", "2"]
    )

    if opcion_tipo == "1":
        cliente["tipo_vehiculo"] = "moto"
    else:
        cliente["tipo_vehiculo"] = "carro"

    lista_clientes.append(cliente)
    reemplazar(NOMBRE_ARCHIVO, lista_clientes)

    print("Cliente registrado correctamente.")


def imprimir(cliente):
    print(f"""
        ******************************
        ID:               {cliente.get("id")}
        Nombre:           {cliente.get("nombre")}
        Documento:        {cliente.get("documento")}
        Tipo de vehículo: {cliente.get("tipo_vehiculo")}
    """)


def listar_cliente():
    lista_clientes = cargar(NOMBRE_ARCHIVO)

    if len(lista_clientes) < 1:
        print("No existen clientes registrados.")
        return

    for cliente in lista_clientes:
        imprimir(cliente)


def consultar():
    id_cliente = validar_entero(
        "Ingrese el ID del cliente: "
    )

    cliente = buscar_cliente(id_cliente)

    if cliente is None:
        print("El cliente no existe.")
    else:
        imprimir(cliente)


def menu_cliente():
    while True:
        opcion = validar_entero("""
            BIENVENIDO AL MÓDULO DE CLIENTES

            1. Registrar cliente
            2. Listar clientes
            3. Buscar cliente
            4. Regresar

            Opción: """)

        match opcion:
            case 1:
                agregar()

            case 2:
                listar_cliente()

            case 3:
                consultar()

            case 4:
                break

            case _:
                print("Opción no encontrada.")