import os
import json


RUTA_PROYECTO = os.path.dirname(os.path.abspath(__file__))


def obtener_ruta(nombre_archivo):
    return os.path.join(RUTA_PROYECTO, nombre_archivo)


def cargar(nombre_archivo):
    ruta = obtener_ruta(nombre_archivo)

    try:
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        else:
            return []

    except json.JSONDecodeError:
        print(f"El archivo {nombre_archivo} contiene un JSON inválido.")
        return []


def reemplazar(nombre_archivo, lista_datos):
    ruta = obtener_ruta(nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(
            lista_datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )


def generar_id(lista):
    if not lista:
        return 1

    return max(elemento.get("id", 0) for elemento in lista) + 1