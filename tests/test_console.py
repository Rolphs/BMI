import bmi_console as bc


def _patch_common(monkeypatch):
    monkeypatch.setattr(bc.bmi, "limpiar_pantalla", lambda: None)
    monkeypatch.setattr(bc.ph, "establecer_idioma", lambda *a, **k: None)


def test_show_history_select_existing(monkeypatch):
    _patch_common(monkeypatch)
    monkeypatch.setattr(
        bc.bmi,
        "obtener_nombres_guardados",
        lambda base: ["Ana"],
    )
    monkeypatch.setattr(bc.bmi, "msj", lambda k: k)
    monkeypatch.setattr("builtins.input", lambda _: "1")
    calls = []
    monkeypatch.setattr(
        bc.bmi,
        "mostrar_historial",
        lambda n, b: calls.append(("hist", n, b)),
    )
    monkeypatch.setattr(
        bc.ph,
        "plot_historial",
        lambda n, b: calls.append(("plot", n, b)),
    )
    bc._show_history_and_graph("base")
    assert calls == [("hist", "Ana", "base"), ("plot", "Ana", "base")]


def test_show_history_new_user(monkeypatch):
    _patch_common(monkeypatch)
    monkeypatch.setattr(
        bc.bmi,
        "obtener_nombres_guardados",
        lambda base: ["Ana"],
    )
    monkeypatch.setattr(bc.bmi, "msj", lambda k: k)
    inputs = iter(["0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(bc.bmi, "pedir_cadena_no_vacia", lambda prompt: "Bob")
    calls = []
    monkeypatch.setattr(
        bc.bmi,
        "mostrar_historial",
        lambda n, b: calls.append(("hist", n, b)),
    )
    monkeypatch.setattr(
        bc.ph,
        "plot_historial",
        lambda n, b: calls.append(("plot", n, b)),
    )
    bc._show_history_and_graph("base")
    assert calls == [("hist", "Bob", "base"), ("plot", "Bob", "base")]


def test_main_menu_calls_actions(monkeypatch, tmp_path):
    _patch_common(monkeypatch)
    calls = []
    monkeypatch.setattr(
        bc.bmi,
        "main",
        lambda args: calls.append(("main", args)),
    )
    monkeypatch.setattr(
        bc,
        "_show_history_and_graph",
        lambda base: calls.append(("hist", base)),
    )
    inputs = iter(["1", "2", "", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    bc.main(["--base-dir", str(tmp_path), "--lang", "en"])
    assert calls == [
        ("main", ["--base-dir", str(tmp_path), "--lang", "en"]),
        ("hist", str(tmp_path)),
    ]
