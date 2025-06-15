import os
import csv
import argparse
import sys
from datetime import datetime


MENSAJES = {
    "es": {
        "titulo": "CALCULADORA DE BMI",
        "lista_usuarios": "Usuarios con historial registrado:",
        "seleccion_usuario": "Selecciona un usuario por número o 0 para nuevo: ",
        "sin_registros": "No hay registros previos.\n",
        "historial_para": "Historial para {nombre}:",
        "pregunta_nombre": "¿Cómo te llamas? ",
        "saludo": "Hola, {nombre}!\n",
        "pregunta_peso": "¿Cuántos Kilogramos pesas? ",
        "pregunta_altura": "¿Cuánto metros mides? ",
        "peso_ingresado": "Peso ingresado: {peso} kg",
        "altura_ingresada": "Altura ingresada: {altura} m",
        "tu_bmi": "Tu indice de masa corporal es: {bmi:.2f}",
        "clasificacion": "Clasificación: {clasificacion}",
        "rango_saludable": (
            "Para tu altura, un peso entre {peso_min:.1f} kg y {peso_max:.1f} kg es considerado saludable."
        ),
        "pregunta_objetivo": "Ingresa un peso objetivo para ver su BMI: ",
        "bmi_objetivo": "El BMI para {peso_objetivo} kg sería: {bmi_objetivo:.2f}",
        "repetir": "¿Deseas calcular otro BMI? [S/N]: ",
    },
    "en": {
        "titulo": "BMI CALCULATOR",
        "lista_usuarios": "Users with stored history:",
        "seleccion_usuario": "Select a user by number or 0 for new: ",
        "sin_registros": "No previous records.\n",
        "historial_para": "History for {nombre}:",
        "pregunta_nombre": "What's your name? ",
        "saludo": "Hello, {nombre}!\n",
        "pregunta_peso": "How many kilograms do you weigh? ",
        "pregunta_altura": "How tall are you in meters? ",
        "peso_ingresado": "Weight entered: {peso} kg",
        "altura_ingresada": "Height entered: {altura} m",
        "tu_bmi": "Your Body Mass Index is: {bmi:.2f}",
        "clasificacion": "Classification: {clasificacion}",
        "rango_saludable": (
            "For your height, a weight between {peso_min:.1f} kg and {peso_max:.1f} kg is considered healthy."
        ),
        "pregunta_objetivo": "Enter a target weight to see its BMI: ",
        "bmi_objetivo": "The BMI for {peso_objetivo} kg would be: {bmi_objetivo:.2f}",
        "repetir": "Calculate another BMI? [Y/N]: ",
    },
}

_IDIOMA = "es"


def establecer_idioma(idioma):
    """Configura el idioma para los mensajes de la aplicación."""

    global _IDIOMA
    if idioma in MENSAJES:
        _IDIOMA = idioma


def msj(clave, **kwargs):
    """Devuelve el mensaje traducido para la clave dada."""

    return MENSAJES[_IDIOMA][clave].format(**kwargs)


def limpiar_pantalla():
    """Borra el contenido de la terminal cuando es posible.

    Utiliza ``os.system('cls' if os.name == 'nt' else 'clear')`` para
    realizar la limpieza de forma compatible entre sistemas Windows y UNIX.
    Esta acción puede fallar o no estar permitida en algunos entornos,
    por lo que se considera opcional y su ausencia no afecta al programa.
    """

    os.system('cls' if os.name == 'nt' else 'clear')


def pedir_float_positivo(prompt, min_val=None, max_val=None):
    """Solicita al usuario un número flotante positivo.

    Si ``min_val`` o ``max_val`` se proporcionan, el valor ingresado debe
    encontrarse dentro de ese rango (inclusive). En caso contrario se
    mostrar\u00e1 un mensaje explicativo y se pedir\u00e1 nuevamente.
    """
    while True:
        dato = input(prompt)
        try:
            valor = float(dato)
            if valor <= 0:
                print("Por favor ingresa un número positivo mayor que cero.")
                continue
            if min_val is not None and valor < min_val:
                print(f"El valor debe ser mayor o igual que {min_val}.")
                continue
            if max_val is not None and valor > max_val:
                print(f"El valor debe ser menor o igual que {max_val}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")


