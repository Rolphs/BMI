import os
import platform

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

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

# Al inicio del programa
limpiar_pantalla()

# Pedir peso y talla al usuario
peso = pedir_float_positivo("¿Cuántos Kilogramos pesas? ")
altura = pedir_float_positivo("¿Cuánto metros mides? ")

def calcular_bmi(peso, altura):
    """Calcula el índice de masa corporal."""
    return peso / (altura ** 2)

# Calcular el BMI
bmi = calcular_bmi(peso, altura)

# Presentar resultado
print(f"Tu indice de masa corporal es: {bmi:.2f}")
