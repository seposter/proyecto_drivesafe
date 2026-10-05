from datetime import datetime, timedelta

from validaciones import (
    validar_entero,
    validar_fecha,
    validar_hora,
    validar_si_no,
    validar_texto_opcional
)
from gestion_json import cargar, reemplazar, generar_id
from gestion_cliente import (
    buscar_cliente,
    listar_cliente
)
from gestion_instructor import (
    buscar_instructor,
    listar_instructor
)
from gestion_vehiculo import (
    buscar_vehiculo,
    listar_vehiculo
)


NOMBRE_ARCHIVO = "cita.json"


def buscar_cita(id_cita):
    lista_citas = cargar(NOMBRE_ARCHIVO)

    for cita in lista_citas:
        if cita["id"] == id_cita:
            return cita

    return None


def obtener_intervalo(fecha, hora, duracion):
    fecha_hora = datetime.strptime(
        f"{fecha} {hora}",
        "%Y-%m-%d %H:%M"
    )

    fecha_hora_final = fecha_hora + timedelta(
        minutes=duracion
    )

    return fecha_hora, fecha_hora_final


def existe_conflicto(
    lista_citas,
    campo,
    id_elemento,
    fecha,
    hora,
    duracion
):
    nuevo_inicio, nuevo_final = obtener_intervalo(
        fecha,
        hora,
        duracion
    )

    for cita in lista_citas:
        if cita[campo] == id_elemento:
            inicio_existente, final_existente = obtener_intervalo(
                cita["fecha"],
                cita["hora"],
                cita["duracion"]
            )

            if (
                nuevo_inicio < final_existente
                and inicio_existente < nuevo_final
            ):
                return True

    return False


def agregar():
    lista_citas = cargar(NOMBRE_ARCHIVO)

    lista_clientes = cargar("cliente.json")
    lista_instructores = cargar("instructor.json")
    lista_vehiculos = cargar("vehiculo.json")

    if len(lista_clientes) < 1:
        print("Debe registrar al menos un cliente.")
        return

    if len(lista_instructores) < 1:
        print("Debe registrar al menos un instructor.")
        return

    if len(lista_vehiculos) < 1:
        print("Debe registrar al menos un vehículo.")
        return

    listar_cliente()

    id_cliente = validar_entero(
        "Ingrese el ID del cliente: "
    )

    cliente = buscar_cliente(id_cliente)

    if cliente is None:
        print("El cliente no existe.")
        return

    listar_instructor()

    id_instructor = validar_entero(
        "Ingrese el ID del instructor: "
    )

    instructor = buscar_instructor(id_instructor)

    if instructor is None:
        print("El instructor no existe.")
        return

    if instructor["disponible"] is False:
        print("El instructor está marcado como no disponible.")
        return

    if instructor["especialidad"] != cliente["tipo_vehiculo"]:
        print(
            "La especialidad del instructor no coincide "
            "con el tipo de vehículo del cliente."
        )
        return

    listar_vehiculo()

    id_vehiculo = validar_entero(
        "Ingrese el ID del vehículo: "
    )

    vehiculo = buscar_vehiculo(id_vehiculo)

    if vehiculo is None:
        print("El vehículo no existe.")
        return

    if vehiculo["disponible"] is False:
        print("El vehículo está marcado como no disponible.")
        return

    if vehiculo["tipo"] != cliente["tipo_vehiculo"]:
        print(
            "El tipo del vehículo no coincide "
            "con el solicitado por el cliente."
        )
        return

    fecha = validar_fecha(
        "Ingrese la fecha de la cita (AAAA-MM-DD): "
    )

    hora = validar_hora(
        "Ingrese la hora de la cita (HH:MM): "
    )

    duracion = validar_entero(
        "Ingrese la duración en minutos: ",
        minimo=30
    )

    inicio_cita, _ = obtener_intervalo(
        fecha,
        hora,
        duracion
    )

    if inicio_cita <= datetime.now():
        print("La cita debe programarse para una fecha futura.")
        return

    if existe_conflicto(
        lista_citas,
        "id_cliente",
        id_cliente,
        fecha,
        hora,
        duracion
    ):
        print("El cliente ya tiene una cita en ese horario.")
        return

    if existe_conflicto(
        lista_citas,
        "id_instructor",
        id_instructor,
        fecha,
        hora,
        duracion
    ):
        print("El instructor ya tiene una cita en ese horario.")
        return

    if existe_conflicto(
        lista_citas,
        "id_vehiculo",
        id_vehiculo,
        fecha,
        hora,
        duracion
    ):
        print("El vehículo ya está reservado en ese horario.")
        return

    cita = {}

    cita["id"] = generar_id(lista_citas)
    cita["id_cliente"] = id_cliente
    cita["id_instructor"] = id_instructor
    cita["id_vehiculo"] = id_vehiculo
    cita["fecha"] = fecha
    cita["hora"] = hora
    cita["duracion"] = duracion
    cita["asistencia"] = None
    cita["observaciones"] = ""
    cita["estado"] = "programada"

    lista_citas.append(cita)
    reemplazar(NOMBRE_ARCHIVO, lista_citas)

    print("Cita programada correctamente.")


