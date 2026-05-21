# Análisis de Resultados Deportivos

Trabajo práctico de Organización Empresarial orientado a la gestión colaborativa, control de versiones y documentación de un proyecto técnico utilizando Git, GitHub, Jira y Google Colab.

## Escenario elegido

Se seleccionó el **Escenario D: Estadísticas de Resultados Deportivos**. El proyecto analiza resultados de partidos de un campeonato deportivo simulado y genera estadísticas básicas del torneo.

## Objetivo del proyecto

Procesar un archivo CSV con resultados de partidos para obtener indicadores deportivos que permitan interpretar el rendimiento de los equipos participantes.

El análisis incluye:

- cantidad de partidos jugados;
- partidos ganados, empatados y perdidos;
- goles a favor y goles en contra;
- diferencia de gol;
- puntos obtenidos;
- tabla de posiciones;
- promedio de goles por partido;
- gráfico comparativo de puntos por equipo.

## Estructura del repositorio

```text
analisis-resultados-deportivos/
├── datos/
│   └── resultados_partidos.csv
├── scripts/
│   └── analisis_resultados.py
├── resultados/
│   ├── tabla_posiciones.csv
│   ├── resumen_torneo.txt
│   └── grafico_puntos.png
├── README.md
└── .gitignore
```

## Dataset utilizado

El archivo `datos/resultados_partidos.csv` contiene datos simulados de un campeonato deportivo con seis equipos. Las columnas utilizadas son:

- `fecha`
- `equipo_local`
- `equipo_visitante`
- `goles_local`
- `goles_visitante`

Los datos fueron elaborados con fines académicos para permitir la reproducción completa del análisis.

## Ejecución en Google Colab

Para ejecutar el proyecto desde Google Colab:

1. Clonar el repositorio.
2. Ingresar a la carpeta del proyecto.
3. Ejecutar el script de análisis.

Comando de ejecución:

```bash
python scripts/analisis_resultados.py
```

## Resultados generados

El script genera automáticamente los siguientes archivos dentro de la carpeta `resultados`:

- `tabla_posiciones.csv`: tabla ordenada por puntos, diferencia de gol y goles a favor.
- `resumen_torneo.txt`: resumen general del campeonato.
- `grafico_puntos.png`: gráfico comparativo de puntos por equipo.

## Herramientas utilizadas

- Python
- Git
- GitHub
- Jira
- Google Colab
- Matplotlib

## Buenas prácticas aplicadas

- Uso de rutas relativas para asegurar reproducibilidad.
- Organización del repositorio en carpetas separadas.
- Documentación del proyecto en README.
- Uso de `.gitignore` para evitar archivos innecesarios.
- Preparación del trabajo para commits trazables vinculados a issues de Jira.
