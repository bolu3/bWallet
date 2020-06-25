from account import Account
import funcionesCuentas
import funcionesGenerales
import informacion


def ppal():
    # Main de la app
    accountList = []

    try:
        informacion.abrirCuentas('data.csv', accountList)
    except:
        print("Aun no existen cuentas")
        

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

        quehacer = funcionesGenerales.verificacion("Qué querés hacer?: ")

        if quehacer == 1:
            funcionesCuentas.showAccounts(accountList)
        elif quehacer == 2:
            funcionesCuentas.addAccount(accountList)
        elif quehacer == 3:
            funcionesCuentas.removeAccount(accountList)
        elif quehacer == 4:
            funcionesCuentas.chooseAccount(accountList)
        else:
            print("Numero no válido")


        informacion.guardarCuentas('data.csv',accountList)





ppal()
