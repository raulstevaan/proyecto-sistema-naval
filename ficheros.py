# ==========================================
# Asignatura: 08GIIN - Fundamentos de Programación
# Alumno: Estevan Dominguez Raúl
# Módulo para la gestión de lectura y escritura en el disco duro
# Archivo: ficheros.py
# ==========================================


def leer_configuracion():
    """
    Lee el fichero conf.txt línea por línea.
    Separa las claves y los valores y separa los textos conflictivos por punto y coma.
    """
    configuracion = {}
    
    try:
        # Usamos 'with open' para que el archivo se cierre automáticamente
        with open("conf.txt", "r", encoding="utf-8") as f:
            for linea in f:
                # Quitamos los espacios o saltos de línea de los bordes
                linea = linea.strip()
                
                # Si la línea está vacía o no tiene un "=", la ignoramos
                if linea == "" or "=" not in linea:
                    continue
                
                # Cortamos la línea por el signo "="
                partes = linea.split("=")
                clave = partes[0].strip()
                valor = partes[1].strip()
                
                # Si la clave es de banderas o puertos, es texto separado por ';'
                if clave == "banderas_conflictivas" or clave == "puertos_conflictivos":
                    configuracion[clave] = valor.split(";")
                else:
                    configuracion[clave] = int(valor)
                    
        return configuracion
        
    except FileNotFoundError:
        print("[ERROR CRÍTICO] No se encuentra el archivo 'conf.txt' en la carpeta.")
        return None
    except ValueError:
        print("[ERROR CRÍTICO] Hay un error en los números del archivo 'conf.txt'.")
        return None

def guardar_estado(nombre_fichero, viajes_activos, historicos, interceptados):
    """Guarda toda la información del sistema en un único fichero .txt."""
    try:
        with open(nombre_fichero, "w", encoding="utf-8") as f:
            # 1. Guardamos el diccionario de viajes activos
            f.write("VIAJES\n")
            for imo in viajes_activos:
                d = viajes_activos[imo]
                linea = imo + ";" + d['nombre'] + ";" + str(d['edad']) + ";" + d['bandera'] + ";" + str(d['barriles']) + ";" + d['puerto_origen'] + ";" + d['puerto_destino'] + ";" + d['estado'] + ";" + str(d['riesgo']) + "\n"
                f.write(linea)
                
            # 2. Guardamos la lista de interceptados
            f.write("INTERCEPTADOS\n")
            for d in interceptados:
                linea = d['imo'] + ";" + d['nombre'] + ";" + str(d['edad']) + ";" + d['bandera'] + ";" + str(d['barriles']) + ";" + d['puerto_origen'] + ";" + d['puerto_destino'] + ";" + d['estado'] + ";" + str(d['riesgo']) + "\n"
                f.write(linea)
                
            # 3. Guardamos la lista de históricos
            f.write("HISTORICOS\n")
            for d in historicos:
                linea = d['imo'] + ";" + d['nombre'] + ";" + str(d['edad']) + ";" + d['bandera'] + ";" + str(d['barriles']) + ";" + d['puerto_origen'] + ";" + d['puerto_destino'] + ";" + d['estado'] + ";" + str(d['riesgo']) + "\n"
                f.write(linea)
                
        print("\n[ÉXITO] Datos guardados correctamente en el fichero: " + nombre_fichero)
        
    except IOError:
        print("\n[ERROR CRÍTICO] No se pudo escribir en el archivo.")

def cargar_estado(nombre_fichero, viajes_activos, historicos, interceptados):
    """Lee un fichero .txt y reconstruye el diccionario y las listas."""
    try:
        with open(nombre_fichero, "r", encoding="utf-8") as f:
            # Primero vaciamos las estructuras actuales para que no se mezclen datos
            viajes_activos.clear()
            historicos.clear()
            interceptados.clear()
            
            seccion_actual = ""
            
            for linea in f:
                linea = linea.strip()
                if linea == "":
                    continue
                
                # Detectar las palabras clave que separan la información
                if linea == "VIAJES" or linea == "INTERCEPTADOS" or linea == "HISTORICOS":
                    seccion_actual = linea
                    continue
                    
                # Extraer la información del barco separando por ';'
                partes = linea.split(";")
                if len(partes) >= 9:
                    imo = partes[0]
                    barco = {
                        "nombre": partes[1],
                        "edad": int(partes[2]),
                        "bandera": partes[3],
                        "barriles": int(partes[4]),
                        "puerto_origen": partes[5],
                        "puerto_destino": partes[6],
                        "estado": partes[7],
                        "riesgo": int(partes[8])
                    }
                    
                    # Meter el barco en la estructura correspondiente
                    if seccion_actual == "VIAJES":
                        viajes_activos[imo] = barco
                    elif seccion_actual == "INTERCEPTADOS":
                        barco["imo"] = imo
                        interceptados.append(barco)
                    elif seccion_actual == "HISTORICOS":
                        barco["imo"] = imo
                        historicos.append(barco)
                        
        print("\n[ÉXITO] Datos cargados correctamente desde el fichero: " + nombre_fichero)
        return True
        
    except FileNotFoundError:
        print("\n[ERROR] El archivo '" + nombre_fichero + "' no existe en esta carpeta.")
        return False
    except ValueError:
        print("\n[ERROR] El archivo está corrupto o tiene un formato incorrecto.")
        return False