import csv
from pathlib import Path
import matplotlib.pyplot as plt

# Rutas relativas para asegurar reproducibilidad en Google Colab y en cualquier entorno local.
BASE_DIR = Path(__file__).resolve().parent.parent
DATOS_PATH = BASE_DIR / "datos" / "resultados_partidos.csv"
RESULTADOS_DIR = BASE_DIR / "resultados"
RESULTADOS_DIR.mkdir(exist_ok=True)

def inicializar_equipo(tabla, equipo):
    """Crea el registro inicial de un equipo si todavía no existe en la tabla."""
    if equipo not in tabla:
        tabla[equipo] = {
            "PJ": 0,
            "PG": 0,
            "PE": 0,
            "PP": 0,
            "GF": 0,
            "GC": 0,
            "DG": 0,
            "PTS": 0,
        }

def cargar_partidos(ruta_csv):
    """Carga los partidos desde el archivo CSV y convierte los goles a números enteros."""
    partidos = []
    with open(ruta_csv, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        columnas_requeridas = {
            "fecha",
            "equipo_local",
            "equipo_visitante",
            "goles_local",
            "goles_visitante",
        }

        if not columnas_requeridas.issubset(set(lector.fieldnames or [])):
            raise ValueError("El CSV no contiene todas las columnas requeridas.")

        for fila in lector:
            partidos.append({
                "fecha": fila["fecha"],
                "equipo_local": fila["equipo_local"],
                "equipo_visitante": fila["equipo_visitante"],
                "goles_local": int(fila["goles_local"]),
                "goles_visitante": int(fila["goles_visitante"]),
            })
    return partidos

def calcular_tabla(partidos):
    """Calcula la tabla de posiciones a partir de los resultados de cada partido."""
    tabla = {}

    for partido in partidos:
        local = partido["equipo_local"]
        visitante = partido["equipo_visitante"]
        goles_local = partido["goles_local"]
        goles_visitante = partido["goles_visitante"]

        inicializar_equipo(tabla, local)
        inicializar_equipo(tabla, visitante)

        tabla[local]["PJ"] += 1
        tabla[visitante]["PJ"] += 1

        tabla[local]["GF"] += goles_local
        tabla[local]["GC"] += goles_visitante
        tabla[visitante]["GF"] += goles_visitante
        tabla[visitante]["GC"] += goles_local

        if goles_local > goles_visitante:
            tabla[local]["PG"] += 1
            tabla[visitante]["PP"] += 1
            tabla[local]["PTS"] += 3
        elif goles_local < goles_visitante:
            tabla[visitante]["PG"] += 1
            tabla[local]["PP"] += 1
            tabla[visitante]["PTS"] += 3
        else:
            tabla[local]["PE"] += 1
            tabla[visitante]["PE"] += 1
            tabla[local]["PTS"] += 1
            tabla[visitante]["PTS"] += 1

    for equipo in tabla:
        tabla[equipo]["DG"] = tabla[equipo]["GF"] - tabla[equipo]["GC"]

    tabla_ordenada = sorted(
        tabla.items(),
        key=lambda item: (item[1]["PTS"], item[1]["DG"], item[1]["GF"]),
        reverse=True
    )

    return tabla_ordenada

def guardar_tabla(tabla_ordenada):
    """Guarda la tabla de posiciones en formato CSV dentro de la carpeta resultados."""
    ruta_salida = RESULTADOS_DIR / "tabla_posiciones.csv"

    with open(ruta_salida, "w", newline="", encoding="utf-8") as archivo:
        columnas = ["posicion", "equipo", "PJ", "PG", "PE", "PP", "GF", "GC", "DG", "PTS"]
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()

        for posicion, (equipo, datos) in enumerate(tabla_ordenada, start=1):
            fila = {"posicion": posicion, "equipo": equipo}
            fila.update(datos)
            escritor.writerow(fila)

def generar_resumen(partidos, tabla_ordenada):
    """Genera un resumen textual con indicadores generales del campeonato."""
    total_partidos = len(partidos)
    total_goles = sum(p["goles_local"] + p["goles_visitante"] for p in partidos)
    promedio_goles = total_goles / total_partidos if total_partidos else 0

    campeon_parcial = tabla_ordenada[0][0]
    mas_ganados = max(tabla_ordenada, key=lambda item: item[1]["PG"])[0]

    ruta_resumen = RESULTADOS_DIR / "resumen_torneo.txt"
    with open(ruta_resumen, "w", encoding="utf-8") as archivo:
        archivo.write("Resumen del campeonato deportivo\n")
        archivo.write("=================================\n\n")
        archivo.write(f"Cantidad de partidos analizados: {total_partidos}\n")
        archivo.write(f"Total de goles convertidos: {total_goles}\n")
        archivo.write(f"Promedio de goles por partido: {promedio_goles:.2f}\n")
        archivo.write(f"Equipo ubicado en primer lugar: {campeon_parcial}\n")
        archivo.write(f"Equipo con más partidos ganados: {mas_ganados}\n")

def generar_grafico(tabla_ordenada):
    """Genera un gráfico comparativo de puntos por equipo."""
    equipos = [equipo for equipo, datos in tabla_ordenada]
    puntos = [datos["PTS"] for equipo, datos in tabla_ordenada]

    plt.figure(figsize=(10, 6))
    plt.bar(equipos, puntos)
    plt.title("Puntos obtenidos por equipo")
    plt.xlabel("Equipos")
    plt.ylabel("Puntos")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(RESULTADOS_DIR / "grafico_puntos.png")
    plt.close()

def mostrar_tabla(tabla_ordenada):
    """Muestra la tabla de posiciones en consola para facilitar la verificación."""
    print("Tabla de posiciones")
    print("-" * 95)
    print(f"{'Pos':<5}{'Equipo':<18}{'PJ':<5}{'PG':<5}{'PE':<5}{'PP':<5}{'GF':<5}{'GC':<5}{'DG':<5}{'PTS':<5}")
    print("-" * 95)

    for posicion, (equipo, datos) in enumerate(tabla_ordenada, start=1):
        print(
            f"{posicion:<5}{equipo:<18}{datos['PJ']:<5}{datos['PG']:<5}"
            f"{datos['PE']:<5}{datos['PP']:<5}{datos['GF']:<5}"
            f"{datos['GC']:<5}{datos['DG']:<5}{datos['PTS']:<5}"
        )

def main():
    partidos = cargar_partidos(DATOS_PATH)
    tabla_ordenada = calcular_tabla(partidos)

    guardar_tabla(tabla_ordenada)
    generar_resumen(partidos, tabla_ordenada)
    generar_grafico(tabla_ordenada)
    mostrar_tabla(tabla_ordenada)

    print("\nArchivos generados correctamente en la carpeta /resultados.")

if __name__ == "__main__":
    main()