def pedir_cadena_no_vacia(prompt):
    """Solicita al usuario una cadena no vacía."""
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("Por favor ingresa un valor no vacío.")


def obtener_nombres_guardados(base_dir="registros"):
    """Devuelve una lista de nombres con registros guardados.

    Los nombres se devuelven ordenados alfabéticamente.
    """
    if not os.path.isdir(base_dir):
        return []
    nombres = []
    for archivo in os.listdir(base_dir):
        if archivo.lower().endswith(".csv"):
            nombre = os.path.splitext(archivo)[0].replace("_", " ")
            nombres.append(nombre)
    nombres.sort(key=lambda n: n.lower())
    return nombres


def cargar_historial(nombre, base_dir="registros"):
    """Carga el historial de un usuario y devuelve una lista de registros."""
    sanitized = "".join(
        c for c in nombre if c.isalnum() or c in "-_ "
    ).strip().replace(" ", "_")
    archivo = os.path.join(base_dir, f"{sanitized}.csv")
    if not os.path.exists(archivo):
        return []
    with open(archivo, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def mostrar_historial(nombre, base_dir="registros"):
    """Muestra por pantalla el historial de un usuario si existe."""
    registros = cargar_historial(nombre, base_dir)
    if not registros:
        print(msj("sin_registros"))
        return
    print(msj("historial_para", nombre=nombre))
    for reg in registros:
        fecha = reg.get("fecha", "-")
        bmi = reg.get("bmi", "-")
        clasificacion = reg.get("clasificacion", "-")
        print(f" {fecha} -> BMI {bmi} ({clasificacion})")
    print()


def main(argv=None):
    """Ejecuta el flujo principal de la aplicación."""

    if argv is None:
        argv = []

    parser = argparse.ArgumentParser(description="Calcula el BMI")
    parser.add_argument(
        "--lang",
        default="es",
        choices=MENSAJES.keys(),
        help="Selecciona el idioma de la interfaz",
    )
    parser.add_argument(
        "--base-dir",
        default="registros",
        help="Directorio base para guardar registros",
    )
    args = parser.parse_args(argv)
    establecer_idioma(args.lang)

    while True:
        # Al inicio del programa
        limpiar_pantalla()

        # Mostrar cabecera del programa
        print("=" * 40)
        print(msj("titulo").center(40))
        print("=" * 40)

        nombres = obtener_nombres_guardados(args.base_dir)
        nombre = None
        if nombres:
            print(msj("lista_usuarios"))
            for idx, n in enumerate(nombres, 1):
                print(f" {idx}) {n}")
            print(" 0) Nuevo usuario")
            eleccion = input(msj("seleccion_usuario"))
            if eleccion.isdigit():
                idx = int(eleccion)
                if 1 <= idx <= len(nombres):
                    nombre = nombres[idx - 1]
                    mostrar_historial(nombre, args.base_dir)
        if not nombre:
            nombre = pedir_cadena_no_vacia(msj("pregunta_nombre"))
        print(msj("saludo", nombre=nombre))

        # Pedir peso y talla al usuario
        peso = pedir_float_positivo(
            msj("pregunta_peso"), min_val=30, max_val=300
        )
        altura = pedir_float_positivo(
            msj("pregunta_altura"), min_val=0.5, max_val=2.5
        )

        print(msj("peso_ingresado", peso=peso))
        print(msj("altura_ingresada", altura=altura))

        bmi = calcular_bmi(peso, altura)
        print(msj("tu_bmi", bmi=bmi))
        clasificacion = clasificar_bmi(bmi)
        print(msj("clasificacion", clasificacion=clasificacion))
        consejo = obtener_consejo(clasificacion)
        if consejo:
            print(consejo)
        imprimir_tabla_bmi(bmi, clasificacion)

        peso_min, peso_max = calcular_rango_peso_saludable(altura)
        print(msj("rango_saludable", peso_min=peso_min, peso_max=peso_max))

        peso_objetivo = pedir_float_positivo(
            msj("pregunta_objetivo"),
            min_val=30,
            max_val=300,
        )
        bmi_objetivo = calcular_bmi(peso_objetivo, altura)
        print(msj("bmi_objetivo", peso_objetivo=peso_objetivo, bmi_objetivo=bmi_objetivo))

        guardar_registro(
            nombre,
            peso,
            altura,
            bmi,
            clasificacion,
            args.base_dir,
        )

        repetir = input(msj("repetir"))
        if repetir.strip().lower().startswith("n"):
            break


def calcular_bmi(peso, altura):
    """Calcula el índice de masa corporal."""
    return peso / (altura ** 2)


def clasificar_bmi(bmi):
    """Devuelve una clasificaci\u00f3n textual seg\u00fan el BMI."""
    if bmi < 16:
        return "Muy bajo"
    elif bmi < 18.5:
        return "Bajo"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Alto"
    else:
        return "Muy alto"


def obtener_consejo(clasificacion):
    """Devuelve un breve consejo seg\u00fan la clasificaci\u00f3n del BMI."""
    mensajes = {
        "Muy bajo": (
            "Consulta a un profesional para mejorar tu nutrición."
        ),
        "Bajo": "Incluye más calorías saludables en tu dieta.",
        "Normal": "Continúa con tu estilo de vida saludable.",
        "Alto": (
            "Aumenta la actividad física y cuida tu alimentación."
        ),
        "Muy alto": "Busca apoyo médico para reducir tu peso.",
    }
    return mensajes.get(clasificacion, "")


def imprimir_tabla_bmi(bmi, clasificacion):
    """Muestra una tabla con el BMI dentro del rango destacado."""
    categorias = ["Muy bajo", "Bajo", "Normal", "Alto", "Muy alto"]
    ancho = 12
    linea = "+" + "+".join(["-" * ancho for _ in categorias]) + "+"
    encabezado = "|" + "|".join(cat.center(ancho) for cat in categorias) + "|"

    # Construir fila con el BMI en la categor\u00eda correspondiente
    fila = []
    for cat in categorias:
        if cat == clasificacion:
            texto = f"\x1b[7m{format(bmi, '.2f').center(ancho)}\x1b[0m"
        else:
            texto = " " * ancho
        fila.append(texto)
    fila = "|" + "|".join(fila) + "|"

    print(linea)
    print(encabezado)
    print(linea)
    print(fila)
    print(linea)


def calcular_rango_peso_saludable(altura, bmi_min=18.5, bmi_max=24.9):
    """Devuelve el rango de peso saludable para la altura dada."""
    peso_min = bmi_min * altura ** 2
    peso_max = bmi_max * altura ** 2
    return peso_min, peso_max


def guardar_registro(
    nombre,
    peso,
    altura,
    bmi,
    clasificacion,
    base_dir="registros",
):
    """Guarda los datos de la consulta en un archivo CSV.

    El archivo se crea dentro de ``base_dir`` con el nombre del usuario.
    Si el directorio o el archivo no existen, se crean autom\u00e1ticamente.
    """

    os.makedirs(base_dir, exist_ok=True)
    sanitized = "".join(
        c for c in nombre if c.isalnum() or c in "-_ "
    ).strip().replace(" ", "_")
    if not sanitized:
        sanitized = "usuario"
    archivo = os.path.join(base_dir, f"{sanitized}.csv")

    escribir_encabezado = not os.path.exists(archivo)

    with open(archivo, "a", newline="", encoding="utf-8") as f:
        campos = ["fecha", "nombre", "peso", "altura", "bmi", "clasificacion"]
        writer = csv.DictWriter(f, fieldnames=campos)
        if escribir_encabezado:
            writer.writeheader()
        writer.writerow(
            {
                "fecha": datetime.now().isoformat(timespec="seconds"),
                "nombre": nombre,
                "peso": peso,
                "altura": altura,
                "bmi": round(bmi, 2),
                "clasificacion": clasificacion,
            }
        )


def main_cli():
    """Punto de entrada cuando se invoca como script."""

    main(sys.argv[1:])


if __name__ == "__main__":
    main_cli()
