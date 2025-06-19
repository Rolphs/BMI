import bmi
import plot_bmi_history as ph
import translations
import pytest


def test_shared_translation_objects():
    assert bmi.MENSAJES is translations.MENSAJES
    assert ph.MENSAJES is translations.MENSAJES


def test_language_switch_affects_both():
    bmi.establecer_idioma("en")
    assert ph.msj("rising") == translations.MENSAJES["en"]["rising"]
    ph.establecer_idioma("es")
    assert bmi.msj("falling") == translations.MENSAJES["es"]["falling"]


def test_invalid_language_raises_error():
    current = translations.msj("titulo")
    with pytest.raises(ValueError):
        translations.establecer_idioma("fr")
    # language should remain unchanged
    assert translations.msj("titulo") == current

