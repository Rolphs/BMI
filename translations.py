# -*- coding: utf-8 -*-
"""Shared translations and language helpers for the BMI scripts."""

MENSAJES = {
    "es": {
        # bmi.py messages
        "titulo": "CALCULADORA DE BMI",
        "lista_usuarios": "Usuarios con historial registrado:",
        "seleccion_usuario": (
            "Selecciona un usuario por número o 0 para nuevo: "
        ),
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
            "Para tu altura, un peso entre {peso_min:.1f} kg y "
            "{peso_max:.1f} kg es considerado saludable."
        ),
        "pregunta_objetivo": "Ingresa un peso objetivo para ver su BMI: ",
        "bmi_objetivo": (
            "El BMI para {peso_objetivo} kg sería: {bmi_objetivo:.2f}"
        ),
        "repetir": "¿Deseas calcular otro BMI? [S/N]: ",
        "error_positivo": (
            "Por favor ingresa un número positivo mayor que cero."
        ),
        "error_minimo": "El valor debe ser mayor o igual que {min_val}.",
        "error_maximo": "El valor debe ser menor o igual que {max_val}.",
        "error_invalido": "Entrada inválida. Ingresa un número válido.",
        "error_vacio": "Por favor ingresa un valor no vacío.",
        # Categorías y consejos
        "cat_muy_bajo": "Muy bajo",
        "cat_bajo": "Bajo",
        "cat_normal": "Normal",
        "cat_alto": "Alto",
        "cat_muy_alto": "Muy alto",
        "adv_muy_bajo": "Consulta a un profesional para mejorar tu nutrición.",
        "adv_bajo": "Incluye más calorías saludables en tu dieta.",
        "adv_normal": "Continúa con tu estilo de vida saludable.",
        "adv_alto": "Aumenta la actividad física y cuida tu alimentación.",
        "adv_muy_alto": "Busca apoyo médico para reducir tu peso.",
        # plot_bmi_history messages
        "no_historial": "No hay historial para {nombre}",
        "no_recientes": (
            "No hay suficientes registros recientes para analizar."
        ),
        "tendencia_para": "Tendencia para {nombre}: {tendencia}",
        "rising": "tu BMI está subiendo",
        "falling": "tu BMI está bajando",
        "stable": "tu BMI se mantiene estable",
        "resumen": (
            "En las últimas {semanas} semanas {tendencia_msg} y tu "
            "clasificación {cambio}"
        ),
        "mejora": "mejoró (de {primera} a {ultima}). ¡Buen trabajo!",
        "empeora": (
            "empeoró (de {primera} a {ultima}). "
            "Revisa tu alimentación y actividad física."
        ),
        "sin_cambio": "se mantiene en {ultima}.",
    },
    "en": {
        # bmi.py messages
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
            "For your height, a weight between {peso_min:.1f} kg and "
            "{peso_max:.1f} kg is considered healthy."
        ),
        "pregunta_objetivo": "Enter a target weight to see its BMI: ",
        "bmi_objetivo": (
            "The BMI for {peso_objetivo} kg would be: {bmi_objetivo:.2f}"
        ),
        "repetir": "Calculate another BMI? [Y/N]: ",
        "error_positivo": "Please enter a positive number greater than zero.",
        "error_minimo": "Value must be greater than or equal to {min_val}.",
        "error_maximo": "Value must be less than or equal to {max_val}.",
        "error_invalido": "Invalid input. Enter a valid number.",
        "error_vacio": "Please enter a non-empty value.",
        # Categories and advice
        "cat_muy_bajo": "Very low",
        "cat_bajo": "Low",
        "cat_normal": "Normal",
        "cat_alto": "High",
        "cat_muy_alto": "Very high",
        "adv_muy_bajo": "Consult a professional to improve your nutrition.",
        "adv_bajo": "Include more healthy calories in your diet.",
        "adv_normal": "Keep up your healthy lifestyle.",
        "adv_alto": "Increase physical activity and watch your diet.",
        "adv_muy_alto": "Seek medical support to reduce your weight.",
        # plot_bmi_history messages
        "no_historial": "No history for {nombre}",
        "no_recientes": "Not enough recent records to analyze.",
        "tendencia_para": "Trend for {nombre}: {tendencia}",
        "rising": "your BMI is going up",
        "falling": "your BMI is going down",
        "stable": "your BMI is stable",
        "resumen": (
            "In the last {semanas} weeks {tendencia_msg} and your "
            "classification {cambio}"
        ),
        "mejora": "improved (from {primera} to {ultima}). Great job!",
        "empeora": (
            "worsened (from {primera} to {ultima}). "
            "Check your diet and exercise."
        ),
        "sin_cambio": "remains {ultima}.",
    },
}

_IDIOMA = "es"


def establecer_idioma(idioma):
    """Set the active language if available."""
    global _IDIOMA
    if idioma in MENSAJES:
        _IDIOMA = idioma


def msj(clave, **kwargs):
    """Return the translated message for ``clave``."""
    return MENSAJES[_IDIOMA][clave].format(**kwargs)
