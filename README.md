# proyecto\_drivesafe





\## Tabla de contenidos





1\. Descripción General

2\. Módulos del Sistema

3\. Estructura de Archivos

4\. Almacenamiento de Datos 

5\. Validaciones 

6\. Requisitos e Instalación

7\. Modo de Uso





\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\# Sistema de Gestión para Escuela de Conducción 



Aplicación de consola desarrollada en Python para la administración de estudiantes, instructores, vehiculos y programación de citas en una escuela de conducción. El proyecto implementa almacenamientp de datos mediante archivos JSON y control de flujo basado en menús interactivos con validación de entradas.



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\## Modulos del sistema



\* `main.py`: Archivo principal que inicia la ejecución del programa.

\* `gestion\_menu\_principal.py`: Despliega las opciones del menú e interactúa con el usuario.

\* `gestion\_cliente.py`: Maneja el registro, edición, consulta y eliminación de clientes.

\* `gestion\_instructor.py`: Controla el registro y asignación de instructores.

\* `gestion\_vehiculo.py`: Administra la información de los vehículos (placa, modelo, estado).

\* `gestion\_cita.py`: Coordina el agendamiento y seguimiento de las clases.

\* `gestion\_json.py`: Agrupa las funciones para cargar, actualizar y guardar los datos.

\* `validaciones.py`: Contiene las funciones de comprobación para datos ingresados (texto, numeros, fechas, etc).



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\## Estructura de archivos



Proyecto\_python

│

├── main.py                        # Punto de entrada principal de la aplicación

│

├── gestion\_menu\_principal.py      # Interfaz de consola y navegación entre menús

│

├── gestion\_cliente.py             # Lógica CRUD para la administración de clientes

├── gestion\_instructor.py          # Lógica CRUD para la administración de instructores

├── gestion\_vehiculo.py            # Lógica CRUD para la gestión de los vehiculos

├── gestion\_cita.py                # Lógica para agendamiento de citas/clases

│

├── gestion\_json.py                # Funciones de lectura, carga y guardado en archivos JSON

├── validaciones.py                # Validaciones de entrada (placas, documentos, datos)

│

├── cliente.json                   # Base de datos de clientes

├── instructor.json                # Base de datos de instructores

├── vehiculo.json                  # Base de datos de vehículos

└── cita.json                      # Base de datos de citas



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\## Almacenamiento de datos



Los datos se almacenan en la raíz del proyecto dentro de archivos `.json`:



\* `cliente.json` — Registro de alumnos inscritos.

\* `instructor.json` — Datos del personal docente.

\* `vehiculo.json` — Información de los automóviles de la escuela.

\* `cita.json` — Registro de clases y citas programadas.



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\## Validaciones de Entrada



El módulo `validaciones.py` incluye funciones para verificar que los datos ingresados por el usuario cumplan con los formatos esperados antes de ser registrados en el sistema:



\* Validación de documento: Verifica que las cédulas o documentos de identidad de clientes e instructores sean numéricos y no contengan caracteres especiales.

\* Validación de Fechas y Horarios: Asegura que las citas y lecciones agendadas respeten un formato válido de fecha/hora que aún no hayan ocurrido.

\* Validación de Opciones: Controla que las entradas numéricas en los menús de la consola estén dentro del rango permitido, evitando cierres inesperados por entradas inválidas.





\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\## Requisitos e Instalación



\* "Python 3.10" o posterior.

\* No requiere la instalación de librerías de terceros (utiliza módulos nativos de Python).



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\## Modo de uso



Una vez iniciado el programa ejecutando `python main.py`, la aplicación desplegará el menú principal en la terminal; Seguido de esto, y dependiendo de la opción seleccionada, se comenzarán a desplegar opciones que dependerán de la categoría. Estas actuarán como un menú, dando la posibilidad de ingresar y regresar al menú anterior, hasta llegar al menú principal o hasta finalizar el programa.

