from account import Account


# import app


def mainMenu():
    # Es el menu de la app, para ver que acciones realizar
    while True:
        print("Menu  ")
        print("=" * 25)
        print("Ver cuentas [1]")
        print("Agregar Cuenta [2]")
        print("Eliminar Cuenta [3]")
        print("Seleccionar Cuenta [4]")

        quehacer = input("Qué querés hacer?: ")

        if verificacion(quehacer) == 1:
            showAccounts()
        else:
            print("Numero no válido")


def verificacion(n):
    try:
        return int(n)
    except ValueError:
        print("=" * 25)
        print("=" * 25)
        print("=" * 25)
        print("'{}' no es un valor correcto. ".format(n))


def showAccounts():
    print('Funciona')
    for x in accountList:
        print(x.name)
        print(x.ahorro)
