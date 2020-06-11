from account import Account
import funcionesCuentas


def ppal():
    # Main de la app
    accountList = []

    mainMenu(accountList)


def mainMenu(accountList):
    # Es el menu de la app, para ver que acciones realizar
    while True:
        print("=" * 25)
        print("=" * 25)
        print("=" * 25)
        print("Menu  ")
        print("=" * 25)
        print("Ver cuentas [1]")
        print("Agregar Cuenta [2]")
        print("Eliminar Cuenta [3]")
        print("Seleccionar Cuenta [4]")

        quehacer = input("Qué querés hacer?: ")

        if verificacion(quehacer) == 1:
            funcionesCuentas.showAccounts(accountList)
        elif verificacion(quehacer) == 2:
            funcionesCuentas.addAccount(accountList)
        elif verificacion(quehacer) == 3:
            funcionesCuentas.removeAccount(accountList)
        elif verificacion(quehacer) == 4:
            funcionesCuentas.chooseAccount(accountList)
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



ppal()
