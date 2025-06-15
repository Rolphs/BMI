import csv
import matplotlib.pyplot as plt
import plot_bmi_history as ph


def _write_records(path, bmis):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["fecha", "nombre", "peso", "altura", "bmi", "clasificacion"],
        )
        writer.writeheader()
        for i, bmi in enumerate(bmis):
            writer.writerow(
                {
                    "fecha": f"2024-{i+1:02d}-01T00:00:00",
                    "nombre": "Ana",
                    "peso": "70",
                    "altura": "1.70",
                    "bmi": bmi,
                    "clasificacion": "Normal",
                }
            )


import pytest


@pytest.mark.parametrize(
    "bmis, expected",
    [([20, 21], "rising"), ([25, 24], "falling"), ([22, 22.05], "stable")],
)
def test_plot_historial_trend(tmp_path, monkeypatch, capsys, bmis, expected):
    csv_path = tmp_path / "Ana.csv"
    _write_records(csv_path, bmis)
    monkeypatch.setattr(plt, "show", lambda: None)
    ph.plot_historial("Ana", str(tmp_path))
    out = capsys.readouterr().out
    assert f"Tendencia para Ana: {expected}" in out

