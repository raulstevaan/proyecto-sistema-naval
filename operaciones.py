# ==========================================
# Asignatura: 08GIIN - Fundamentos de Programación
# Alumno: Estevan Dominguez Raúl
# Módulo de Lógica
# Archivo: operaciones.py
# ==========================================
 
import ficheros

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("[ERROR] Este campo no puede estar vacío.")
        else:
            return texto

def pedir_numero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("[ERROR] El valor debe ser mayor que 0.")
            else:
                return valor
        except ValueError:
            print("[ERROR] Debes escribir un número entero.")

def pedir_imo(viajes_activos):
    while True:
        numero = input("Introduce los 7 dígitos del IMO (ej. 1234567): ").strip()
        # Si el usuario escribe 'IMO' por costumbre, se lo quitamos
        if numero.upper().startswith("IMO"):
            numero = numero[3:]
            
        if len(numero) != 7 or not numero.isdigit():
            print("[ERROR] Tienen que ser exactamente 7 dígitos numéricos.")
        else:
            clave = "IMO" + numero
            if clave in viajes_activos:
                print("[ERROR] El barco con ID " + clave + " ya existe.")
            else:
                return clave

def nombre_es_unico(nombre_test, viajes_activos):
    for imo in viajes_activos:
        if viajes_activos[imo]["nombre"].lower() == nombre_test.lower():
            return False
    return True

def listar_barcos(viajes_activos):
    if len(viajes_activos) == 0:
        print("\n[INFO] No hay barcos registrados actualmente.")
        return False
    print("\n--- BARCOS REGISTRADOS ---")
    for imo in viajes_activos:
        datos = viajes_activos[imo]
        print(f"ID: {imo} | Nombre: {datos['nombre']} | Riesgo: {datos['riesgo']}")
    return True

# --- OPCIÓN 1: REGISTRO ---
def menu_registro(viajes_activos):
    while True:
        print("\n--- GESTIÓN DE VIAJES ---")
        print("1) Alta de viaje")
        print("2) Baja de viaje")
        print("3) Modificación de viaje")
        print("4) Volver al menú principal")
        opcion = input("Selecciona una opción (1-4): ")
        if opcion == '1': alta_viaje(viajes_activos)
        elif opcion == '2': baja_viaje(viajes_activos)
        elif opcion == '3': modificar_viaje(viajes_activos)
        elif opcion == '4': break
        else: print("[ERROR] Opción incorrecta.")

def alta_viaje(viajes_activos):
    print("\n--- ALTA DE NUEVO VIAJE ---")
    while True:
        nombre = pedir_texto("Nombre del barco (max 30 char): ")
        if len(nombre) > 30: print("[ERROR] El nombre no puede tener más de 30 caracteres.")
        elif not nombre_es_unico(nombre, viajes_activos): print("[ERROR] Ya existe un barco con ese nombre.")
        else: break
    
    edad = pedir_numero("Edad del barco (años): ")
    bandera = pedir_texto("Bandera del barco: ")
    barriles = pedir_numero("Cantidad de barriles de crudo: ")
    
    while True:
        puerto_origen = pedir_texto("Puerto de origen (max 20 char): ")
        if len(puerto_origen) > 20: print("[ERROR] Máximo 20 caracteres.")
        else: break
            
    while True:
        puerto_destino = pedir_texto("Puerto de destino (max 20 char): ")
        if len(puerto_destino) > 20: print("[ERROR] Máximo 20 caracteres.")
        else: break
    
    imo_clave = pedir_imo(viajes_activos)
    
    viajes_activos[imo_clave] = {
        "nombre": nombre, "edad": edad, "bandera": bandera, "barriles": barriles,
        "puerto_origen": puerto_origen, "puerto_destino": puerto_destino,
        "estado": "Pendiente", "riesgo": 0
    }
    print("\n[ÉXITO] Viaje registrado correctamente. ID: " + imo_clave)

def baja_viaje(viajes_activos):
    print("\n--- BAJA DE VIAJE ---")
    if not listar_barcos(viajes_activos): return
    imo_baja = input("\nIntroduce el ID del barco a eliminar o 's' para salir: ").strip().upper()
    if imo_baja == 'S': return
    if imo_baja in viajes_activos:
        if input(f"¿Seguro que deseas eliminar {imo_baja}? (s/n): ").lower() == 's':
            del viajes_activos[imo_baja]
            print("[ÉXITO] Barco eliminado.")
        else:
            print("[INFO] Operación cancelada.")
    else:
        print("[ERROR] El ID no existe.")

