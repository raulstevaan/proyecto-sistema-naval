# 🚢 Sistema de Gestión Naval (SGN) - Versión SQLite

**Autor:** Raúl Estevan Domínguez  
**Asignatura:** Fundamentos de Programación (08 GIIN)  
**Edición:** Octubre 2026

> **🌟 Versión 2.0 (Rama Actual): Persistencia con Bases de Datos** > Estás visualizando la rama `version-sqlite`. En esta versión, el sistema ha sido refactorizado para abandonar el almacenamiento en ficheros de texto plano (usado en la rama `main`) e implementar una **base de datos relacional (SQLite)**, demostrando escalabilidad y buenas prácticas de ingeniería de software.

## 📝 Descripción del Proyecto
Este proyecto simula la gestión completa de rutas petroleras. El software permite registrar navíos, calcular riesgos de seguridad dinámicos y gestionar su ciclo de vida (autorizaciones, bloqueos, fugas o interceptaciones).

## 🛠️ Arquitectura y Mejoras Técnicas
El código mantiene una estricta separación de responsabilidades para evitar importaciones circulares:

* **`main.py`**: Interfaz de usuario (terminal) y control del bucle principal.
* **`operaciones.py`**: Motor lógico. Evalúa los riesgos, valida las entradas del usuario y gestiona el estado en memoria (diccionarios y listas).
* **`ficheros.py` (Módulo Refactorizado)**: 
  * Sustituye la escritura secuencial por **consultas SQL**.
  * Utiliza consultas parametrizadas (`?`) para prevenir inyecciones SQL.
  * Implementa el IMO del barco como `PRIMARY KEY` para garantizar la integridad referencial y evitar registros duplicados.
  * Mantiene la lectura externa de reglas de negocio a través de `conf.txt`.

## ⚙️ Configuración del Sistema (`conf.txt`)
El motor de evaluación es dinámico. Las siguientes variables se pueden modificar en `conf.txt` sin alterar el código fuente:
* `edad_min` / `edad_peso`: Umbral de antigüedad y su penalización.
* `barriles_min` / `barriles_peso`: Volumen de carga crítica.
* `banderas_conflictivas`: Lista de países sancionados (ej. Irán, Panamá).
* `puertos_conflictivos`: Zonas geográficas de alto riesgo.

## 🛡️ Robustez y Control de Errores
El sistema incluye protección activa contra fallos de ejecución:
* **Validación de Entradas:** Bloqueo de campos vacíos y formatos incorrectos (ej. validación estricta de 7 dígitos para el IMO).
* **Manejo de Excepciones:** Control de `sqlite3.Error` al interactuar con la base de datos y de `FileNotFoundError` al leer configuraciones.
* **Normalización de Datos:** Conversión a minúsculas interna (`.lower()`) en validaciones de cadenas para evitar falsos negativos por errores de tipografía del usuario.

## 🚀 Cómo ejecutarlo
1. Clona el repositorio y sitúate en la rama `version-sqlite`.
2. Asegúrate de tener Python 3.10+ (Compatible con 3.13).
3. Ejecuta el archivo principal:
   ```bash
   python main.py
