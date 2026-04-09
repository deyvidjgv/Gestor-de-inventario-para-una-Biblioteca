from gestion_libros import *
from buscar_libros import * 

def prestar_libro():
    lista = cargar_libros()
    
    if not lista:
        print("No hay libros disponibles")
        return

    nombre = input("Ingrese su nombre: ")
    titulo = input("Qué libro quieres llevar: ").lower()

    for libro in lista:
        if libro["titulo"].lower() == titulo:

            if libro["prestado"]:
                print("El libro ya está prestado")
                return
            libro["prestado"] = nombre

            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(lista, f, indent=4, ensure_ascii=False)

            print(f"\nDisfruta tu lectura del libro '{titulo}'\n")
            return
    print("Lo siento, el libro no existe")

def devolver_libro():
    lista = cargar_libros()
    if not lista:
        print("No hay libros disponibles ")
        return
    
    encontrado = False
    nombre = input("Ingrese su nombre: ")
    titulo = input("Que libro quieres devolver: ").lower()

    
    for libro in lista:
        if libro["titulo"].lower() == titulo and libro["prestado"] == nombre: 
            encontrado = True         
            libro["prestado"] = False
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(lista, f, indent=4, ensure_ascii=False )
            print(f"\nGracias por devolver el libro '{titulo}'\n")
            break
        
    
    
    if not encontrado:
        print("Lo siento, el libro no existe o no lo tienes prestado")