def modificar_viaje(viajes_activos):
    print("\n--- MODIFICAR VIAJE ---")
    if not listar_barcos(viajes_activos): return
    imo_mod = input("\nIntroduce el ID del barco a modificar o 's' para salir: ").strip().upper()
    if imo_mod == 'S': return
    if imo_mod in viajes_activos:
        barco = viajes_activos[imo_mod]
        print("\nNuevos datos (El IMO y barriles NO cambian).")
        while True:
            nuevo_nombre = pedir_texto(f"Nuevo nombre [{barco['nombre']}]: ")
            if len(nuevo_nombre) > 30: print("[ERROR] Máximo 30 caracteres.")
            else: break
        nueva_edad = pedir_numero(f"Nueva edad [{barco['edad']}]: ")
        nueva_bandera = pedir_texto(f"Nueva bandera [{barco['bandera']}]: ")
        while True:
            nuevo_origen = pedir_texto(f"Nuevo puerto origen [{barco['puerto_origen']}]: ")
            if len(nuevo_origen) > 20: print("[ERROR] Máximo 20 caracteres.")
            else: break
        while True:
            nuevo_destino = pedir_texto(f"Nuevo puerto destino [{barco['puerto_destino']}]: ")
            if len(nuevo_destino) > 20: print("[ERROR] Máximo 20 caracteres.")
            else: break
        
        if input("\n¿Confirmar cambios? (s/n): ").lower() == 's':
            barco["nombre"] = nuevo_nombre
            barco["edad"] = nueva_edad
            barco["bandera"] = nueva_bandera
            barco["puerto_origen"] = nuevo_origen
            barco["puerto_destino"] = nuevo_destino
            barco["riesgo"] = 0
            barco["estado"] = "Pendiente"
            print("[ÉXITO] Datos actualizados. El riesgo se ha reiniciado a 0.")
        else:
            print("[INFO] Operación cancelada.")
    else:
        print("[ERROR] El ID no existe.")

# --- OPCIÓN 2: RIESGOS ---
def menu_riesgos(viajes_activos):
    config = ficheros.leer_configuracion()
    if config is None: return
    while True:
        print("\n--- EVALUACIÓN DE RIESGO ---")
        print("1) Listar barcos sin evaluar (riesgo 0)")
        print("2) Evaluar riesgos de un barco")
        print("3) Volver al menú principal")
        opcion = input("Selecciona una opción (1-3): ")
        if opcion == '1': listar_barcos_riesgo_cero(viajes_activos)
        elif opcion == '2': evaluar_barco(viajes_activos, config)
        elif opcion == '3': break
        else: print("[ERROR] Opción incorrecta.")

def listar_barcos_riesgo_cero(viajes_activos):
    print("\n--- BARCOS PENDIENTES DE EVALUAR (RIESGO 0) ---")
    hay_barcos = False
    for imo, datos in viajes_activos.items():
        if datos["riesgo"] == 0:
            print(f"ID: {imo} | Nombre: {datos['nombre']} | Riesgo: 0")
            hay_barcos = True
    if not hay_barcos: print("[INFO] No hay barcos pendientes de evaluación.")

def evaluar_barco(viajes_activos, config):
    """Calcula el riesgo de un barco según la configuración."""
    if len(viajes_activos) == 0:
        print("[INFO] No hay barcos registrados en el sistema para evaluar.")
        return

    imo_eval = input("\nIntroduce el ID del barco a evaluar o 's' para salir: ").strip().upper()
    if imo_eval.lower() == 's':
        return
        
    if imo_eval not in viajes_activos:
        print("[ERROR] El ID introducido no existe.")
        return
        
    barco = viajes_activos[imo_eval]
    nuevo_riesgo = 0
    
    # --- LA CORRECCIÓN DE LAS MAYÚSCULAS ESTÁ AQUÍ ---
    banderas_conf = [b.lower() for b in config["banderas_conflictivas"]]
    puertos_conf = [p.lower() for p in config["puertos_conflictivos"]]

    if barco["edad"] > config["edad_min"]:
        nuevo_riesgo = nuevo_riesgo + config["edad_peso"]
        
    if barco["barriles"] > config["barriles_min"]:
        nuevo_riesgo = nuevo_riesgo + config["barriles_peso"]
        
    if barco["bandera"].lower() in banderas_conf:
        nuevo_riesgo = nuevo_riesgo + config["bandera_peso"]
        
    if barco["puerto_origen"].lower() in puertos_conf:
        nuevo_riesgo = nuevo_riesgo + config["puertos_peso"]
        
    if barco["puerto_destino"].lower() in puertos_conf:
        nuevo_riesgo = nuevo_riesgo + config["puertos_peso"]
    # -------------------------------------------------
        
    if nuevo_riesgo == 0:
        nuevo_riesgo = -1
        
    barco["riesgo"] = nuevo_riesgo
    print("\n[ÉXITO] Evaluación completada. Riesgo Actualizado: " + str(barco["riesgo"]))

