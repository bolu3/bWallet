import functionsAccount
import functionsGeneral
import information


def ppal():
    # Apps main
    accountList = []

    try:
        information.abrirCuentas('data.csv', accountList)
    except IOError:
        print("Aun no existen cuentas")

    mainMenu(accountList)


def mainMenu(accountList):
    # Main menu
    while True:
        print("=" * 25)
        print("=" * 25)
        print("=" * 25)
        print("Menu  ")
        print("=" * 25)
        print("Accounts [1]")
        print("Add Account [2]")
        print("Remove Account [3]")
        print("Select Account [4]")

        whatToDo = functionsGeneral.verificacion("Next Step?: ")

        # Lista del menu para hacer las diferentes acciones.
        if whatToDo == 1:
            functionsAccount.showAccounts(accountList)
        elif whatToDo == 2:
            functionsAccount.addAccount(accountList)
        elif whatToDo == 3:
            functionsAccount.removeAccount(accountList)
        elif whatToDo == 4:
            chooseAccount(accountList)
        else:
            print("Non valid number")

        information.guardarCuentas('data.csv', accountList)


def chooseAccount(accountList):
    # Choose an account, inside accountlist[]
    name = input('Account: ')
    i = 0
    for x in accountList:
        if name == x.name:
            menuCuenta(x)
        else:
            i += 1
    if i > (len(accountList) - 1):
        print(f'{name} does not exist.')


def menuCuenta(account):
    # Menu of a particular account.
    centinela = True

    try:
        information.abrirStatus("%sStatus.csv" % account.name, account)
    except IOError:
        print("No current status")

    while centinela:
        print(f"""
        =========================
        =========================
        =========================
        Account: {account.name}
        =========================
        Expendable: {account.expendable}
        Savings: {account.savings}
        =========================
        =========================
        Transaction List[1]
        Add Expense[2]
        Add income[3]
        Graphics[4]
        Back to Account Menu[5]
        """)

        whatToDo = functionsGeneral.verificacion("Next Step?: ")

        if whatToDo == 1:
            functionsAccount.showTransaccion(account)
        elif whatToDo == 2:
            account.addGasto()
        elif whatToDo == 3:
            account.addIngreso()
        # elif quehacer == 4:
        # chooseAccount(account)
        elif whatToDo == 5:
            centinela = False
        else:
            print("Non valid number")

    ppal()


ppal()
