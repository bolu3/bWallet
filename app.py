from account import Account
from menus import mainMenu


def ppal():
    accountList = []
    a1 = Account("Diego")
    accountList.append(a1)
    a2 = Account("Empresa")
    accountList.append(a2)

    for x in accountList:
        print(x.name)
        print(x.ahorro)

    mainMenu()


ppal()
