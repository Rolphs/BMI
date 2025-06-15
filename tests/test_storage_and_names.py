import pytest
import bmi

from bmi import (
    obtener_nombres_guardados,
    guardar_registro,
    cargar_historial,
    mostrar_historial,
    calcular_rango_peso_saludable,
    sanitize_nombre,
    CAT_NORMAL,
)


def test_obtener_nombres_guardados(tmp_path):
    base = tmp_path
    (base / "juan.csv").write_text("header\n", encoding="utf-8")
    (base / "Ana_Maria.csv").write_text("header\n", encoding="utf-8")
    (base / "otro.txt").write_text("ignored", encoding="utf-8")
    nombres = obtener_nombres_guardados(str(base))
    assert nombres == ["Ana Maria", "juan"]


def test_guardar_y_cargar_registro(tmp_path):
    base = tmp_path
    guardar_registro(
        "Ana Maria",
        70,
        1.75,
        22.86,
        CAT_NORMAL,
        base_dir=str(base),
    )
    archivo = base / "Ana_Maria.csv"
    assert archivo.exists()
    registros = cargar_historial("Ana Maria", str(base))
    assert len(registros) == 1
    r = registros[0]
    assert r["nombre"] == "Ana Maria"
    assert float(r["peso"]) == pytest.approx(70)
    assert float(r["altura"]) == pytest.approx(1.75)
    assert float(r["bmi"]) == pytest.approx(22.86, rel=1e-2)
    assert r["clasificacion"] == CAT_NORMAL


def test_mostrar_historial(capsys, tmp_path):
    base = tmp_path
    guardar_registro(
        "Jose",
        80,
        1.8,
        24.69,
        CAT_NORMAL,
        base_dir=str(base),
    )
    mostrar_historial("Jose", str(base))
    out = capsys.readouterr().out
    assert "Historial para Jose" in out
    assert "Normal" in out


def test_calcular_rango_peso_saludable_custom():
    peso_min, peso_max = calcular_rango_peso_saludable(
        1.8, bmi_min=20, bmi_max=22
    )
    assert peso_min == pytest.approx(20 * 1.8 ** 2)
    assert peso_max == pytest.approx(22 * 1.8 ** 2)


def test_sanitization_consistency(tmp_path, monkeypatch):
    nombre = "  Ju@n _ Lopez!  "
    expected = sanitize_nombre(nombre)

    join_calls = []
    original_join = bmi.os.path.join

    def spy_join(base, fname):
        join_calls.append(fname)
        return original_join(base, fname)

    monkeypatch.setattr(bmi.os.path, "join", spy_join)

    guardar_registro(nombre, 70, 1.75, 22.86, CAT_NORMAL, base_dir=str(tmp_path))
    cargar_historial(nombre, str(tmp_path))

    assert join_calls == [f"{expected}.csv", f"{expected}.csv"]