# --- OPCIÓN 3: AUTORIZACIONES ---
def menu_autorizaciones(viajes_activos):
    while True:
        print("\n--- GESTIÓN DE AUTORIZACIONES ---")
        print("1) Listar barcos evaluados")
        print("2) Cambiar estado (Autorizar/Bloquear)")
        print("3) Volver al menú principal")
        opcion = input("Selecciona una opción (1-3): ")
        if opcion == '1': listar_barcos_evaluados(viajes_activos)
        elif opcion == '2': autorizar_bloquear_barco(viajes_activos)
        elif opcion == '3': break
        else: print("[ERROR] Opción incorrecta.")

def listar_barcos_evaluados(viajes_activos):
    print("\n--- BARCOS EVALUADOS ---")
    hay_barcos = False
    for imo, datos in viajes_activos.items():
        if datos["riesgo"] != 0:
            print(f"ID: {imo} | Nombre: {datos['nombre']} | Riesgo: {datos['riesgo']} | Estado: {datos['estado']}")
            hay_barcos = True
    if not hay_barcos: print("[INFO] No hay barcos con riesgo evaluado todavía.")

def autorizar_bloquear_barco(viajes_activos):
    imo_aut = input("\nIntroduce el ID completo del barco o 's' para salir: ").strip().upper()
    if imo_aut == 'S': return
    if imo_aut not in viajes_activos:
        print("[ERROR] El ID introducido no existe.")
        return
        
    barco = viajes_activos[imo_aut]
    if barco["riesgo"] == 0:
        print("[ERROR] Este barco no ha sido evaluado todavía.")
        return
        
    while True:
        nuevo_estado = input("¿Deseas 'Autorizar' o 'Bloquear' este viaje? (a/b): ").strip().lower()
        if nuevo_estado == 'a':
            barco["estado"] = "Autorizado"
            print("[ÉXITO] El viaje ha sido Autorizado.")
            break
        elif nuevo_estado == 'b':
            barco["estado"] = "Bloqueado"
            print("[ÉXITO] El viaje ha sido Bloqueado.")
            break
        else:
            print("[ERROR] Introduce 'a' o 'b'.")

# --- OPCIÓN 4: FINALIZAR ---
def menu_finalizar(viajes_activos, historicos):
    while True:
        print("\n--- FINALIZAR VIAJE ---")
        print("1) Listar barcos autorizados")
        print("2) Finalizar un viaje")
        print("3) Volver al menú principal")
        opcion = input("Selecciona una opción (1-3): ")
        if opcion == '1': listar_barcos_autorizados(viajes_activos)
        elif opcion == '2': finalizar_barco(viajes_activos, historicos)
        elif opcion == '3': break
        else: print("[ERROR] Opción incorrecta.")

def listar_barcos_autorizados(viajes_activos):
    print("\n--- BARCOS AUTORIZADOS ---")
    hay_barcos = False
    for imo, datos in viajes_activos.items():
        if datos["estado"] == "Autorizado":
            print(f"ID: {imo} | Nombre: {datos['nombre']} | Riesgo: {datos['riesgo']}")
            hay_barcos = True
    if not hay_barcos: print("[INFO] No hay barcos autorizados.")
    return hay_barcos

