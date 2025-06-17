# BMI Calculator

[![CI](https://github.com/Rolphs/BMI/actions/workflows/ci.yml/badge.svg)](https://github.com/Rolphs/BMI/actions/workflows/ci.yml)

This repository contains a simple Python script `bmi.py` that calculates the **Body Mass Index** (BMI). BMI is a ratio of weight to height squared used to determine whether a person has a healthy body weight.

## How the script works

When launched, the program looks for CSV files in the ``registros`` directory and lists the stored user names alphabetically. Selecting a number from this list prints the past BMI history for that user. You can also choose ``0`` to start as a new user.

After the selection phase, the script will prompt for your weight in kilograms and height in meters (questions are displayed in Spanish). Values must fall within a sensible range (30–300 kg for weight and 0.5–2.5 m for height). It then computes your BMI, shows the associated classification (e.g. Normal, Alto) and prints a table highlighting your category. Depending on the result, the script also displays a short recommendation. After that the program shows the ideal weight range for the given height and lets you enter a target weight to see its BMI. Each time you complete a calculation the data are stored in a CSV file inside the ``registros`` directory.

## Prerequisites

- Python 3.6 or later (the script was tested with Python 3.12)
 - Dependencies are listed in ``pyproject.toml``. Install them with
   ``pip install .``.  If you want the optional plotting helper make sure to add
   the ``plot`` extra:
   ``pip install .[plot]``.  When running straight from the source you can use
   ``pip install -r requirements.txt`` which already includes this extra.

## Installation

From the repository root you can install the project as a package so the
console scripts are available in your environment:

```bash
pip install .
# install the optional plotting helper with:
pip install .[plot]
```

This will provide the commands ``bmi``, ``plot-bmi-history``, ``bmi-console`` and ``bmi-recent``
which wrap the scripts in this repository.

## Usage

From the repository root, execute the ``bmi`` command (installed via
``pip install .``).  A ``--lang`` flag lets you switch between
Spanish (default) and English. Use ``--base-dir`` to select where CSV
records are stored (default is ``registros``):

```bash
bmi --lang en
```

After entering your name, weight and height you should see output similar to:

```
¿Cómo te llamas? Tania
Hola, Tania!
¿Cuántos Kilogramos pesas? 70
¿Cuánto metros mides? 1.75
Tu indice de masa corporal es: 22.86
Clasificación: Normal
+------------+------------+------------+------------+------------+
|  Muy bajo  |    Bajo    |   Normal   |    Alto    |  Muy alto  |
+------------+------------+------------+------------+------------+
|            |            |    22.86   |            |            |
+------------+------------+------------+------------+------------+
Para tu altura, un peso entre 56.7 kg y 76.3 kg es considerado saludable.
Ingresa un peso objetivo para ver su BMI: 65
El BMI para 65 kg sería: 21.25
```

(The highlighted cell uses inverted colours.)

All completed calculations are appended to ``registros/<tu_nombre>.csv`` so you can keep track of your history. The directory can be changed with the ``--base-dir`` flag.

### Menu mode

You can launch a simple interactive menu with ``bmi-console`` which
allows you to calculate a new BMI or view the stored history and graph
for a user.

```bash
bmi-console --lang en
```

## Running tests

Before invoking the test suite make sure the dependencies are installed.  You
can either install the project in editable mode or use the provided
``requirements.txt`` file:

```bash
pip install .[plot]
# or
pip install -r requirements.txt
```

After that simply run ``pytest`` from the repository root.  The suite adjusts
``sys.path`` automatically so running ``pytest`` directly works without using
``python -m``.  The optional ``plot`` extra installs ``matplotlib`` so the
plot-related tests can run.

```bash
pytest
```


## License

This project is licensed under the [MIT License](LICENSE).


## Plotting BMI history

A helper script ``plot_bmi_history.py`` reads the CSV file for a user and
plots their BMI values over time using ``matplotlib``. After installation you
can launch it with the ``plot-bmi-history`` command. The plot displays the
evolution and prints whether the trend is ``rising``, ``falling`` or ``stable``
based on the first and last stored BMI values. Run it with:

```bash
plot-bmi-history <nombre>
```
You can add ``--lang en`` to show the output in English.

Install the project with ``pip install .[plot]`` so ``matplotlib`` is available
to display the graph.

## Analyzing recent history

The helper module also provides ``analizar_registros_recientes`` which inspects
the last few weeks of stored data. It prints whether your BMI is rising,
falling or stable and reports any change in BMI classification.

After installation you can invoke it directly with ``bmi-recent``:

```bash
bmi-recent Tania --weeks 8 --lang en
```

## Contributing

Optional development dependencies:

- pytest
- pytest-cov
- flake8 (run `flake8` to check code style)

### Continuous integration

This repository uses GitHub Actions to run `flake8` and `pytest` on every push.
You can run the same checks locally with:

```bash
pip install -r requirements.txt flake8 pytest
flake8
pytest
```
