import json
from gestion_libros import *
import os





def auditoria():
    
    inconsistencia = []
    conteo = {
    "ESTADO_INVALIDO" :  0,
    "PRESTADO_SIN_USUARIO" : 0,
    "DISPONIBLE_CON_USUARIO" : 0
    }
    
    print("\n" + "=" * 50)
    print("REPORTE DEL INVENTARIO DE AUDITORIA")
    print("=" * 50)

    with open("Gestor de inventario para una Biblioteca/data/libros.json", "r", encoding="utf-8") as f:
            libros = json.load(f)
    
    total_libro = len(libros)
    
    for libro in libros:
        titulo = libro.get("titulo", "N/A")
        autor = libro.get("autor", "N/A")
        estado = libro.get("estado", "")
        prestado = libro.get("prestado", None)
    
    error = None
    
    if estado not in ["Disponible", "Prestado"]:
        error = "ESTADO_INVALIDO"
        
    elif estado == "Disponible" and prestado:
        error = "PRESTADO_SIN_USUARIO"
        
    elif estado == "Prestado" and (prestado is None or prestado == ""):
        error = "DISPONIBLE_CON_USUARIO"
        
    if error:
        inconsistencia.append({
        "titulo": titulo,
        "autor": autor,
        "estado": estado,
        "prestado": error
        })
        
        conteo[error] += 1
        
    reporte = {
        "libro_Problema" : inconsistencia,
        "resumen" : {
            "numero_de_libros" : total_libro,
            "numero_de_problemas" : len(inconsistencia),
            "conteo_por_tipo" : conteo
        }
    }
    
    try:
        with open("Gestor de inventario para una Biblioteca/data/reportes/reporte_auditoria.json", "w", encoding="utf-8") as archivo:
            json.dump(reporte, archivo, indent=4, ensure_ascii=False)
    except:
        pass
    
    print(f"Total de libros analizados: {reporte['resumen']['numero_de_libros']}")
    print(f"Numero de problemas: {reporte['resumen']['numero_de_problemas']}")
    print(f" ---- Conteo ---- \n  Estado invalido: {conteo['ESTADO_INVALIDO']} \n Prestado sin Usuario: {conteo['PRESTADO_SIN_USUARIO']} \n Disponible con Usuario: {conteo['DISPONIBLE_CON_USUARIO']} \n ")