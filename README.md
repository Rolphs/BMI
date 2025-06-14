# BMI Calculator

This repository contains a simple Python script `bmi.py` that calculates the **Body Mass Index** (BMI). BMI is a ratio of weight to height squared used to determine whether a person has a healthy body weight.

## How the script works

Running the script will prompt you for your weight in kilograms and height in meters (questions are displayed in Spanish). It then computes your BMI, shows the associated classification (e.g. Normal, Alto) and prints a table highlighting your category.

## Prerequisites

- Python 3.6 or later (the script was tested with Python 3.12)

## Usage

From the repository root, execute:

```bash
python bmi.py
```

After entering your weight and height you should see output similar to:

```
¿Cuántos Kilogramos pesas? 70
¿Cuánto metros mides? 1.75
Tu indice de masa corporal es: 22.86
Clasificación: Normal
+------------+------------+------------+------------+------------+
|  Muy bajo  |    Bajo    |   Normal   |    Alto    |  Muy alto  |
+------------+------------+------------+------------+------------+
|            |            |    22.86   |            |            |
+------------+------------+------------+------------+------------+
```

(The highlighted cell uses inverted colours.)

## License

This project is licensed under the [MIT License](LICENSE).

