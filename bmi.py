import os

def limpiar_pantalla():
    """Borra el contenido de la terminal cuando es posible.

    Utiliza ``os.system('cls' if os.name == 'nt' else 'clear')`` para
    realizar la limpieza de forma compatible entre sistemas Windows y UNIX.
    Esta acción puede fallar o no estar permitida en algunos entornos,
    por lo que se considera opcional y su ausencia no afecta al programa.
    """

    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_float_positivo(prompt):
    """Solicita al usuario un número flotante positivo."""
    while True:
        dato = input(prompt)
        try:
            valor = float(dato)
            if valor > 0:
                return valor
            else:
                print("Por favor ingresa un número positivo mayor que cero.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def main():
    """Ejecuta el flujo principal de la aplicación."""
    # Al inicio del programa
    limpiar_pantalla()

    # Pedir peso y talla al usuario
    peso = pedir_float_positivo("¿Cuántos Kilogramos pesas? ")
    altura = pedir_float_positivo("¿Cuánto metros mides? ")

    bmi = calcular_bmi(peso, altura)
    print(f"Tu indice de masa corporal es: {bmi:.2f}")
    clasificacion = clasificar_bmi(bmi)
    print(f"Clasificaci\u00f3n: {clasificacion}")
    imprimir_tabla_bmi(clasificacion)

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


def imprimir_tabla_bmi(clasificacion):
    """Muestra una tabla con el rango destacado correspondiente."""
    categorias = ["Muy bajo", "Bajo", "Normal", "Alto", "Muy alto"]
    ancho = 12
    linea = "+" + "+".join(["-" * ancho for _ in categorias]) + "+"
    encabezado = "|" + "|".join(cat.center(ancho) for cat in categorias) + "|"

    # Construir fila con la categor\u00eda resaltada
    fila = []
    for cat in categorias:
        if cat == clasificacion:
            texto = f"\x1b[7m{cat.center(ancho)}\x1b[0m"  # invert colors
        else:
            texto = " " * ancho
        fila.append(texto)
    fila = "|" + "|".join(fila) + "|"

    print(linea)
    print(encabezado)
    print(linea)
    print(fila)
    print(linea)


if __name__ == "__main__":
    main()
