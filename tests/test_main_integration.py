import bmi


def _patch_ui(monkeypatch):
    monkeypatch.setattr(bmi, "limpiar_pantalla", lambda: None)
    monkeypatch.setattr(bmi, "imprimir_tabla_bmi", lambda *a, **k: None)


def test_main_creates_and_loads_records(tmp_path, monkeypatch, capsys):
    _patch_ui(monkeypatch)
    # First run as new user
    inputs = iter(["Ana", "70", "1.75", "65", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    bmi.main(["--base-dir", str(tmp_path)])
    registros = bmi.cargar_historial("Ana", str(tmp_path))
    assert len(registros) == 1

    # Second run selecting existing user
    inputs2 = iter(["1", "71", "1.75", "65", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs2))
    bmi.main(["--base-dir", str(tmp_path)])
    out = capsys.readouterr().out
    assert "Historial para Ana" in out
