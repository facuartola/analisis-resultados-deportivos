# Comentarios técnicos sugeridos para el Pull Request

Estos comentarios pueden usarse como base para cumplir con la revisión por pares solicitada.

1. Se verifica que el script utiliza rutas relativas mediante `Path`, lo que permite ejecutar el proyecto en Google Colab sin depender de rutas locales del equipo.

2. Se revisa que el archivo CSV contenga las columnas necesarias antes de procesar los datos, reduciendo errores al ejecutar el análisis.

3. Se recomienda mantener los archivos generados dentro de `/resultados` para conservar una estructura clara y reproducible.

4. Se confirma que el archivo `.gitignore` evita subir archivos temporales, cachés de Python y checkpoints de notebooks.

5. La tabla de posiciones queda ordenada por puntos, diferencia de gol y goles a favor, criterio adecuado para el análisis deportivo.
