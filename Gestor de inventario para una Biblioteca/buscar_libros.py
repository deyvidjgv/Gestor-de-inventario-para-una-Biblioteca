from gestion_libros import *

def buscar_libro():
    lista = cargar_libros()
    if not lista:
        print("No hay libros registrados en el inventario.")
        return
    
    filtro = input("Ingrese un criterio de busqueda (titulo, autor o genero): ").lower()
    buscar = [libro for libro in lista 
            if filtro in libro["titulo"].lower() or 
            filtro in libro["autor"].lower() or 
            filtro in str(libro["anio"]) or
            filtro in libro["genero"].lower()
            ]
    if not buscar:
        print("no se encontraron libros con ese criterio")
        return
    
    #con este for se muestra el titulo del libro
    for libro in buscar:
        print(f"- {libro['titulo']}")
        
    print(f"Se encontraron {len(buscar)} libro con el criterio '{filtro}': ")
