# Issues sugeridos para Jira

## OE-1: Crear repositorio, estructura inicial y README.md

**Rol:** P1 - Líder y Organizador  
**Responsable sugerido:** Facundo Artola  
**Tipo:** Tarea  
**Prioridad:** Media

**Descripción:**  
Crear el repositorio central del proyecto en GitHub, definir la estructura inicial de carpetas y redactar el archivo README.md con la visión general del proyecto.

**Criterios de aceptación:**
- El repositorio público está creado en GitHub.
- Existen las carpetas `/datos`, `/scripts` y `/resultados`.
- El archivo README.md describe el objetivo del proyecto, escenario elegido, estructura e instrucciones de ejecución.
- Se realiza al menos un commit trazable con el ID del issue.

---

## OE-2: Desarrollar script de análisis de resultados deportivos

**Rol:** P2 - Desarrollador Técnico  
**Responsable sugerido:** Integrante 2  
**Tipo:** Tarea  
**Prioridad:** Alta

**Descripción:**  
Desarrollar el script en Python encargado de leer los resultados deportivos desde un archivo CSV y generar estadísticas del campeonato.

**Criterios de aceptación:**
- El script lee correctamente el archivo `resultados_partidos.csv`.
- Se calcula la tabla de posiciones.
- Se calculan partidos ganados, empatados y perdidos.
- Se calculan goles a favor, goles en contra, diferencia de gol y puntos.
- Se genera un resumen textual y un gráfico comparativo.
- Los resultados se guardan en la carpeta `/resultados`.

---

## OE-3: Revisar documentación, seguridad y Pull Request

**Rol:** P3 - Revisor y QA  
**Responsable sugerido:** Integrante 3  
**Tipo:** Tarea  
**Prioridad:** Alta

**Descripción:**  
Revisar la documentación del repositorio, controlar que no existan datos sensibles, validar el uso de `.gitignore` y gestionar la revisión mediante Pull Request.

**Criterios de aceptación:**
- El archivo `.gitignore` está correctamente configurado.
- No se exponen tokens ni credenciales.
- El Pull Request contiene comentarios técnicos de revisión.
- La rama de desarrollo se integra correctamente a la rama principal.
- El informe final incluye evidencias del proceso.
