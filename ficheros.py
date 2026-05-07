# ==========================================
# Asignatura: 08GIIN - Fundamentos de Programación
# Alumno: Estevan Dominguez Raúl
# Módulo de Persistencia con SQLite
# Archivo: ficheros.py
# ==========================================

import sqlite3

def leer_configuracion():
    """
    Lee el fichero conf.txt línea por línea.
    Separa las claves y los valores (convirtiéndolos a entero si es necesario),
    y separa los textos conflictivos (banderas/puertos) por punto y coma.
    """
    configuracion = {}
    try:
        with open("conf.txt", "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea == "" or "=" not in linea:
                    continue
                partes = linea.split("=")
                clave = partes[0].strip()
                valor = partes[1].strip()
                
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

def inicializar_base_datos(nombre_bd="sistema_naval.db"):
    """Crea la base de datos y la tabla principal si no existen."""
    conexion = sqlite3.connect(nombre_bd)
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS barcos (
            imo TEXT PRIMARY KEY,
            nombre TEXT,
            edad INTEGER,
            bandera TEXT,
            barriles INTEGER,
            puerto_origen TEXT,
            puerto_destino TEXT,
            estado TEXT,
            riesgo INTEGER,
            categoria TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def guardar_estado(nombre_fichero, viajes_activos, historicos, interceptados):
    """Guarda toda la información del sistema en la base de datos SQLite."""
    conexion = sqlite3.connect("sistema_naval.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("DELETE FROM barcos")
        
        for imo, d in viajes_activos.items():
            cursor.execute("INSERT INTO barcos VALUES (?,?,?,?,?,?,?,?,?,?)", 
                (imo, d['nombre'], d['edad'], d['bandera'], d['barriles'], d['puerto_origen'], d['puerto_destino'], d['estado'], d['riesgo'], 'VIAJE'))
            
        for d in interceptados:
            cursor.execute("INSERT INTO barcos VALUES (?,?,?,?,?,?,?,?,?,?)", 
                (d['imo'], d['nombre'], d['edad'], d['bandera'], d['barriles'], d['puerto_origen'], d['puerto_destino'], d['estado'], d['riesgo'], 'INTERCEPTADO'))
            
        for d in historicos:
            cursor.execute("INSERT INTO barcos VALUES (?,?,?,?,?,?,?,?,?,?)", 
                (d['imo'], d['nombre'], d['edad'], d['bandera'], d['barriles'], d['puerto_origen'], d['puerto_destino'], d['estado'], d['riesgo'], 'HISTORICO'))
                
        conexion.commit()
        print("\n[ÉXITO] Datos guardados correctamente en la base de datos SQLite.")
    except sqlite3.Error as e:
        print("\n[ERROR CRÍTICO] Hubo un fallo en la base de datos: " + str(e))
    finally:
        conexion.close()

def cargar_estado(nombre_fichero, viajes_activos, historicos, interceptados):
    """Lee la base de datos SQLite y reconstruye el diccionario y las listas en RAM."""
    conexion = sqlite3.connect("sistema_naval.db")
    cursor = conexion.cursor()
    try:
        viajes_activos.clear()
        historicos.clear()
        interceptados.clear()
        
        cursor.execute("SELECT * FROM barcos")
        filas = cursor.fetchall()
        
        for f in filas:
            barco = {
                "nombre": f[1], "edad": f[2], "bandera": f[3], "barriles": f[4],
                "puerto_origen": f[5], "puerto_destino": f[6], "estado": f[7], "riesgo": f[8]
            }
            categoria = f[9]
            imo = f[0]
            
            if categoria == 'VIAJE':
                viajes_activos[imo] = barco
            elif categoria == 'INTERCEPTADO':
                barco["imo"] = imo
                interceptados.append(barco)
            elif categoria == 'HISTORICO':
                barco["imo"] = imo
                historicos.append(barco)
                
        print("\n[ÉXITO] Datos cargados correctamente desde la base de datos.")
        return True
    except sqlite3.Error:
        print("\n[ERROR] No se pudo leer la base de datos.")
        return False
    finally:
        conexion.close()