def finalizar_barco(viajes_activos, historicos):
    if not listar_barcos_autorizados(viajes_activos): return
    imo_fin = input("\nIntroduce el ID completo del barco a finalizar o 's' para salir: ").strip().upper()
    if imo_fin == 'S': return
    if imo_fin in viajes_activos and viajes_activos[imo_fin]["estado"] == "Autorizado":
        if input(f"¿Finalizar viaje de {viajes_activos[imo_fin]['nombre']}? (s/n): ").lower() == 's':
            barco = viajes_activos[imo_fin].copy()
            barco["imo"] = imo_fin
            historicos.append(barco)
            del viajes_activos[imo_fin]
            print("[ÉXITO] Barco movido a Históricos.")
    else:
        print("[ERROR] El ID no existe o no está autorizado.")

# --- OPCIÓN 5: INCIDENTES ---
def menu_incidentes(viajes_activos, interceptados):
    while True:
        print("\n--- REGISTRO DE INCIDENTES ---")
        print("1) Intercepción por autoridades")
        print("2) Saltarse bloqueo")
        print("3) Volver")
        opcion = input("Selecciona una opción (1-3): ")
        if opcion == '1': intercepcion_autoridades(viajes_activos, interceptados)
        elif opcion == '2': saltarse_bloqueo(viajes_activos)
        elif opcion == '3': break
        else: print("[ERROR] Opción incorrecta.")

def intercepcion_autoridades(viajes_activos, interceptados):
    print("\n--- INTERCEPCIÓN ---")
    imo_int = input("Introduce el ID del barco bloqueado o 's': ").strip().upper()
    if imo_int == 'S': return
    if imo_int in viajes_activos and viajes_activos[imo_int]["estado"] == "Bloqueado":
        if input("¿Intercepción exitosa? (s/n): ").lower() == 's':
            barco = viajes_activos[imo_int].copy()
            barco["imo"] = imo_int
            interceptados.append(barco)
            del viajes_activos[imo_int]
            print("[ÉXITO] Movido a incidentes.")
    else:
        print("[ERROR] Barco no encontrado o no está bloqueado.")

def saltarse_bloqueo(viajes_activos):
    imo_fuga = input("\nID del barco bloqueado que intenta fugarse o 's': ").strip().upper()
    if imo_fuga == 'S': return
    if imo_fuga in viajes_activos and viajes_activos[imo_fuga]["estado"] == "Bloqueado":
        barco = viajes_activos[imo_fuga]
        if input("¿Fuga exitosa? (s/n): ").lower() == 's':
            print("\n[INFO] Fuga exitosa. Reseteando riesgo y estado.")
            barco["riesgo"] = 0
            barco["estado"] = "Pendiente"
        else:
            print("[INFO] Intento fallido.")
    else:
        print("[ERROR] Barco no encontrado o no bloqueado.")

# --- OPCIONES 6, 7 y 8 ---
def info_sistema(viajes_activos, historicos, interceptados):
    print("\n" + "="*50 + "\n       INFORMACIÓN GENERAL DEL SISTEMA\n" + "="*50)
    print("\n>>> VIAJES ACTIVOS <<<")
    for imo, b in viajes_activos.items(): print(f"- ID: {imo} | Nombre: {b['nombre']} | Estado: {b['estado']}")
    print("\n>>> HISTÓRICOS <<<")
    for b in historicos: print(f"- ID: {b['imo']} | Nombre: {b['nombre']}")
    print("\n>>> INTERCEPTADOS <<<")
    for b in interceptados: print(f"- ID: {b['imo']} | Nombre: {b['nombre']}")

def menu_ficheros(viajes_activos, historicos, interceptados):
    while True:
        print("\n--- GESTIÓN DE FICHEROS (SQLITE) ---")
        print("1) Guardar estado en BD")
        print("2) Cargar estado desde BD")
        print("3) Volver")
        opcion = input("Selecciona (1-3): ")
        if opcion == '1': ficheros.guardar_estado("bd", viajes_activos, historicos, interceptados)
        elif opcion == '2': 
            if ficheros.cargar_estado("bd", viajes_activos, historicos, interceptados):
                info_sistema(viajes_activos, historicos, interceptados)
        elif opcion == '3': break

def cambio_ano(viajes_activos, historicos, interceptados):
    for imo in viajes_activos: viajes_activos[imo]["edad"] += 1
    for b in historicos: b["edad"] += 1
    for b in interceptados: b["edad"] += 1
    print("[ÉXITO] Todos los barcos han envejecido 1 año.")
