import os
import platform

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Al inicio del programa:
limpiar_pantalla()

# Pedir peso y talla al usuario
peso = float (input ("¿Cuántos Kilogramos pesas? "))
altura = float (input ("¿Cuánto metros mides? "))

# Hacer el cálculo
def calcular_bmi (peso, altura):
        return peso / (altura ** 2)
# Calcular el BMI
bmi = calcular_bmi(peso, altura)

# Presentar resultado
print (f"Tu indice de masa corporal es: {bmi:.2f}")
