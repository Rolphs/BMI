import os
import csv
from datetime import datetime

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

def main():
    """Ejecuta el flujo principal de la aplicación."""
    while True:
        # Al inicio del programa
        limpiar_pantalla()

        # Mostrar cabecera del programa
        print("=" * 40)
        print(" CALCULADORA DE BMI ".center(40))
        print("=" * 40)

        nombre = pedir_cadena_no_vacia("¿Cómo te llamas? ")
        print(f"Hola, {nombre}!\n")

        # Pedir peso y talla al usuario
        peso = pedir_float_positivo(
            "¿Cuántos Kilogramos pesas? ", min_val=30, max_val=300
        )
        altura = pedir_float_positivo(
            "¿Cuánto metros mides? ", min_val=0.5, max_val=2.5
        )

        print(f"Peso ingresado: {peso} kg")
        print(f"Altura ingresada: {altura} m")

        bmi = calcular_bmi(peso, altura)
        print(f"Tu indice de masa corporal es: {bmi:.2f}")
        clasificacion = clasificar_bmi(bmi)
        print(f"Clasificaci\u00f3n: {clasificacion}")
        consejo = obtener_consejo(clasificacion)
        if consejo:
            print(consejo)
        imprimir_tabla_bmi(bmi, clasificacion)

        peso_min, peso_max = calcular_rango_peso_saludable(altura)
        print(
            f"Para tu altura, un peso entre {peso_min:.1f} kg y {peso_max:.1f} kg es considerado saludable."
        )

        peso_objetivo = pedir_float_positivo(
            "Ingresa un peso objetivo para ver su BMI: ", min_val=30, max_val=300
        )
        bmi_objetivo = calcular_bmi(peso_objetivo, altura)
        print(f"El BMI para {peso_objetivo} kg sería: {bmi_objetivo:.2f}")

        guardar_registro(nombre, peso, altura, bmi, clasificacion)

        repetir = input("¿Deseas calcular otro BMI? [S/N]: ")
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
        "Muy bajo": "Consulta a un profesional para mejorar tu nutrici\u00f3n.",
        "Bajo": "Incluye m\u00e1s calor\u00edas saludables en tu dieta.",
        "Normal": "Contin\u00faa con tu estilo de vida saludable.",
        "Alto": "Aumenta la actividad f\u00edsica y cuida tu alimentaci\u00f3n.",
        "Muy alto": "Busca apoyo m\u00e9dico para reducir tu peso.",
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


def guardar_registro(nombre, peso, altura, bmi, clasificacion, base_dir="registros"):
    """Guarda los datos de la consulta en un archivo CSV.

    El archivo se crea dentro de ``base_dir`` con el nombre del usuario.
    Si el directorio o el archivo no existen, se crean autom\u00e1ticamente.
    """

    os.makedirs(base_dir, exist_ok=True)
    sanitized = "".join(c for c in nombre if c.isalnum() or c in "-_ ").strip().replace(" ", "_")
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


if __name__ == "__main__":
    main()
