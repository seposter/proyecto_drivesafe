from validaciones import (
    validar_entero,
    validar_texto,
    validar_documento,
    validar_opcion
)
from gestion_json import cargar, reemplazar, generar_id


NOMBRE_ARCHIVO = "instructor.json"


def buscar_instructor(id_instructor):
    lista_instructores = cargar(NOMBRE_ARCHIVO)

    for instructor in lista_instructores:
        if instructor["id"] == id_instructor:
            return instructor

    return None


def buscar_por_documento(documento):
    lista_instructores = cargar(NOMBRE_ARCHIVO)

    for instructor in lista_instructores:
        if instructor["documento"] == documento:
            return instructor

    return None


def agregar():
    lista_instructores = cargar(NOMBRE_ARCHIVO)

    documento = validar_documento(
        "Ingrese el documento del instructor: "
    )

    if buscar_por_documento(documento) is not None:
        print("Ya existe un instructor con ese documento.")
        return

    instructor = {}

    instructor["id"] = generar_id(lista_instructores)
    instructor["nombre"] = validar_texto(
        "Ingrese el nombre del instructor: "
    )
    instructor["documento"] = documento

    opcion_especialidad = validar_opcion(
        """
Seleccione la especialidad:
1. Moto
2. Carro
Opción: """,
        ["1", "2"]
    )

    if opcion_especialidad == "1":
        instructor["especialidad"] = "moto"
    else:
        instructor["especialidad"] = "carro"

    instructor["disponible"] = True

    lista_instructores.append(instructor)
    reemplazar(NOMBRE_ARCHIVO, lista_instructores)

    print("Instructor registrado correctamente.")


def imprimir(instructor):
    if instructor.get("disponible"):
        estado = "Disponible"
    else:
        estado = "No disponible"

    print(f"""
        ******************************
        ID:           {instructor.get("id")}
        Nombre:       {instructor.get("nombre")}
        Documento:    {instructor.get("documento")}
        Especialidad: {instructor.get("especialidad")}
        Estado:       {estado}
    """)


def listar_instructor():
    lista_instructores = cargar(NOMBRE_ARCHIVO)

    if len(lista_instructores) < 1:
        print("No existen instructores registrados.")
        return

    for instructor in lista_instructores:
        imprimir(instructor)


def cambiar_disponibilidad(id_instructor):
    lista_instructores = cargar(NOMBRE_ARCHIVO)

    for instructor in lista_instructores:
        if instructor["id"] == id_instructor:
            instructor["disponible"] = not instructor["disponible"]

            reemplazar(
                NOMBRE_ARCHIVO,
                lista_instructores
            )

            print("Disponibilidad actualizada correctamente.")
            return

    print("El instructor no existe.")


def menu_instructor():
    while True:
        opcion = validar_entero("""
            BIENVENIDO AL MÓDULO DE INSTRUCTORES

            1. Registrar instructor
            2. Listar instructores
            3. Cambiar disponibilidad
            4. Regresar

            Opción: """)

        match opcion:
            case 1:
                agregar()

            case 2:
                listar_instructor()

            case 3:
                listar_instructor()

                id_instructor = validar_entero(
                    "Ingrese el ID del instructor: "
                )

                cambiar_disponibilidad(id_instructor)

            case 4:
                break

            case _:
                print("Opción no encontrada.")