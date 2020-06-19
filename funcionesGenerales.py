def verificacion(prompt):
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
