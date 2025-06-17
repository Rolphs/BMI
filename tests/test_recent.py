from datetime import datetime
import plot_bmi_history as ph
import bmi
from bmi import BmiCategory

analizar_registros_recientes = ph.analizar_registros_recientes


def test_analizar_recientes_mejora(capsys, monkeypatch):
    registros = [
        {
            "fecha": "2024-01-01T00:00:00",
            "bmi": 31,
            "clasificacion": BmiCategory.MUY_ALTO,
        },
        {
            "fecha": "2024-01-15T00:00:00",
            "bmi": 29,
            "clasificacion": BmiCategory.ALTO,
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
            "clasificacion": BmiCategory.NORMAL,
        },
        {
            "fecha": "2024-02-01T00:00:00",
            "bmi": 27,
            "clasificacion": BmiCategory.ALTO,
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


def test_analizar_recientes_sin_historial(capsys, monkeypatch):
    monkeypatch.setattr(
        "plot_bmi_history.cargar_historial",
        lambda nombre, base_dir="registros": [],
    )

    class DummyDate(datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2024, 2, 1)

    monkeypatch.setattr(ph, "datetime", DummyDate)
    analizar_registros_recientes("Ana", semanas=8)
    out = capsys.readouterr().out
    assert "No hay historial" in out


def test_analizar_recientes_no_suficientes(capsys, monkeypatch):
    registros = [
        {
            "fecha": "2024-01-01T00:00:00",
            "bmi": 31,
            "clasificacion": BmiCategory.MUY_ALTO,
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
    assert "No hay suficientes registros" in out


def test_main_recent_lang_en(monkeypatch, capsys):
    registros = [
        {
            "fecha": "2024-01-01T00:00:00",
            "bmi": 31,
            "clasificacion": BmiCategory.MUY_ALTO,
        },
        {
            "fecha": "2024-01-15T00:00:00",
            "bmi": 29,
            "clasificacion": BmiCategory.ALTO,
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
    ph.main_recent(["Ana", "--weeks", "8", "--lang", "en"])
    out = capsys.readouterr().out
    assert "improved" in out
    ph.establecer_idioma("es")


def test_main_recent_passes_arguments(monkeypatch):
    captured = {}

    def fake_an(nombre, semanas=4, base_dir="registros"):
        captured["args"] = (nombre, semanas, base_dir)

    monkeypatch.setattr(ph, "analizar_registros_recientes", fake_an)
    ph.main_recent(["Bob", "--weeks", "6", "--base-dir", "foo"])
    assert captured["args"] == ("Bob", 6, "foo")
