import json
import os

archivo = "/home/camper/Documentos/Ejercicios Python - Deyvid/Gestor de inventario para una Biblioteca/data/libros.json"

def cargar_libros():
    "carga los libros desde  el archivo json"
    if not os.path.exists(archivo):
        return []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return[]



#funcion para registrar un libro
def registrar_libro():
    print("====== Registrar un nuevo libro ======")
    titulo = input("Ingrese el título del libro: ").lower()
    autor = input("Ingrese el autor del libro: ").lower()
    genero = input("Ingrese el género del libro: ").lower()
    try:
        anio = int(input("Ingrese el año de publicación: "))
    except ValueError:
        print("Error: El año debe ser un número. Se asignará 0 por defecto.")
        anio = 0

    #creacion del diccionario
    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "anio": anio,
        "estado": True,
        "prestado": False
    }
    lista_libros = []
    
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            try:
                lista_libros = json.load(f)
            except json.JSONDecodeError:
                lista_libros = [] #si el archivo esta vacio
    
    lista_libros.append(libro)
    
    #se guarda la lista actualizada
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(lista_libros, f, indent=4, ensure_ascii=False)

    print(f"\n¡Libro '{titulo}' guardado exitosamente!")
    return libro




#funcion para ver el inventario
def ver_inventario():
    
    if not os.path.exists(archivo):
        print("No hay libros registrados en el inventario.")
        return
    
    with open(archivo, 'r', encoding='utf-8') as f:
        try:
            libros = json.load(f)
        except json.JSONDecodeError:
            print("No hay libros registrados en el inventario.")
            return
        
    print("  =" * 10)
    print("    Inventario de los Libros")
    print("  =" * 10)
    
    print("\n|        Titulo        |   Autor   |   Año   |   Estado   |")
    print("-" * 60)

    for libro in libros:
        titulo = libro.get("titulo", "N/A")
        autor = libro.get("autor", "N/A")
        anio = libro.get("anio", 0)     
        genero = libro.get("genero", "N/A")
        estado = "Disponible" if not libro.get("prestado") else "Prestado"
        print(" -" * 35)
        print(f"| {titulo:<10} | {autor:<5} | {anio:<5} | {estado} | {genero} |")
        print(" -" * 35)