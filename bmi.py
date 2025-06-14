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

def calcular_bmi(peso, altura):
    """Calcula el índice de masa corporal."""
    return peso / (altura ** 2)


if __name__ == "__main__":
    main()
