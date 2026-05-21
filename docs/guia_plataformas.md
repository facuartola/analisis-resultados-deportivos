# Guía paso a paso para trabajar en Jira, GitHub y Google Colab

## 1. Crear el repositorio en GitHub

1. Entrar a GitHub.
2. Crear un repositorio nuevo llamado `analisis-resultados-deportivos`.
3. Dejarlo como público.
4. Crear el repositorio con README inicial o vacío. Si ya cargás los archivos del ZIP, no hace falta agregar más contenido manualmente.

## 2. Crear el proyecto en Jira

1. Crear un proyecto nuevo.
2. Nombre sugerido: `Análisis Resultados Deportivos`.
3. Clave sugerida: `OE`.
4. Crear tres issues:
   - OE-1: Crear repositorio, estructura inicial y README.md.
   - OE-2: Desarrollar script de análisis de resultados deportivos.
   - OE-3: Revisar documentación, seguridad y Pull Request.

## 3. Subir el proyecto desde Google Colab

En una celda de Google Colab:

```bash
!git config --global user.email "tu_email"
!git config --global user.name "Tu Nombre Completo"
```

Luego clonar el repo:

```bash
!git clone https://github.com/USUARIO/analisis-resultados-deportivos.git
%cd analisis-resultados-deportivos
```

Subir archivos y hacer commits:

```bash
!git status
!git add README.md .gitignore
!git commit -m "OE-1: Crear documentación inicial y archivo gitignore"
```

Para subir usando PAT:

```bash
!git push https://TOKEN@github.com/USUARIO/analisis-resultados-deportivos.git main
```

No mostrar el token en capturas. Conviene borrar u ocultar la celda luego de usarlo.

## 4. Crear rama de desarrollo

```bash
!git checkout -b feature/analisis-resultados
!git add datos/resultados_partidos.csv scripts/analisis_resultados.py
!git commit -m "OE-2: Agregar dataset y script de análisis deportivo"
!python scripts/analisis_resultados.py
!git add resultados/
!git commit -m "OE-2: Generar resultados del campeonato"
!git push https://TOKEN@github.com/USUARIO/analisis-resultados-deportivos.git feature/analisis-resultados
```

## 5. Crear Pull Request

1. Ir al repositorio en GitHub.
2. Crear Pull Request desde `feature/analisis-resultados` hacia `main`.
3. Agregar comentarios técnicos.
4. Hacer merge cuando esté revisado.

## 6. Capturas recomendadas

- Tablero de Jira con las tres tareas.
- Detalle de cada issue.
- Repositorio de GitHub con estructura de carpetas.
- Historial de commits.
- Rama `feature/analisis-resultados`.
- Pull Request abierto.
- Comentarios técnicos en el Pull Request.
- Resultado de ejecución del script en Colab.
- Archivos generados en `/resultados`.
