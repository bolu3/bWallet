import funcionesCuentas
import funcionesGenerales
import informacion


def ppal():
    # Main de la app
    accountList = []

    try:
        informacion.abrirCuentas('data.csv', accountList)
    except IOError:
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

        # Lista del menu para hacer las diferentes acciones.
        if quehacer == 1:
            funcionesCuentas.showAccounts(accountList)
        elif quehacer == 2:
            funcionesCuentas.addAccount(accountList)
        elif quehacer == 3:
            funcionesCuentas.removeAccount(accountList)
        elif quehacer == 4:
            chooseAccount(accountList)
        else:
            print("Numero no válido")

        informacion.guardarCuentas('data.csv', accountList)


def chooseAccount(accountList):
    # Elegir un cuenta dentro de las que salen de Ver cuentas
    name = input('Cuenta a ingresar: ')
    i = 0
    for x in accountList:
        if name == x.name:
            menuCuenta(x)
        else:
            i += 1
    if i > (len(accountList) - 1):
        print(f'{name} no se encuentra en la lista')


def menuCuenta(account):
    # Este es el menu de inicio de la cuenta. Donde se van a poder ver los ahorras, realizar las diferentes acciones
    # como ingresar gastos e ingresos, y tambien poder elegir el procesamiento de los datos.
    centinela = True

    try:
        informacion.abrirStatus("%sStatus.csv" % account.name, account)
    except IOError:
        print("No se encoentró status actual")

    while centinela:
        print(f"""
        =========================
        =========================
        =========================
        Cuenta: {account.name}
        =========================
        Dinero disponible: {account.gastable}
        Dinero ahorrado: {account.ahorro}
        =========================
        =========================
        Lista de transacciones[1]
        Ingresar Gasto[2]
        Ingresar Ingreso[3]
        Gráficos[4]
        Volver a Lista de Cuentas[5]
        """)

        quehacer = funcionesCuentas.verificacion("Que querés hacer?: ")

        if quehacer == 1:
            funcionesCuentas.showTransaccion(account)
        elif quehacer == 2:
            account.addGasto()
        elif quehacer == 3:
            account.addIngreso()
        # elif quehacer == 4:
        # chooseAccount(account)
        elif quehacer == 5:
            centinela = False
        else:
            print("Numero no válido")

        ppal()


ppal()
