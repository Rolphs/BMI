from datetime import datetime
import plot_bmi_history as ph
import bmi

analizar_registros_recientes = ph.analizar_registros_recientes


def test_analizar_recientes_mejora(capsys, monkeypatch):
    registros = [
        {
            "fecha": "2024-01-01T00:00:00",
            "bmi": 31,
            "clasificacion": bmi.CAT_MUY_ALTO,
        },
        {
            "fecha": "2024-01-15T00:00:00",
            "bmi": 29,
            "clasificacion": bmi.CAT_ALTO,
        },
    ]
    monkeypatch.setattr(
        "plot_bmi_history.cargar_historial",
        lambda nombre, base_dir="registros": registros,
    )

    class DummyDate(datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2024, 2, 1)

    monkeypatch.setattr(ph, "datetime", DummyDate)
    analizar_registros_recientes("Ana", semanas=8)
    out = capsys.readouterr().out
    assert "mejor\u00f3" in out


def test_analizar_recientes_empeora(capsys, monkeypatch):
    registros = [
        {
            "fecha": "2024-01-01T00:00:00",
            "bmi": 22,
            "clasificacion": bmi.CAT_NORMAL,
        },
        {
            "fecha": "2024-02-01T00:00:00",
            "bmi": 27,
            "clasificacion": bmi.CAT_ALTO,
        },
    ]
    monkeypatch.setattr(
        "plot_bmi_history.cargar_historial",
        lambda nombre, base_dir="registros": registros,
    )

    class DummyDate(datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2024, 2, 2)

    monkeypatch.setattr(ph, "datetime", DummyDate)
    analizar_registros_recientes("Ana", semanas=8)
    out = capsys.readouterr().out
    assert "empeor\u00f3" in out
