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


def test_main_lang_en_errors(tmp_path, monkeypatch, capsys):
    _patch_ui(monkeypatch)
    inputs = iter([
        "",
        " ",
        "Bob",
        "-1",
        "20",
        "301",
        "abc",
        "70",
        "0",
        "0.4",
        "2.6",
        "no",
        "1.7",
        "65",
        "n",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    bmi.main(["--base-dir", str(tmp_path), "--lang", "en"])
    out = capsys.readouterr().out
    assert "Please enter a non-empty value." in out
    assert "Please enter a positive number greater than zero." in out
    assert "Value must be greater than or equal to 30." in out
    assert "Value must be less than or equal to 300." in out
    assert "Value must be greater than or equal to 0.5." in out
    assert "Value must be less than or equal to 2.5." in out
    assert "Invalid input. Enter a valid number." in out
    bmi.establecer_idioma("es")
