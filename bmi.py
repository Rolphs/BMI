import os

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

def main():
    """Ejecuta el flujo principal de la aplicación."""
    # Al inicio del programa
    limpiar_pantalla()

    # Mostrar cabecera del programa
    print("=" * 40)
    print(" CALCULADORA DE BMI ".center(40))
    print("=" * 40)

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
    imprimir_tabla_bmi(bmi, clasificacion)

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


if __name__ == "__main__":
    main()
