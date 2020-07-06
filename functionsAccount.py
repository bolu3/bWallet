from account import Account
from funcionesGenerales import verificacion

import informacion


def showAccounts(accountList):
    # Function used to read current accounts.
    if not accountList:
        print('No hay cuentas para mostrar')
    else:
        for x in accountList:
            print(f"Cuenta: {x.name} ")


def addAccount(accountList):
    # Add an account to the account list.
    name = input('Ingrese alias de nueva cuenta: ')
    account = Account(name)
    accountList.append(account)


def removeAccount(accountList):
    # Remove an account of the account list (The account name must exist)
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


def showTransaccion(account):
    # Show transactions list of a specific account
    informacion.abrirTransacciones("%sTransacciones.csv" % account.name, account)
    for x in account.transaccionList:
        print(f"""
        {x.categoria} || $ {x.monto} || {x.descripcion}  || {x.fecha}
        """)
