import argparse
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from bmi import (
    cargar_historial,
    CAT_MUY_BAJO,
    CAT_BAJO,
    CAT_NORMAL,
    CAT_ALTO,
    CAT_MUY_ALTO,
)

from translations import MENSAJES, establecer_idioma, msj


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
        print(msj("no_historial", nombre=nombre))
        return

    limite = datetime.now() - timedelta(weeks=semanas)
    recientes = [
        r
        for r in registros
        if datetime.fromisoformat(r["fecha"]) >= limite
    ]
    if len(recientes) < 2:
        print(msj("no_recientes"))
        return

    recientes_sorted = sorted(recientes, key=lambda r: r.get("fecha", ""))
    tendencia = calcular_tendencia_bmi(recientes_sorted)
    primera = recientes_sorted[0]["clasificacion"]
    ultima = recientes_sorted[-1]["clasificacion"]

    orden = [CAT_MUY_BAJO, CAT_BAJO, CAT_NORMAL, CAT_ALTO, CAT_MUY_ALTO]
    idx_primera = orden.index(primera)
    idx_ultima = orden.index(ultima)

    primera_label = msj("cat_" + primera.lower())
    ultima_label = msj("cat_" + ultima.lower())

    if idx_ultima < idx_primera:
        cambio = msj("mejora", primera=primera_label, ultima=ultima_label)
    elif idx_ultima > idx_primera:
        cambio = msj("empeora", primera=primera_label, ultima=ultima_label)
    else:
        cambio = msj("sin_cambio", ultima=ultima_label)

    if tendencia == "rising":
        tendencia_msg = msj("rising")
    elif tendencia == "falling":
        tendencia_msg = msj("falling")
    else:
        tendencia_msg = msj("stable")

    print(
        msj(
            "resumen",
            semanas=semanas,
            tendencia_msg=tendencia_msg,
            cambio=cambio,
        )
    )


def plot_historial(nombre, base_dir="registros"):
    registros = cargar_historial(nombre, base_dir)
    if not registros:
        print(msj("no_historial", nombre=nombre))
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
    print(msj("tendencia_para", nombre=nombre, tendencia=tendencia))


def mostrar_grafica(nombre, base_dir="registros"):
    """Muestra la evolución del BMI en una gráfica.

    This wrapper simply delegates to :func:`plot_historial` so external
    callers can invoke the plotting helper using a Spanish name.
    """

    plot_historial(nombre, base_dir)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Grafica el historial de BMI de un usuario"
    )
    parser.add_argument("nombre", help="Nombre del usuario")
    parser.add_argument(
        "--base-dir", default="registros", help="Directorio con registros"
    )
    parser.add_argument(
        "--lang",
        default="es",
        choices=MENSAJES.keys(),
        help="Idioma de los mensajes",
    )
    args = parser.parse_args(argv)
    establecer_idioma(args.lang)
    plot_historial(args.nombre, args.base_dir)


if __name__ == "__main__":
    main()
