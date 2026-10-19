# DriveSafe


## Tabla de contenidos


1. Descripción General
2. Módulos del Sistema
3. Estructura de Archivos
4. Almacenamiento de Datos 
5. Validaciones 
6. Requisitos e Instalación
7. Modo de Uso


____________________________________________________________________

# Sistema de Gestión para Escuela de Conducción 

Aplicación de consola desarrollada en Python para la administración de estudiantes, instructores, vehiculos y programación de citas en una escuela de conducción. El proyecto implementa almacenamientp de datos mediante archivos JSON y control de flujo basado en menús interactivos con validación de entradas.

____________________________________________________________________

## Modulos del sistema

* `main.py`: Archivo principal que inicia la ejecución del programa.
* `gestion_menu_principal.py`: Despliega las opciones del menú e interactúa con el usuario.
* `gestion_cliente.py`: Maneja el registro, edición, consulta y eliminación de clientes.
* `gestion_instructor.py`: Controla el registro y asignación de instructores.
* `gestion_vehiculo.py`: Administra la información de los vehículos (placa, modelo, estado).
* `gestion_cita.py`: Coordina el agendamiento y seguimiento de las clases.
* `gestion_json.py`: Agrupa las funciones para cargar, actualizar y guardar los datos.
* `validaciones.py`: Contiene las funciones de comprobación para datos ingresados (texto, numeros, fechas, etc).

____________________________________________________________________

## Estructura de archivos

Proyecto_python
│
├── main.py                        # Punto de entrada principal de la aplicación
│
├── gestion_menu_principal.py      # Interfaz de consola y navegación entre menús
│
├── gestion_cliente.py             # Lógica CRUD para la administración de clientes
├── gestion_instructor.py          # Lógica CRUD para la administración de instructores
├── gestion_vehiculo.py            # Lógica CRUD para la gestión de los vehiculos
├── gestion_cita.py                # Lógica para agendamiento de citas/clases
│
├── gestion_json.py                # Funciones de lectura, carga y guardado en archivos JSON
├── validaciones.py                # Validaciones de entrada (placas, documentos, datos)
│
├── cliente.json                   # Base de datos de clientes
├── instructor.json                # Base de datos de instructores
├── vehiculo.json                  # Base de datos de vehículos
└── cita.json                      # Base de datos de citas

____________________________________________________________________

## Almacenamiento de datos

Los datos se almacenan en la raíz del proyecto dentro de archivos `.json`:

* `cliente.json` — Registro de alumnos inscritos.
* `instructor.json` — Datos del personal docente.
* `vehiculo.json` — Información de los automóviles de la escuela.
* `cita.json` — Registro de clases y citas programadas.

____________________________________________________________________

## Validaciones de Entrada

El módulo `validaciones.py` incluye funciones para verificar que los datos ingresados por el usuario cumplan con los formatos esperados antes de ser registrados en el sistema:

* Validación de documento: Verifica que las cédulas o documentos de identidad de clientes e instructores sean numéricos y no contengan caracteres especiales.
* Validación de Fechas y Horarios: Asegura que las citas y lecciones agendadas respeten un formato válido de fecha/hora que aún no hayan ocurrido.
* Validación de Opciones: Controla que las entradas numéricas en los menús de la consola estén dentro del rango permitido, evitando cierres inesperados por entradas inválidas.


____________________________________________________________________

## Requisitos e Instalación

* "Python 3.10" o posterior.
* No requiere la instalación de librerías de terceros (utiliza módulos nativos de Python).

____________________________________________________________________

## Modo de uso

Una vez iniciado el programa ejecutando `python main.py`, la aplicación desplegará el menú principal en la terminal; Seguido de esto, y dependiendo de la opción seleccionada, se comenzarán a desplegar opciones que dependerán de la categoría. Estas actuarán como un menú, dando la posibilidad de ingresar y regresar al menú anterior, hasta llegar al menú principal o hasta finalizar el programa.