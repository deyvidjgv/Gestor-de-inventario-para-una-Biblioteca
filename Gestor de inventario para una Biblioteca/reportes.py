import json
import os
from gestion_libros import *
from ruta import *

reporte = "/data/reportes/reporte_libros_2024.json"
ruta_report = ruta + reporte

def generar_reporte():
    if not os.path.exists(ruta_report):
        print("No hay libros registrados en el inventario.")
        return
    
    with open(ruta_report, 'r', encoding='utf-8') as f:
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
#obtengo el genero sin repetirlo
    for libro in libros:
        g = libro.get("genero", "Sin Género")
        if g not in generos:
            generos.append(g)
#agrupo por genero
    for genero in generos:
        print(f"\n{genero}:")
        libros_categoria = []
        
        for libro in libros:
            if libro.get("genero") == genero:
                titulo = libro.get("titulo", "N/A") #N/A por si falta algo
                autor = libro.get("autor", "N/A")
                
                if libro.get("estado") == True:
                    estado_texto = f"Prestado a {libro.get('prestado', 'N/A')}"
                else:
                    estado_texto = "Disponible"
                
                print(f"- {titulo} | Autor: {autor} | Estado: {estado_texto}")
                #guarda el reporte 
                libros_categoria.append({
                    "titulo": titulo,
                    "autor": autor,
                    "estado": estado_texto
                })
        
        reporte_formateado.append({
            "categoria": genero,
            "libros": libros_categoria
        })

    directorio = os.path.dirname(reporte) #devuelve la carpeta
    if not os.path.exists(directorio): #verifica si existe
        os.makedirs(directorio)

    try:
        with open(reporte, 'w', encoding='utf-8') as f_reporte:
            json.dump(reporte_formateado, f_reporte, indent=4, ensure_ascii=False)
    except:
        pass

    print("-" * 50)
    input("Presione enter para continuar")


