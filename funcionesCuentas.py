from account import Account


def showAccounts(accountList):
    if not accountList:
        print('No hay cuentas para mostrar')
    else:
        for x in accountList:
            print(f"Cuenta: {x.name} || Dinero disponible: {x.gastable} || Ahorros: {x.ahorro}.")


def addAccount(accountList):
    name = input('Ingrese alias de nueva cuenta: ')
    account = Account(name)
    accountList.append(account)


def removeAccount(accountList):
    name = input('Ingrese alias de cuenta a eliminar: ')
    i = 0

    for x in accountList:
        if name == x.name:
            accountList.pop(i)
            break
        else:
            i += 1
    if i > (len(accountList) - 1):
        print(f'{name} no se encuentra en la lista')


def chooseAccount(accountList):
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
    centinela = True
    while centinela:
        print('=' * 25)
        print('=' * 25)
        print('=' * 25)
        print(f'Cuenta: {account.name}')
