import bmi


def test_imprimir_tabla_bmi_output(capsys):
    bmi.imprimir_tabla_bmi(22.86, bmi.CAT_NORMAL)
    out = capsys.readouterr().out
    lines = out.splitlines()
    width = 12
    expected_line = "+" + "+".join(["-" * width for _ in range(5)]) + "+"
    assert lines[0] == expected_line
    assert lines[2] == expected_line
    assert lines[4] == expected_line
    highlight = f"\x1b[7m{format(22.86, '.2f').center(width)}\x1b[0m"
    cells = lines[3].split("|")
    assert cells[3] == highlight
