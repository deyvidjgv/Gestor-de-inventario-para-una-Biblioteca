import json
from gestion_libros import *
import os
from ruta import *



def auditoria():
    
    errores = []
    conteo = {
    "Estado_Invalido" :  0,
    "Prestado_Sin_Usuario" : 0,
    "Disponible_Usuario" : 0
    }
    
    print("\n" + "=" * 50)
    print("REPORTE DEL INVENTARIO DE AUDITORIA")
    print("=" * 50)

    with open(ruta_completa, "r", encoding="utf-8") as f:
            libros = json.load(f)
    
    total_libro = len(libros)
    
    for libro in libros:
        titulo = libro.get("titulo", "N/A")
        autor = libro.get("autor", "N/A")
        estado = libro.get("estado", False)
        prestado = libro.get("prestado", None)
    
        error = None 
        
        if estado is True and (prestado is not False and prestado != ""):
            error = "Estado_Invalido"
            
        elif estado is False and (prestado is  False or prestado == ""):
            error = "Prestado_Sin_Usuario"
            
        elif estado == "Prestado" and (prestado is None or prestado == ""):
            error = "Disponible_Usuario"
            
        if error:
            errores.append({
            "titulo": titulo,
            "autor": autor,
            "estado": estado,
            "prestado": error
            })
            
            conteo[error] += 1
        
    reporte = {
        "libro_Problema" : errores,
        "resumen" : {
            "numero_de_libros" : total_libro,
            "numero_de_problemas" : len(errores),
            "conteo_por_tipo" : conteo
        }
    }
    
    try:
        with open("/data/reportes/reporte_auditoria.json", "w", encoding="utf-8") as ruta_completa:
            json.dump(reporte, ruta_completa, indent=4, ensure_ascii=False)
    except:
        pass
    
    print(f"Total de libros analizados: {reporte['resumen']['numero_de_libros']}")
    print(f"Numero de problemas: {reporte['resumen']['numero_de_problemas']}")
    print(" ---- Conteo ---- \n")  
    print(f"Estado invalido: {conteo['Estado_Invalido']} \n Prestado sin Usuario: {conteo['Prestado_Sin_Usuario']} \n Disponible con Usuario: {conteo['Disponible_Usuario']} \n ")