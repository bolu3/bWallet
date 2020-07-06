def verificacion(prompt):
    # Int verification fucntions
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("No es un valor correcto. ")
            print("=" * 25)
            print("=" * 25)
            print("=" * 25)
            continue
        return value


def verificacionFloat(prompt):
    # Float verifcation function
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("No es un valor correcto. ")
            print("=" * 25)
            print("=" * 25)
            print("=" * 25)
            continue
        return value
