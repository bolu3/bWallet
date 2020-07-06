import information
from account import Account


def showAccounts(accountList):
    # Function used to read current accounts.
    if not accountList:
        print('No accounts to show')
    else:
        for x in accountList:
            print(f"Account: {x.name} ")


def addAccount(accountList):
    # Add an account to the account list.
    name = input('New accounts name: ')
    account = Account(name)
    accountList.append(account)


def removeAccount(accountList):
    # Remove an account of the account list (The account name must exist)
    name = input('Name of account to remove: ')
    i = 0

    for x in accountList:
        if name == x.name:
            accountList.pop(i)
            break
        else:
            i += 1
    if i > (len(accountList) - 1):
        print(f'{name} is not in the list.')


def showTransaccion(account):
    # Show transactions list of a specific account
    information.abrirTransacciones("%sTransacciones.csv" % account.name, account)
    for x in account.transaccionList:
        print(f"""
        {x.category} || $ {x.amount} || {x.description}  || {x.date}
        """)
