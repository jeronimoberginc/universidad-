# -*- coding: utf-8 -*-
"""
===============================================================================
📄 II Examen Parcial
🎯 Propósito: Gestión de estudiantes 
📚 Contenido: Registro, modificación, eliminación, listado y estadísticas
===============================================================================
👤 Autor: [jeronimo berginc natanael]
📅 Fecha Parcial: 14-06-2025
📘 Asignatura: Introducción a la Programación
👨‍🏫 Profesor: Víctor Hugo Contreras
===============================================================================
🧱 Estructura del estudiante:
    - Nombre (str)
    - Apellido (str)
    - DNI (str)
    - Nota (int): -1 si no está asignada
    - Condición (str): "ausente", "aprobado", "reprobado"

📌 Funcionalidades:
Helper. `dni_duplicado(dni)`:
   - Verifica si un DNI ya está registrado en la lista de estudiantes.
   - Devuelve `True` si el DNI está duplicado, de lo contrario, `False`.

Helper. `buscar_por_dni(dni)`:
   - Busca un estudiante en la lista por su DNI.
   - Devuelve el índice del estudiante si lo encuentra, o `-1` si no existe.

1. `agregar_estudiante()`:
   - Permite agregar un nuevo estudiante a la lista.
   - Solicita nombre, apellido y DNI.
   - Valida que el nombre, apellido y DNI no estén vacíos.
   - Valida que el DNI sea numérico y no esté duplicado.
   - Inicializa la nota como `-1` (sin asignar) y la condición como "ausente".


2. `modificar_nota()`:
   - Permite asignar o modificar la nota de un estudiante.
   - Valida que la nota esté entre 0 y 10.
   - Actualiza la condición del estudiante según la nota:
     - `0`: "ausente".
     - `6 o más`: "aprobado".
     - Menor a `6`: "reprobado".

3. `eliminar_estudiante()`:
   - Elimina un estudiante de la lista si no tiene una nota asignada.
   - Valida que el estudiante exista y que su nota sea `-1`.

4. `listar_estudiantes()`:
   - Muestra la lista completa de estudiantes con su nombre, apellido, DNI, nota y condición.
   - Indica si no hay estudiantes registrados.

5. `mostrar_estadisticas()`:
   - Calcula y muestra estadísticas de los estudiantes:
     - Cantidad de aprobados.
     - Cantidad de reprobados.
     - Cantidad de ausentes.
===============================================================================
"""
DNI_REP=True
DNI_NO_ENCONTRADO=False
NOMBRE=0
APELLDIO=1
DNI=2
NOTA=3
ESTADO=4

estudiantes = []

# ------------------ Funciones Auxiliares ------------------
def dni_duplicado(dni):
    for estudiante in estudiantes:
        if estudiante[2] == dni:
            return DNI_REP
    return DNI_NO_ENCONTRADO

def buscar_por_dni(dni):
    for i in range(len(estudiantes)):
        if estudiantes[i][DNI] == dni:
            return i
    return DNI_NO_ENCONTRADO

def condicion_estudiante(nota):
    if nota <= 0:
        return "ausente"
    elif nota < 5:
        return "reprobado"
    else:
        return "aprobado"


# ------------------ Funciones Principales ------------------

def agregar_estudiante():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    while True:
        apellido = input("Ingrese el apellido del estudiante: ").strip()
        if apellido:
            break
        print("El apellido no puede estar vacío.")

    while True:
        dni_input = input("Ingrese el DNI del estudiante: ").strip()
        if dni_input.isdigit():
            dni = int(dni_input)
            if dni_duplicado(dni):
                print("Ya existe un estudiante con ese DNI.")
            else:
                break
        else:
            print("El DNI debe ser un número.")

    while True:
        try:
            nota = int(input("Ingrese la nota del estudiante (0-10): ").strip())
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("La nota debe ser un número entero.")

    estado = condicion_estudiante(nota)
    estudiantes.append([nombre, apellido, dni, nota, estado])
    print("Estudiante agregado correctamente.")
def modificar_nota():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    dni_input = input("Ingrese el DNI del estudiante cuya nota desea modificar: ").strip()
    if not dni_input.isdigit():
        print("El DNI debe ser un número.")
        return

    dni = int(dni_input)
    for estudiante in estudiantes:
        if estudiante[2] == dni:
            while True:
                try:
                    nueva_nota = int(input("Ingrese la nueva nota (0-10): ").strip())
                    if 0 <= nueva_nota <= 10:
                        estudiante[3] = nueva_nota
                        estudiante[4] = condicion_estudiante(nueva_nota)
                        print("Nota modificada correctamente.")
                        return
                    else:
                        print("La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("La nota debe ser un número entero.")
            return
    print("No se encontró un estudiante con ese DNI.")
def eliminar_estudiante():
    if not estudiantes:
        print("No hay estudiantes para eliminar.")
        return

    dni_input = input("Ingrese el DNI del estudiante a eliminar: ").strip()
    if not dni_input.isdigit():
        print("El DNI debe ser un número.")
        return
    dni = int(dni_input)
    for i, estudiante in enumerate(estudiantes):
        if estudiante[2] == dni:
            eliminado = estudiantes.pop(i)
            print(f"Estudiante {eliminado[0]} {eliminado[1]} eliminado correctamente.")
            return
    print("No se encontró un estudiante con ese DNI.")
def listar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes.\n")
        return

    print("\n Lista de estudiantes")
    print("*" * 100)
    for i in estudiantes:
        print(f"# nombre: {i[NOMBRE]} / apellido: {i[APELLDIO]} / dni: {i[DNI]} / nota: {i[NOTA]:.2f} / estado: {i[ESTADO]}")
    print("*" * 100 + "\n")

def mostrar_estadisticas():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    ausentes = 0
    aprobados = 0
    reprobados = 0

    for est in estudiantes:
        estado = condicion_estudiante(NOTA)
        if estado == "ausente":
            ausentes += 1
        elif estado == "aprobado":
            aprobados += 1
        elif estado == "reprobado":
            reprobados += 1

    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")
    print(f"Ausentes: {ausentes}")
def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar estudiante")
        print("2. Modificar nota")
        print("3. Eliminar estudiante")
        print("4. Listar estudiantes")
        print("5. Mostrar estadísticas")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            modificar_nota()
        elif opcion == "3":
            eliminar_estudiante()
        elif opcion == "4":
            listar_estudiantes()
        elif opcion == "5":
            mostrar_estadisticas()
        elif opcion == "6":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":    
    menu()