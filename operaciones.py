# ==========================================
# Asignatura: 08GIIN - Fundamentos de Programación
# Alumno: Estevan Dominguez Raúl
# Módulo de Lógica
# Archivo: operaciones.py
# ==========================================
 
import ficheros
# ==========================================
# FUNCIONES AYUDANTES (Sencillas y directas)
# ==========================================

def pedir_texto(mensaje):
    """Pide un texto y comprueba que no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("[ERROR] Este campo no puede estar vacío.")
        else:
            return texto

def pedir_numero(mensaje):
    """Pide un número y comprueba que sea un entero mayor que 0."""
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
    """Pide los 7 números, comprueba que sean números y añade 'IMO'."""
    while True:
        numero = input("Introduce los 7 dígitos del IMO (sin la palabra 'IMO'): ")
        
        if len(numero) != 7:
            print("[ERROR] Tienen que ser exactamente 7 dígitos.")
        elif numero.isdigit() == False:
            print("[ERROR] Solo puedes introducir números.")
        else:
            clave = "IMO" + numero
            if clave in viajes_activos:
                print("[ERROR] El barco con ID " + clave + " ya existe.")
            else:
                return clave

def nombre_es_unico(nombre_test, viajes_activos):
    """Comprueba si el nombre ya existe recorriendo el diccionario."""
    for imo in viajes_activos:
        if viajes_activos[imo]["nombre"].lower() == nombre_test.lower():
            return False
    return True

def listar_barcos(viajes_activos):
    """Muestra la lista de barcos en pantalla."""
    if len(viajes_activos) == 0:
        print("\n[INFO] No hay barcos registrados actualmente.")
        return False
    
    print("\n--- BARCOS REGISTRADOS ---")
    for imo in viajes_activos:
        datos = viajes_activos[imo]
        print("ID: " + imo + " | Nombre: " + datos["nombre"] + " | Riesgo: " + str(datos["riesgo"]))
    return True

# ==========================================
# OPCIÓN 1: REGISTRAR VIAJE
# ==========================================

def menu_registro(viajes_activos):
    while True:
        print("\n--- GESTIÓN DE VIAJES ---")
        print("1) Alta de viaje")
        print("2) Baja de viaje")
        print("3) Modificación de viaje")
        print("4) Volver al menú principal")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            alta_viaje(viajes_activos)
        elif opcion == '2':
            baja_viaje(viajes_activos)
        elif opcion == '3':
            modificar_viaje(viajes_activos)
        elif opcion == '4':
            break
        else:
            print("[ERROR] Opción incorrecta.")

def alta_viaje(viajes_activos):
    print("\n--- ALTA DE NUEVO VIAJE ---")
    
    # Pedir nombre con el límite explícito de 30
    while True:
        nombre = pedir_texto("Nombre del barco (max 30 char): ")
        if len(nombre) > 30:
            print("[ERROR] El nombre no puede tener más de 30 caracteres.")
        elif nombre_es_unico(nombre, viajes_activos) == False:
            print("[ERROR] Ya existe un barco con ese nombre.")
        else:
            break
    
    edad = pedir_numero("Edad del barco (años): ")
    bandera = pedir_texto("Bandera del barco: ")
    barriles = pedir_numero("Cantidad de barriles de crudo: ")
    
    # Pedir puerto origen con límite de 20
    while True:
        puerto_origen = pedir_texto("Puerto de origen (max 20 char): ")
        if len(puerto_origen) > 20:
            print("[ERROR] El puerto no puede tener más de 20 caracteres.")
        else:
            break
            
    # Pedir puerto destino con límite de 20
    while True:
        puerto_destino = pedir_texto("Puerto de destino (max 20 char): ")
        if len(puerto_destino) > 20:
            print("[ERROR] El puerto no puede tener más de 20 caracteres.")
        else:
            break
    
    imo_clave = pedir_imo(viajes_activos)
    
    # Guardar datos
    viajes_activos[imo_clave] = {
        "nombre": nombre,
        "edad": edad,
        "bandera": bandera,
        "barriles": barriles,
        "puerto_origen": puerto_origen,
        "puerto_destino": puerto_destino,
        "estado": "Pendiente",
        "riesgo": 0
    }
    
    print("\n[ÉXITO] Viaje registrado correctamente. ID: " + imo_clave)

def baja_viaje(viajes_activos):
    print("\n--- BAJA DE VIAJE ---")
    if listar_barcos(viajes_activos) == False:
        return
    
    imo_baja = input("\nIntroduce el ID (ej. IMO1234567) del barco a eliminar o 's' para salir: ").strip().upper()
    if imo_baja.lower() == 's':
        return
    
    if imo_baja in viajes_activos:
        confirmacion = input("¿Seguro que deseas eliminar " + imo_baja + "? (s/n): ")
        if confirmacion.lower() == 's':
            del viajes_activos[imo_baja]
            print("[ÉXITO] Barco eliminado.")
        else:
            print("[INFO] Operación cancelada.")
    else:
        print("[ERROR] El ID no existe.")

def modificar_viaje(viajes_activos):
    print("\n--- MODIFICAR VIAJE ---")
    if listar_barcos(viajes_activos) == False:
        return
    
    imo_mod = input("\nIntroduce el ID del barco a modificar o 's' para salir: ").strip().upper()
    if imo_mod.lower() == 's':
        return
    
    if imo_mod in viajes_activos:
        barco = viajes_activos[imo_mod]
        print("\nNuevos datos (El IMO y barriles NO cambian).")
        
        # Validar nuevo nombre
        while True:
            nuevo_nombre = pedir_texto("Nuevo nombre [" + barco['nombre'] + "]: ")
            if len(nuevo_nombre) > 30:
                print("[ERROR] Máximo 30 caracteres.")
            else:
                break
                
        nueva_edad = pedir_numero("Nueva edad [" + str(barco['edad']) + "]: ")
        nueva_bandera = pedir_texto("Nueva bandera [" + barco['bandera'] + "]: ")
        
        # Validar nuevo puerto origen
        while True:
            nuevo_origen = pedir_texto("Nuevo puerto origen [" + barco['puerto_origen'] + "]: ")
            if len(nuevo_origen) > 20:
                print("[ERROR] Máximo 20 caracteres.")
            else:
                break
                
        # Validar nuevo puerto destino
        while True:
            nuevo_destino = pedir_texto("Nuevo puerto destino [" + barco['puerto_destino'] + "]: ")
            if len(nuevo_destino) > 20:
                print("[ERROR] Máximo 20 caracteres.")
            else:
                break
        
        # Aquí termina validación de nuevo_destino
        
        confirmacion = input("\n¿Confirmar cambios? (s/n): ")
        if confirmacion.lower() == 's':
            barco["nombre"] = nuevo_nombre
            barco["edad"] = nueva_edad
            barco["bandera"] = nueva_bandera
            barco["puerto_origen"] = nuevo_origen
            barco["puerto_destino"] = nuevo_destino
            
            # --- SOLUCIÓN AL FALLO LÓGICO ---
            barco["riesgo"] = 0
            barco["estado"] = "Pendiente"
            
            print("[ÉXITO] Datos actualizados.")
            print("[INFO] Al cambiar los datos, el riesgo se ha reiniciado a 0 y el estado a 'Pendiente'.")
        else:
            print("[INFO] Operación cancelada.")
    else:
        print("[ERROR] El ID no existe.")

# ==========================================
# OPCIÓN 2: EVALUACIÓN DE RIESGO
# ==========================================

def menu_riesgos(viajes_activos):
    """Submenú para evaluar el riesgo de los barcos."""
    
    # Se debe leer la configuración cada vez que se entra en esta opción
    config = ficheros.leer_configuracion()
    if config == None:
        print("[ERROR] No se ha podido cargar la configuración. Volviendo al menú principal.")
        return

    while True:
        print("\n--- EVALUACIÓN DE RIESGO ---")
        print("1) Listar barcos sin evaluar (riesgo 0)")
        print("2) Evaluar riesgos de un barco")
        print("3) Volver al menú principal")
        
        opcion = input("Selecciona una opción (1-3): ")
        
        if opcion == '1':
            listar_barcos_riesgo_cero(viajes_activos)
        elif opcion == '2':
            evaluar_barco(viajes_activos, config)
        elif opcion == '3':
            break
        else:
            print("[ERROR] Opción incorrecta.")

def listar_barcos_riesgo_cero(viajes_activos):
    """Lista solamente los barcos que tienen riesgo 0 (sin asignar)."""
    print("\n--- BARCOS PENDIENTES DE EVALUAR (RIESGO 0) ---")
    hay_barcos = False
    
    for imo in viajes_activos:
        datos = viajes_activos[imo]
        if datos["riesgo"] == 0:
            print("ID: " + imo + " | Nombre: " + datos["nombre"] + " | Riesgo: " + str(datos["riesgo"]))
            hay_barcos = True
            
    if hay_barcos == False:
        print("[INFO] No hay barcos pendientes de evaluación.")

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
    
    # Aplicar las reglas usando el seudocódigo del proyecto
    if barco["edad"] > config["edad_min"]:
        nuevo_riesgo = nuevo_riesgo + config["edad_peso"]
        
    if barco["barriles"] > config["barriles_min"]:
        nuevo_riesgo = nuevo_riesgo + config["barriles_peso"]
        
    if barco["bandera"] in config["banderas_conflictivas"]:
        nuevo_riesgo = nuevo_riesgo + config["bandera_peso"]
        
    if barco["puerto_origen"] in config["puertos_conflictivos"]:
        nuevo_riesgo = nuevo_riesgo + config["puertos_peso"]
        
    if barco["puerto_destino"] in config["puertos_conflictivos"]:
        nuevo_riesgo = nuevo_riesgo + config["puertos_peso"]
        
    # Si no cumple ninguna condición, el riesgo pasa de 0 a -1
    if nuevo_riesgo == 0:
        nuevo_riesgo = -1
        
    # Actualizar valor en el diccionario
    barco["riesgo"] = nuevo_riesgo
    
    # Mostrar la información completa
    print("\n[ÉXITO] Evaluación completada.")
    print("--- DATOS DEL BARCO ---")
    print("ID: " + imo_eval)
    print("Nombre: " + barco["nombre"])
    print("Edad: " + str(barco["edad"]))
    print("Bandera: " + barco["bandera"])
    print("Barriles: " + str(barco["barriles"]))
    print("Puerto Origen: " + barco["puerto_origen"])
    print("Puerto Destino: " + barco["puerto_destino"])
    print("Estado: " + barco["estado"])
    print("Riesgo Actualizado: " + str(barco["riesgo"]))

# ==========================================
# OPCIÓN 3: AUTORIZAR O BLOQUEAR VIAJE
# ==========================================

def menu_autorizaciones(viajes_activos):
    """Submenú para gestionar autorizaciones de viajes evaluados."""
    while True:
        print("\n--- GESTIÓN DE AUTORIZACIONES ---")
        print("1) Listar barcos evaluados (riesgo != 0)")
        print("2) Cambiar estado (Autorizar/Bloquear)")
        print("3) Volver al menú principal")
        
        opcion = input("Selecciona una opción (1-3): ")
        
        if opcion == '1':
            listar_barcos_evaluados(viajes_activos)
        elif opcion == '2':
            autorizar_bloquear_barco(viajes_activos)
        elif opcion == '3':
            break
        else:
            print("[ERROR] Opción incorrecta.")

def listar_barcos_evaluados(viajes_activos):
    """Lista solamente los barcos con riesgo ya asignado (diferente de 0)."""
    print("\n--- BARCOS EVALUADOS (RIESGO ASIGNADO) ---")
    hay_barcos = False
    
    for imo in viajes_activos:
        datos = viajes_activos[imo]
        # El riesgo debe ser diferente de 0 
        if datos["riesgo"] != 0:
            print("ID: " + imo + " | Nombre: " + datos["nombre"] + 
                  " | Riesgo: " + str(datos["riesgo"]) + " | Estado: " + datos["estado"])
            hay_barcos = True
            
    if hay_barcos == False:
        print("[INFO] No hay barcos con riesgo evaluado todavía.")

def autorizar_bloquear_barco(viajes_activos):
    """Permite al usuario cambiar el estado de un barco evaluado."""
    if len(viajes_activos) == 0:
        print("[INFO] No hay barcos registrados en el sistema para evaluar.")
        return
    
    imo_aut = input("\nIntroduce el ID completo (ej. IMO1234567) del barco o 's' para salir: ").strip().upper()
    
    if imo_aut == 'S':
        return
        
    if imo_aut not in viajes_activos:
        print("[ERROR] El ID introducido no existe.")
        return
        
    barco = viajes_activos[imo_aut]
    
    # Verificamos que el barco esté evaluado antes de dejar cambiar el estado
    if barco["riesgo"] == 0:
        print("[ERROR] Este barco no ha sido evaluado todavía en la Opción 2.")
        return
        
    print("\nBarco: " + barco["nombre"] + " (Riesgo: " + str(barco["riesgo"]) + ")")
    print("Estado actual: " + barco["estado"])
    
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
            print("[ERROR] Opción no válida. Introduce 'a' para Autorizar o 'b' para Bloquear.")
            
    # Mostramos la información completa actualizada
    print("\n--- DATOS ACTUALIZADOS ---")
    print("ID: " + imo_aut)
    print("Nombre: " + barco["nombre"])
    print("Riesgo: " + str(barco["riesgo"]))
    print("Nuevo Estado: " + barco["estado"])

# ==========================================
# OPCIÓN 4: FINALIZAR VIAJE
# ==========================================

def menu_finalizar(viajes_activos, historicos):
    """Submenú para finalizar viajes autorizados."""
    while True:
        print("\n--- FINALIZAR VIAJE ---")
        print("1) Listar barcos autorizados")
        print("2) Finalizar un viaje")
        print("3) Volver al menú principal")
        
        opcion = input("Selecciona una opción (1-3): ")
        
        if opcion == '1':
            listar_barcos_autorizados(viajes_activos)
        elif opcion == '2':
            finalizar_barco(viajes_activos, historicos)
        elif opcion == '3':
            break
        else:
            print("[ERROR] Opción incorrecta.")

def listar_barcos_autorizados(viajes_activos):
    """Lista solamente los barcos con estado 'Autorizado'."""
    print("\n--- BARCOS AUTORIZADOS ---")
    hay_barcos = False
    
    for imo in viajes_activos:
        datos = viajes_activos[imo]
        if datos["estado"] == "Autorizado":
            print("ID: " + imo + " | Nombre: " + datos["nombre"] + " | Riesgo: " + str(datos["riesgo"]))
            hay_barcos = True
            
    if hay_barcos == False:
        print("[INFO] No hay barcos autorizados en este momento.")
        return False
        
    return True

def finalizar_barco(viajes_activos, historicos):
    """Mueve un barco autorizado del diccionario a la lista de históricos."""
    # Reutilizamos la función de listar para ver si hay barcos antes de pedir el ID
    if listar_barcos_autorizados(viajes_activos) == False:
        return
        
    imo_fin = input("\nIntroduce el ID completo (ej. IMO1234567) del barco a finalizar o 's' para salir: ").strip().upper()
    
    if imo_fin == 'S':
        return
        
    if imo_fin not in viajes_activos:
        print("[ERROR] El ID introducido no existe.")
        return
        
    barco = viajes_activos[imo_fin]
    
    # Comprobamos que el estado sea el correcto
    if barco["estado"] != "Autorizado":
        print("[ERROR] Solo se pueden finalizar viajes que estén en estado 'Autorizado'.")
        print("Estado actual del barco: " + barco["estado"])
        return
        
    confirmacion = input("¿Seguro que deseas finalizar el viaje de " + barco["nombre"] + "? (s/n): ").strip().lower()
    
    if confirmacion == 's':
        # 1. Hacemos una copia del barco y le añadimos su IMO dentro para no perderlo
        barco_historico = barco.copy()
        barco_historico["imo"] = imo_fin
        
        # 2. Lo metemos en la lista de históricos
        historicos.append(barco_historico)
        
        # 3. Lo borramos del diccionario de activos
        del viajes_activos[imo_fin]
        
        print("[ÉXITO] El viaje ha finalizado. El barco ha sido movido a Históricos.")
    else:
        print("[INFO] Operación cancelada.")

# ==========================================
# OPCIÓN 5: REGISTRO DE INCIDENTES
# ==========================================

def menu_incidentes(viajes_activos, interceptados):
    """Submenú para registrar intercepciones o fugas de barcos."""
    while True:
        print("\n--- REGISTRO DE INCIDENTES ---")
        print("1) Intercepción por las autoridades")
        print("2) Saltarse bloqueo")
        print("3) Volver al menú principal")
        
        opcion = input("Selecciona una opción (1-3): ")
        
        if opcion == '1':
            intercepcion_autoridades(viajes_activos, interceptados)
        elif opcion == '2':
            saltarse_bloqueo(viajes_activos)
        elif opcion == '3':
            break
        else:
            print("[ERROR] Opción incorrecta.")

def intercepcion_autoridades(viajes_activos, interceptados):
    """Opción 5.1: Mueve un barco bloqueado a la lista de interceptados."""
    print("\n--- INTERCEPCIÓN POR AUTORIDADES ---")
    
    # 1. Listar solo barcos bloqueados
    hay_bloqueados = False
    for imo in viajes_activos:
        datos = viajes_activos[imo]
        if datos["estado"] == "Bloqueado":
            print("ID: " + imo + " | Nombre: " + datos["nombre"] + " | Riesgo: " + str(datos["riesgo"]))
            hay_bloqueados = True
            
    if hay_bloqueados == False:
        print("[INFO] No hay barcos en estado 'Bloqueado' actualmente.")
        return

    # 2. Intentar intercepción
    imo_int = input("\nIntroduce el ID completo del barco a interceptar o 's' para salir: ").strip().upper()
    if imo_int == 'S':
        return
        
    if imo_int not in viajes_activos:
        print("[ERROR] El ID introducido no existe.")
        return
        
    barco = viajes_activos[imo_int]
    
    if barco["estado"] != "Bloqueado":
        print("[ERROR] Solo se puede interceptar a los barcos que están bloqueados.")
        return
        
    exito = input("¿Ha sido exitosa la intercepción de " + barco["nombre"] + "? (s/n): ").strip().lower()
    
    if exito == 's':
        # Hacer copia, guardar IMO y mover a la lista (como en los históricos)
        barco_interceptado = barco.copy()
        barco_interceptado["imo"] = imo_int
        
        interceptados.append(barco_interceptado)
        del viajes_activos[imo_int]
        print("[ÉXITO] Barco interceptado y movido a la lista de incidentes.")
    else:
        print("[INFO] La intercepción falló. El barco sigue su ruta.")

def saltarse_bloqueo(viajes_activos):
    """Opción 5.2: Permite a un barco evadir el bloqueo y cambiar datos selectivamente."""
    print("\n--- SALTARSE EL BLOQUEO ---")
    
    # 1. Listar todos los barcos activos
    if listar_barcos(viajes_activos) == False:
        return
        
    # 2. Intentar saltarse el bloqueo
    imo_fuga = input("\nIntroduce el ID completo del barco o 's' para salir: ").strip().upper()
    if imo_fuga == 'S':
        return
        
    if imo_fuga not in viajes_activos:
        print("[ERROR] El ID introducido no existe.")
        return
        
    barco = viajes_activos[imo_fuga]
    
    # --- NUEVA BARRERA LÓGICA ---
    if barco["estado"] != "Bloqueado":
        print("[ERROR] Este barco está en estado '" + barco["estado"] + "'. Solo los barcos 'Bloqueados' pueden intentar fugarse.")
        return
    # ----------------------------
    
    exito = input("¿El barco " + barco["nombre"] + " ha logrado saltarse el bloqueo? (s/n): ").strip().lower()
    
    if exito == 's':
        print("\n[INFO] Fuga exitosa. Ahora puedes cambiar los datos del barco para camuflarlo.")
        print("(El IMO y los barriles no se pueden cambiar)")
        
        # 3. Preguntar uno por uno cuáles cambiar
        if input("¿Deseas cambiar el nombre? (s/n): ").strip().lower() == 's':
            while True:
                nuevo_nombre = pedir_texto("Nuevo nombre [" + barco['nombre'] + "]: ")
                if len(nuevo_nombre) > 30:
                    print("[ERROR] Máximo 30 caracteres.")
                # Si pone un nombre distinto y no es único
                elif nuevo_nombre.lower() != barco["nombre"].lower() and nombre_es_unico(nuevo_nombre, viajes_activos) == False:
                    print("[ERROR] Ya existe un barco con ese nombre.")
                else:
                    barco["nombre"] = nuevo_nombre
                    break

        if input("¿Deseas cambiar la edad? (s/n): ").strip().lower() == 's':
            barco["edad"] = pedir_numero("Nueva edad [" + str(barco['edad']) + "]: ")

        if input("¿Deseas cambiar la bandera? (s/n): ").strip().lower() == 's':
            barco["bandera"] = pedir_texto("Nueva bandera [" + barco['bandera'] + "]: ")

        if input("¿Deseas cambiar el puerto de origen? (s/n): ").strip().lower() == 's':
            while True:
                nuevo_origen = pedir_texto("Nuevo origen [" + barco['puerto_origen'] + "]: ")
                if len(nuevo_origen) > 20:
                    print("[ERROR] Máximo 20 caracteres.")
                else:
                    barco["puerto_origen"] = nuevo_origen
                    break

        if input("¿Deseas cambiar el puerto de destino? (s/n): ").strip().lower() == 's':
            while True:
                nuevo_destino = pedir_texto("Nuevo destino [" + barco['puerto_destino'] + "]: ")
                if len(nuevo_destino) > 20:
                    print("[ERROR] Máximo 20 caracteres.")
                else:
                    barco["puerto_destino"] = nuevo_destino
                    break

        # --- RESETEO DEL RIESGO Y ESTADO AL FUGARSE ---
        barco["riesgo"] = 0
        barco["estado"] = "Pendiente"
        # ----------------------------------------------

        print("\n[ÉXITO] Datos actualizados correctamente tras la evasión.")
        print("[INFO] El riesgo se ha reiniciado a 0 y el estado a 'Pendiente'.")
    else:
        print("[INFO] El intento de fuga falló. El barco se mantiene igual.")

# ==========================================
# OPCIÓN 6: INFORMACIÓN GENERAL DEL SISTEMA
# ==========================================

def info_sistema(viajes_activos, historicos, interceptados):
    """Muestra un resumen de todas las estructuras del sistema."""
    print("\n" + "="*50)
    print("       INFORMACIÓN GENERAL DEL SISTEMA")
    print("="*50)
    
    # 1. Mostrar viajes activos (Diccionario)
    print("\n>>> VIAJES ACTIVOS (En proceso) <<<")
    if len(viajes_activos) == 0:
        print("No hay viajes activos en este momento.")
    else:
        for imo in viajes_activos:
            barco = viajes_activos[imo]
            print("- ID: " + imo + " | Nombre: " + barco["nombre"] + 
                  " | Estado: " + barco["estado"] + " | Riesgo: " + str(barco["riesgo"]))
            
    # 2. Mostrar viajes históricos (Lista)
    print("\n>>> VIAJES HISTÓRICOS (Finalizados) <<<")
    if len(historicos) == 0:
        print("No hay viajes históricos registrados.")
    else:
        for barco in historicos:
            # Recuerda que al finalizar le metimos el 'imo' dentro del barco
            print("- ID: " + barco["imo"] + " | Nombre: " + barco["nombre"] + 
                  " | Barriles entregados: " + str(barco["barriles"]))
            
    # 3. Mostrar barcos interceptados (Lista)
    print("\n>>> BARCOS INTERCEPTADOS (Incidentes) <<<")
    if len(interceptados) == 0:
        print("No hay barcos interceptados registrados.")
    else:
        for barco in interceptados:
            print("- ID: " + barco["imo"] + " | Nombre: " + barco["nombre"] + 
                  " | Bandera: " + barco["bandera"])
            
    print("\n" + "="*50)

# ==========================================
# OPCIÓN 7: GESTIÓN DE FICHEROS
# ==========================================

def menu_ficheros(viajes_activos, historicos, interceptados):
    """Submenú para guardar o cargar el estado del programa.[cite: 11]"""
    while True:
        print("\n--- GESTIÓN DE FICHEROS ---")
        print("1) Guardar estado actual")
        print("2) Cargar estado")
        print("3) Volver al menú principal")
        
        opcion = input("Selecciona una opción (1-3): ")
        
        if opcion == '1':
            nombre = pedir_texto("Introduce el nombre del fichero para guardar (ej. datos.txt): ")
            ficheros.guardar_estado(nombre, viajes_activos, historicos, interceptados)
            
        elif opcion == '2':
            nombre = pedir_texto("Introduce el nombre del fichero a cargar (ej. datos.txt): ")
            exito = ficheros.cargar_estado(nombre, viajes_activos, historicos, interceptados)
            if exito:
                # El enunciado exige mostrar toda la info tras cargar correctamente
                info_sistema(viajes_activos, historicos, interceptados)
                
        elif opcion == '3':
            break
        else:
            print("[ERROR] Opción incorrecta.")

# ==========================================
# OPCIÓN 8: CAMBIO DE AÑO
# ==========================================

def cambio_ano(viajes_activos, historicos, interceptados):
    """Suma 1 año de edad a todos los barcos del sistema (activos, históricos e interceptados)."""
    print("\n--- CAMBIO DE AÑO ---")
    
    contador = 0
    
    # 1. Envejecer barcos activos (diccionario)
    for imo in viajes_activos:
        viajes_activos[imo]["edad"] = viajes_activos[imo]["edad"] + 1
        contador = contador + 1
        
    # 2. Envejecer barcos históricos (lista)
    for barco in historicos:
        barco["edad"] = barco["edad"] + 1
        contador = contador + 1
        
    # 3. Envejecer barcos interceptados (lista)
    for barco in interceptados:
        barco["edad"] = barco["edad"] + 1
        contador = contador + 1
        
    if contador > 0:
        print("[ÉXITO] Ha pasado un año. Se ha actualizado la edad de " + str(contador) + " barco(s).")
    else:
        print("[INFO] No hay ningún barco en el sistema para actualizar.")