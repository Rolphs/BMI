import pytest

from bmi import (
    calcular_bmi,
    clasificar_bmi,
    pedir_cadena_no_vacia,
    calcular_rango_peso_saludable,
)


def test_calcular_bmi_known_values():
    assert calcular_bmi(70, 1.75) == pytest.approx(22.857142857142858)
    assert calcular_bmi(50, 1.6) == pytest.approx(19.53125)


@pytest.mark.parametrize(
    "bmi_value, expected",
    [
        (15.9, "Muy bajo"),
        (16, "Bajo"),
        (18.4, "Bajo"),
        (18.5, "Normal"),
        (24.9, "Normal"),
        (25, "Alto"),
        (29.9, "Alto"),
        (30, "Muy alto"),
    ],
)
def test_clasificar_bmi_boundaries(bmi_value, expected):
    assert clasificar_bmi(bmi_value) == expected


def test_pedir_cadena_no_vacia(monkeypatch):
    respuestas = iter(["", "   ", "Ana"])
    monkeypatch.setattr("builtins.input", lambda _: next(respuestas))
    assert pedir_cadena_no_vacia("nombre") == "Ana"


def test_calcular_rango_peso_saludable():
    peso_min, peso_max = calcular_rango_peso_saludable(1.70)
    assert peso_min == pytest.approx(18.5 * 1.70 ** 2)
    assert peso_max == pytest.approx(24.9 * 1.70 ** 2)
