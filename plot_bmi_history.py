import argparse
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from bmi import cargar_historial


def calcular_tendencia_bmi(registros, threshold=0.1):
    """Return 'rising', 'falling' or 'stable' depending on BMI trend."""
    if len(registros) < 2:
        return "stable"
    registros_sorted = sorted(registros, key=lambda r: r.get("fecha", ""))
    primero = float(registros_sorted[0]["bmi"])
    ultimo = float(registros_sorted[-1]["bmi"])
    diff = ultimo - primero
    if diff > threshold:
        return "rising"
    elif diff < -threshold:
        return "falling"
    return "stable"


def analizar_registros_recientes(nombre, semanas=4, base_dir="registros"):
    """Analiza las \u00faltimas ``semanas`` de registros y muestra consejos."""
    registros = cargar_historial(nombre, base_dir)
    if not registros:
        print(f"No hay historial para {nombre}")
        return

    limite = datetime.now() - timedelta(weeks=semanas)
    recientes = [
        r
        for r in registros
        if datetime.fromisoformat(r["fecha"]) >= limite
    ]
    if len(recientes) < 2:
        print("No hay suficientes registros recientes para analizar.")
        return

    recientes_sorted = sorted(recientes, key=lambda r: r.get("fecha", ""))
    tendencia = calcular_tendencia_bmi(recientes_sorted)
    primera = recientes_sorted[0]["clasificacion"]
    ultima = recientes_sorted[-1]["clasificacion"]

    orden = ["Muy bajo", "Bajo", "Normal", "Alto", "Muy alto"]
    idx_primera = orden.index(primera)
    idx_ultima = orden.index(ultima)

    if idx_ultima < idx_primera:
        cambio = f"mejor\u00f3 (de {primera} a {ultima}). \u00a1Buen trabajo!"
    elif idx_ultima > idx_primera:
        cambio = (
            f"empeor\u00f3 (de {primera} a {ultima}). "
            "Revisa tu alimentaci\u00f3n y actividad f\u00edsica."
        )
    else:
        cambio = f"se mantiene en {ultima}."

    if tendencia == "rising":
        tendencia_msg = "tu BMI est\u00e1 subiendo"
    elif tendencia == "falling":
        tendencia_msg = "tu BMI est\u00e1 bajando"
    else:
        tendencia_msg = "tu BMI se mantiene estable"

    print(
        "En las \u00faltimas "
        f"{semanas} semanas {tendencia_msg} y tu clasificaci\u00f3n {cambio}"
    )


def plot_historial(nombre, base_dir="registros"):
    registros = cargar_historial(nombre, base_dir)
    if not registros:
        print(f"No hay historial para {nombre}")
        return
    registros_sorted = sorted(registros, key=lambda r: r.get("fecha", ""))
    fechas = [datetime.fromisoformat(r["fecha"]) for r in registros_sorted]
    bmis = [float(r["bmi"]) for r in registros_sorted]
    plt.figure()
    plt.plot(fechas, bmis, marker="o")
    plt.xlabel("Fecha")
    plt.ylabel("BMI")
    plt.title(f"Evolución del BMI para {nombre}")
    plt.gcf().autofmt_xdate()
    tendencia = calcular_tendencia_bmi(registros_sorted)
    plt.tight_layout()
    plt.show()
    print(f"Tendencia para {nombre}: {tendencia}")


def main():
    parser = argparse.ArgumentParser(
        description="Grafica el historial de BMI de un usuario"
    )
    parser.add_argument("nombre", help="Nombre del usuario")
    parser.add_argument(
        "--base-dir", default="registros", help="Directorio con registros"
    )
    args = parser.parse_args()
    plot_historial(args.nombre, args.base_dir)


if __name__ == "__main__":
    main()
