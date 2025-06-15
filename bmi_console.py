import argparse
import bmi
import plot_bmi_history as ph

MENU = {
    "es": {
        "title": "MENU PRINCIPAL",
        "option1": "Calcular nuevo BMI",
        "option2": "Ver historial y grafica",
        "option3": "Salir",
        "prompt": "Elige una opcion: ",
    },
    "en": {
        "title": "MAIN MENU",
        "option1": "Calculate new BMI",
        "option2": "View history and graph",
        "option3": "Exit",
        "prompt": "Choose an option: ",
    },
}


def _show_history_and_graph(base_dir):
    nombres = bmi.obtener_nombres_guardados(base_dir)
    nombre = None
    if nombres:
        print(bmi.msj("lista_usuarios"))
        for idx, n in enumerate(nombres, 1):
            print(f" {idx}) {n}")
        print(" 0) Nuevo usuario")
        eleccion = input(bmi.msj("seleccion_usuario"))
        if eleccion.isdigit():
            idx = int(eleccion)
            if 1 <= idx <= len(nombres):
                nombre = nombres[idx - 1]
    if not nombre:
        nombre = bmi.pedir_cadena_no_vacia(bmi.msj("pregunta_nombre"))
    bmi.mostrar_historial(nombre, base_dir)
    ph.plot_historial(nombre, base_dir)


def main(argv=None):
    if argv is None:
        argv = []
    parser = argparse.ArgumentParser(description="BMI console menu")
    parser.add_argument("--lang", default="es", choices=bmi.MENSAJES.keys())
    parser.add_argument("--base-dir", default="registros")
    args = parser.parse_args(argv)

    bmi.establecer_idioma(args.lang)
    ph.establecer_idioma(args.lang)

    msgs = MENU[args.lang]

    while True:
        bmi.limpiar_pantalla()
        print("=" * 40)
        print(msgs["title"].center(40))
        print("=" * 40)
        print(f"1) {msgs['option1']}")
        print(f"2) {msgs['option2']}")
        print(f"3) {msgs['option3']}")
        choice = input(msgs["prompt"]).strip()
        if choice == "1":
            bmi.main(["--base-dir", args.base_dir, "--lang", args.lang])
        elif choice == "2":
            _show_history_and_graph(args.base_dir)
            input("Press Enter to continue...")
        elif choice == "3":
            break
        else:
            print(bmi.msj("error_invalido"))


if __name__ == "__main__":
    main()
