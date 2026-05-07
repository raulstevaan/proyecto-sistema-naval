# ==========================================
# Asignatura: 08GIIN - Fundamentos de Programación
# Alumno: Estevan Dominguez Raúl
# Programa Principal
# Archivo: main.py
# ==========================================

import operaciones
import ficheros   

def mostrar_menu():
    print("\n*************************************")
    print("*   SISTEMA DE GESTIÓN NAVAL        *")
    print("*************************************")
    print("* 1) Registrar viaje                *")
    print("* 2) Evaluación de riesgo           *")
    print("* 3) Autorizar o bloquear viaje     *")
    print("* 4) Finalizar viaje                *")
    print("* 5) Registro de incidentes         *")
    print("* 6) Información del sistema        *")
    print("* 7) Gestión de Ficheros            *")
    print("* 8) Cambio año                     *")
    print("* 9) Salir                          *")
    print("*************************************")

def main():
    # Inicialización de las estructuras de datos principales en memoria
    viajes_activos = {}      
    interceptados = []       
    historicos = []          

    while True:
        mostrar_menu()
        entrada = input("\nElige una opción (1-9): ")

        try:
            opcion = int(entrada)
            
            if opcion == 1:
                print("\n[INFO] Opción 1: Registrar viaje...")
                operaciones.menu_registro(viajes_activos)
            
            elif opcion == 2:
                print("\n[INFO] Opción 2: Evaluación de riesgo...")
                operaciones.menu_riesgos(viajes_activos)
            elif opcion == 3:
                print("\n[INFO] Opción 3: Autorizar o bloquear viaje...")
                operaciones.menu_autorizaciones(viajes_activos)

            elif opcion == 4:
                print("\n[INFO] Opción 4: Finalizar viaje...")
                operaciones.menu_finalizar(viajes_activos, historicos)
            elif opcion == 5:
                print("\n[INFO] Opción 5: Registro de incidentes...")
                operaciones.menu_incidentes(viajes_activos, interceptados)
            elif opcion == 6:
                print("\n[INFO] Opción 6: Información del sistema...")
                operaciones.info_sistema(viajes_activos, historicos, interceptados)
            elif opcion == 7:
                print("\n[INFO] Opción 7: Gestión de Ficheros...")
                operaciones.menu_ficheros(viajes_activos, historicos, interceptados)
            elif opcion == 8:
                print("\n[INFO] Opción 8: Cambio año...")
                operaciones.cambio_ano(viajes_activos, historicos, interceptados)
            elif opcion == 9:
                print("\n[INFO] Iniciando proceso de salida...")
                guardar = input("¿Deseas guardar los datos actuales antes de salir? (s/n): ").strip().lower()
                if guardar == 's':
                    nombre_fichero = input("Introduce el nombre del fichero para guardar (ej. final.txt): ").strip()
                    if nombre_fichero != "":
                        ficheros.guardar_estado(nombre_fichero, viajes_activos, historicos, interceptados)
                
                print("Cerrando el Sistema de Gestión Naval. ¡Hasta pronto!")
                break
            
            else:
                print("\n[ERROR] Opción incorrecta. Por favor, introduce un número del 1 al 9.")
                
        except ValueError:
            print("\n[ERROR] Entrada no válida. Debes introducir un número entero.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()