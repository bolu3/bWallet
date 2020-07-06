from account import Account
import transactions
import csv


def guardarCuentas(nombreArchivo, ListaCuentas):
    # Save data from accounts
    with open(nombreArchivo, 'w', newline='') as archivo:
        archivo_csv = csv.writer(archivo)
        for x in ListaCuentas:
            archivo_csv.writerow([x.name])


def abrirCuentas(nombreArchivo, accountList):
    # Open the existing accounts
    with open('data.csv') as file:
        reader = csv.reader(file)
        item = next(reader, None)

        while item:
            name = str(item[0])
            account = Account(name)
            accountList.append(account)
            item = next(reader, None)


def abrirTransacciones(nombreArchivo, account):
    # Load transaction of a particular account
    with open("%sTransacciones.csv" % account.name) as file:
        reader = csv.reader(file)
        item = next(reader, None)

        while item:
            category = item[0]
            description = item[1]
            amount = int(item[2])
            date = item[3]

            if amount > 0:
                income = transactions.Ingreso(category, description, amount, date)
                account.transaccionList.append(income)
            else:
                expense = transactions.Gasto(category, description, amount, date)
                account.transaccionList.append(expense)

            item = next(reader, None)


def abrirStatus(nombreArchivo, account):
    # Open status of a certain account
    with open(nombreArchivo) as file:
        reader = csv.reader(file)
        status = next(reader, None)
        account.gastable = status[0]
        account.ahorro = status[1]
