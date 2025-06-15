import pytest

from plot_bmi_history import calcular_tendencia_bmi


def test_calcular_tendencia_bmi_rising():
    registros = [
        {"fecha": "2024-01-01T00:00:00", "bmi": 20},
        {"fecha": "2024-02-01T00:00:00", "bmi": 21},
    ]
    assert calcular_tendencia_bmi(registros) == "rising"


def test_calcular_tendencia_bmi_falling():
    registros = [
        {"fecha": "2024-01-01T00:00:00", "bmi": 25},
        {"fecha": "2024-02-01T00:00:00", "bmi": 24},
    ]
    assert calcular_tendencia_bmi(registros) == "falling"


def test_calcular_tendencia_bmi_stable():
    registros = [
        {"fecha": "2024-01-01T00:00:00", "bmi": 22},
        {"fecha": "2024-02-01T00:00:00", "bmi": 22.05},
    ]
    assert calcular_tendencia_bmi(registros) == "stable"
