import pytest
import bmi

from bmi import (
    calcular_bmi,
    clasificar_bmi,
    pedir_cadena_no_vacia,
    calcular_rango_peso_saludable,
    calcular_bmi_para_usuario,
    BmiCategory,
)


def test_calcular_bmi_known_values():
    assert calcular_bmi(70, 1.75) == pytest.approx(22.857142857142858)
    assert calcular_bmi(50, 1.6) == pytest.approx(19.53125)


@pytest.mark.parametrize(
    "bmi_value, expected",
    [
        (15.9, BmiCategory.MUY_BAJO),
        (16, BmiCategory.BAJO),
        (18.4, BmiCategory.BAJO),
        (18.5, BmiCategory.NORMAL),
        (24.9, BmiCategory.NORMAL),
        (25, BmiCategory.ALTO),
        (29.9, BmiCategory.ALTO),
        (30, BmiCategory.MUY_ALTO),
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


def test_calcular_bmi_para_usuario(tmp_path, monkeypatch):
    inputs = iter(["70", "1.75", "65"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("bmi.imprimir_tabla_bmi", lambda *a, **k: None)
    bmi_val, clasif = calcular_bmi_para_usuario("Ana", base_dir=str(tmp_path))
    assert bmi_val == pytest.approx(22.8571, rel=1e-3)
    assert clasif == BmiCategory.NORMAL
    registros = bmi.cargar_historial("Ana", str(tmp_path))
    assert len(registros) == 1
