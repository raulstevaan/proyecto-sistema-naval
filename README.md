**Autor:** Raúl Estevan 
**Asignatura:** Fundamentos de Programación (08 GIIN) 

## 📝 Descripción del Proyecto
Este proyecto simula la gestión completa de los viajes de barcos petroleros.El programa sigue un flujo claro: registro de datos básicos, cálculo de riesgo, autorización o bloqueo, y gestión de incidentes (fugas o interceptaciones).

## 🛠️ Arquitectura del Software
El proyecto se divide en tres módulos para evitar importaciones circulares:

* **`main.py`**: Motor principal. [cite_start]Muestra el menú y gestiona las opciones del usuario.
* **`operaciones.py`**: Lógica de negocio. Incluye altas, bajas, cálculo de riesgos y gestión de incidentes.
* **`ficheros.py`**: Persistencia de datos. Lee la configuración y guarda/carga el estado del sistema.

## ⚙️ Configuración del Sistema
El programa utiliza un archivo `conf.txt` para definir las reglas de riesgo sin modificar el código:
* [cite_start]**`edad_min`**: Edad mínima para sumar puntos de riesgo.
* **`banderas_conflictivas`**: Países bajo vigilancia (Irán, Cuba, Panamá, etc.).
* **`puertos_conflictivos`**: Listado de puertos de alto riesgo.
* **`barriles_min`**: Cantidad de crudo necesaria para aumentar el riesgo.

## 🛡️ Manejo de Errores
El software incluye barreras de seguridad para ser "a prueba de fallos":
* **Validaciones robustas**: Funciones que impiden campos vacíos o tipos de datos incorrectos.
* **Gestión de Ficheros**: Uso de `try-except` para errores como `FileNotFoundError` al cargar datos.
* **Control de Estados**: Reseteo automático de riesgo si se modifican datos críticos del barco.

## 📋 Estructuras de Datos
La información se gestiona en RAM mediante tres estructura:
1. **Diccionario `viajes_activos`**: Almacena barcos navegando usando el IMO como clave.
2. **Lista `historicos`**: Barcos que han finalizado su viaje correctamente.
3. **Lista `interceptados`**: Barcos bloqueados capturados por autoridades.

---
*Este proyecto fue desarrollado como parte del Grado en Ingeniería Informática.* 
