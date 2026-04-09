import json
from gestion_libros import *
from buscar_libros import *
from prestamos import *
from reportes import *




while True:
    print("=" * 50)
    print("GESTOR DE INVENTARIO PARA UNA BIBLIOTECA VIRTUAL")
    print("=" * 50)
    print("1. Registrar un nuevo libro")
    print("2. Ver el inventario de libros")
    print("3. Buscar un libro")
    print("4. Prestar un libro")
    print("5. Devolver un libro")
    print("6. Generar un reporte del inventario")
    print("7. Salir")
    print("=" * 50)

    opcion = input("\nSeleccione una opción: ")

    match opcion:
        case '1':
                registrar_libro()
        case '2':
                ver_inventario()
        case '3':
                buscar_libro()
        case '4':
                prestar_libro()
        case '5':
                devolver_libro()
        case '6':
                generar_reporte()
        case '7':
                print("Saliendo del programa...")
                break
        case _:
                print("Opción no válida. Intente de nuevo.")

