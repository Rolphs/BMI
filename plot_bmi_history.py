import argparse
import matplotlib.pyplot as plt
from datetime import datetime

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
    parser = argparse.ArgumentParser(description="Grafica el historial de BMI de un usuario")
    parser.add_argument("nombre", help="Nombre del usuario")
    parser.add_argument("--base-dir", default="registros", help="Directorio con registros")
    args = parser.parse_args()
    plot_historial(args.nombre, args.base_dir)

if __name__ == "__main__":
    main()
