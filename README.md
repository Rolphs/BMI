# BMI Calculator

This repository contains a simple Python script `bmi.py` that calculates the **Body Mass Index** (BMI). BMI is a ratio of weight to height squared used to determine whether a person has a healthy body weight.

## How the script works

When launched, the program looks for CSV files in the ``registros`` directory and lists the stored user names alphabetically. Selecting a number from this list prints the past BMI history for that user. You can also choose ``0`` to start as a new user.

After the selection phase, the script will prompt for your weight in kilograms and height in meters (questions are displayed in Spanish). Values must fall within a sensible range (30–300 kg for weight and 0.5–2.5 m for height). It then computes your BMI, shows the associated classification (e.g. Normal, Alto) and prints a table highlighting your category. Depending on the result, the script also displays a short recommendation. After that the program shows the ideal weight range for the given height and lets you enter a target weight to see its BMI. Each time you complete a calculation the data are stored in a CSV file inside the ``registros`` directory.

## Prerequisites

- Python 3.6 or later (the script was tested with Python 3.12)

## Usage

From the repository root, execute:

```bash
python bmi.py
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

All completed calculations are appended to ``registros/<tu_nombre>.csv`` so you can keep track of your history.

## Running tests

To run the unit tests, install `pytest` and execute the command from the
repository root.  The test suite adjusts `sys.path` automatically so running
`pytest` directly works without using `python -m`:

```bash
pytest
```


## License

This project is licensed under the [MIT License](LICENSE).

