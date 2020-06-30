from account import Account
from funcionesGenerales import verificacion

import informacion


def showAccounts(accountList):
    # Funciñon para leer las cuentas. No necesita leer el archivo donde se guardan las cuentas, ya que al iniciarse
    # el programa se cargan las cuentas conlos datos pertinentes.
    if not accountList:
        print('No hay cuentas para mostrar')
    else:
        for x in accountList:
            print(f"Cuenta: {x.name} ")


def addAccount(accountList):
    # Agregar una cuenta a la lista de cuentas.
    name = input('Ingrese alias de nueva cuenta: ')
    account = Account(name)
    accountList.append(account)


def removeAccount(accountList):
    # Remover una cuenta(elegida por el usuario) de la lista de cuentas.
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
    # Mostrar la lista de Transacciones de dicha cuenta
    informacion.abrirTransacciones("%sTransacciones.csv" % account.name, account)
    for x in account.transaccionList:
        print(f"""
        {x.categoria} || $ {x.monto} || {x.descripcion}  || {x.fecha}
        """)
