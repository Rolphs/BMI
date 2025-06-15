import bmi


def _patch_base_dir(monkeypatch, tmp_path):
    orig_guardar = bmi.guardar_registro
    orig_cargar = bmi.cargar_historial
    orig_obtener = bmi.obtener_nombres_guardados
    monkeypatch.setattr(
        bmi,
        "guardar_registro",
        lambda n, p, a, b, c, base_dir="registros": orig_guardar(
            n, p, a, b, c, base_dir=str(tmp_path)
        ),
    )
    monkeypatch.setattr(
        bmi,
        "cargar_historial",
        lambda n, base_dir="registros": orig_cargar(n, str(tmp_path))
    )
    monkeypatch.setattr(
        bmi,
        "obtener_nombres_guardados",
        lambda base_dir="registros": orig_obtener(str(tmp_path))
    )
    monkeypatch.setattr(bmi, "limpiar_pantalla", lambda: None)
    monkeypatch.setattr(bmi, "imprimir_tabla_bmi", lambda *a, **k: None)



def test_main_creates_and_loads_records(tmp_path, monkeypatch, capsys):
    _patch_base_dir(monkeypatch, tmp_path)
    # First run as new user
    inputs = iter(["Ana", "70", "1.75", "65", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    bmi.main()
    registros = bmi.cargar_historial("Ana")
    assert len(registros) == 1

    # Second run selecting existing user
    inputs2 = iter(["1", "71", "1.75", "65", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs2))
    bmi.main()
    out = capsys.readouterr().out
    assert "Historial para Ana" in out