def imprimir(cita):
    cliente = buscar_cliente(cita["id_cliente"])
    instructor = buscar_instructor(cita["id_instructor"])
    vehiculo = buscar_vehiculo(cita["id_vehiculo"])

    if cliente is None:
        nombre_cliente = "Cliente no encontrado"
    else:
        nombre_cliente = cliente["nombre"]

    if instructor is None:
        nombre_instructor = "Instructor no encontrado"
    else:
        nombre_instructor = instructor["nombre"]

    if vehiculo is None:
        placa_vehiculo = "Vehículo no encontrado"
    else:
        placa_vehiculo = vehiculo["placa"]

    if cita["asistencia"] is None:
        asistencia = "Pendiente"
    elif cita["asistencia"] is True:
        asistencia = "Sí asistió"
    else:
        asistencia = "No asistió"

    print(f"""
        *************************************
        ID de cita:   {cita.get("id")}
        Cliente:      {nombre_cliente}
        Instructor:   {nombre_instructor}
        Vehículo:     {placa_vehiculo}
        Fecha:        {cita.get("fecha")}
        Hora:         {cita.get("hora")}
        Duración:     {cita.get("duracion")} minutos
        Estado:       {cita.get("estado")}
        Asistencia:   {asistencia}
        Observaciones:{cita.get("observaciones")}
    """)


def listar():
    lista_citas = cargar(NOMBRE_ARCHIVO)

    if len(lista_citas) < 1:
        print("No existen citas registradas.")
        return

    for cita in lista_citas:
        imprimir(cita)


def buscar_por_cliente(id_cliente):
    lista_citas = cargar(NOMBRE_ARCHIVO)
    lista_resultado = []

    for cita in lista_citas:
        if cita["id_cliente"] == id_cliente:
            lista_resultado.append(cita)

    return lista_resultado


def consultar_por_cliente():
    listar_cliente()

    id_cliente = validar_entero(
        "Ingrese el ID del cliente: "
    )

    cliente = buscar_cliente(id_cliente)

    if cliente is None:
        print("El cliente no existe.")
        return

    lista_resultado = buscar_por_cliente(id_cliente)

    if len(lista_resultado) < 1:
        print("El cliente no tiene citas registradas.")
        return

    for cita in lista_resultado:
        imprimir(cita)


def buscar_por_fecha(fecha):
    lista_citas = cargar(NOMBRE_ARCHIVO)
    lista_resultado = []

    for cita in lista_citas:
        if cita["fecha"] == fecha:
            lista_resultado.append(cita)

    return lista_resultado


def consultar_por_fecha():
    fecha = validar_fecha(
        "Ingrese la fecha (AAAA-MM-DD): ",
        permitir_pasado=True
    )

    lista_resultado = buscar_por_fecha(fecha)

    if len(lista_resultado) < 1:
        print("No existen citas para esa fecha.")
        return

    for cita in lista_resultado:
        imprimir(cita)


def registrar_asistencia():
    lista_citas = cargar(NOMBRE_ARCHIVO)

    if len(lista_citas) < 1:
        print("No existen citas registradas.")
        return

    listar()

    id_cita = validar_entero(
        "Ingrese el ID de la cita: "
    )

    for cita in lista_citas:
        if cita["id"] == id_cita:
            if cita["estado"] != "programada":
                print(
                    "La asistencia de esta cita ya fue registrada."
                )
                return

            asistencia = validar_si_no(
                "¿El cliente asistió? (S/N): "
            )

            observaciones = validar_texto_opcional(
                "Ingrese las observaciones: "
            )

            cita["asistencia"] = asistencia
            cita["observaciones"] = observaciones

            if asistencia:
                cita["estado"] = "realizada"
            else:
                cita["estado"] = "inasistencia"

            reemplazar(NOMBRE_ARCHIVO, lista_citas)

            print("Asistencia registrada correctamente.")
            return

    print("La cita no existe.")


def historial_cliente():
    listar_cliente()

    id_cliente = validar_entero(
        "Ingrese el ID del cliente: "
    )

    cliente = buscar_cliente(id_cliente)

    if cliente is None:
        print("El cliente no existe.")
        return

    lista_citas = buscar_por_cliente(id_cliente)
    historial = []

    for cita in lista_citas:
        if cita["estado"] in ["realizada", "inasistencia"]:
            historial.append(cita)

    if len(historial) < 1:
        print("El cliente no tiene prácticas realizadas.")
        return

    print(f"""
        HISTORIAL DE PRÁCTICAS
        Cliente: {cliente["nombre"]}
        Documento: {cliente["documento"]}
    """)

    for cita in historial:
        imprimir(cita)


def menu_cita():
    while True:
        opcion = validar_entero("""
            BIENVENIDO AL MÓDULO DE CITAS

            1. Programar cita
            2. Listar todas las citas
            3. Consultar citas por cliente
            4. Consultar citas por fecha
            5. Registrar asistencia y observaciones
            6. Consultar historial de un cliente
            7. Regresar

            Opción: """)

        match opcion:
            case 1:
                agregar()

            case 2:
                listar()

            case 3:
                consultar_por_cliente()

            case 4:
                consultar_por_fecha()

            case 5:
                registrar_asistencia()

            case 6:
                historial_cliente()

            case 7:
                break

            case _:
                print("Opción no encontrada.")