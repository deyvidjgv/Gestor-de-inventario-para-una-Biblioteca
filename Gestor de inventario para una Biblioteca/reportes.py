import json
import os
from gestion_libros import *

RUTA_REPORTE = "/home/camper/Documentos/Ejercicios Python - Deyvid/Gestor de inventario para una Biblioteca/data/reportes/reporte_libros_2024.json"

def generar_reporte():
    if not os.path.exists(archivo):
        print("No hay libros registrados en el inventario.")
        return
    
    with open(archivo, 'r', encoding='utf-8') as f:
        try:
            libros = json.load(f)
        except json.JSONDecodeError:
            print("Error al leer el archivo.")
            return

    print("\n" + "=" * 50)
    print("REPORTE DEL INVENTARIO DE LIBROS")
    print("=" * 50)

    reporte_formateado = []
    generos = []
    for libro in libros:
        g = libro.get("genero", "Sin Género")
        if g not in generos:
            generos.append(g)

    for genero in generos:
        print(f"\n{genero}:")
        libros_categoria = []
        
        for libro in libros:
            if libro.get("genero") == genero:
                titulo = libro.get("titulo", "N/A")
                autor = libro.get("autor", "N/A")
                
                if libro.get("estado") == True:
                    estado_texto = f"Prestado a {libro.get('prestado', 'N/A')}"
                else:
                    estado_texto = "Disponible"
                
                print(f"- {titulo} | Autor: {autor} | Estado: {estado_texto}")
                
                libros_categoria.append({
                    "titulo": titulo,
                    "autor": autor,
                    "estado": estado_texto
                })
        
        reporte_formateado.append({
            "categoria": genero,
            "libros": libros_categoria
        })

    directorio = os.path.dirname(RUTA_REPORTE)
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    try:
        with open(RUTA_REPORTE, 'w', encoding='utf-8') as f_reporte:
            json.dump(reporte_formateado, f_reporte, indent=4, ensure_ascii=False)
    except:
        pass

    print("-" * 50)
    input("Presione enter para continuar")