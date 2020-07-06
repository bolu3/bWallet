from transactions import Ingreso
from transactions import Gasto
from functionsGeneral import verificacion, verificacionFloat
import csv


class Account:
    # Representation of an Account

    def __init__(self, name, savings=0, expendable=0, transaccionList=None):
        # Account constructor

        self.name = name
        self.savings = savings
        self.expendable = expendable
        if transaccionList is None:
            transaccionList = []
        self.transaccionList = transaccionList

    def addGasto(self):
        # Add an expese to a certain account. And process the information

        category = input("Ingrese la categoria del gasto: ")
        description = input("Breve descripcion del gasto: ")
        amount = -verificacion("Monto: ")
        date = verificacion("probando fecha:")

        expense = Gasto(category, description, amount, date)
        self.transaccionList.append(expense)

        self.expendable = int(
            self.expendable)

        self.expendable += amount

        guardarTransacciones("%sTransacciones.csv" % self.name, expense)
        guardarStatus("%sStatus.csv" % self.name, self)

    def addIngreso(self):
        # Add an income

        category = input("Ingrese la categoria del ingreso: ")
        description = input("Breve descripcion del ingreso: ")
        amount = verificacion("Monto: ")
        date = verificacion("probando fecha: ")

        income = Ingreso(category, description, amount, date)
        self.transaccionList.append(income)  # Add income to transaction list

        taxSavings = verificacionFloat("Porcentaje del sueldo a ahorrar: ")
        taxSavings /= 100

        self.savings = int(self.savings)
        self.expendable = int(
            self.expendable)

        self.savings += income.amount * taxSavings
        self.expendable += income.amount * (1 - taxSavings)

        guardarTransacciones("%sTransacciones.csv" % self.name, income)
        guardarStatus("%sStatus.csv" % self.name, self)

    def getName(self):
        return self.name


def guardarTransacciones(nombreArchivo, transaccion):
    # Save transaction in a csv
    with open(nombreArchivo, 'a') as archivo:
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerow((transaccion.category, transaccion.description, transaccion.amount, transaccion.date))


def guardarStatus(nombreArchivo, account):
    # Save status of a certain account
    with open(nombreArchivo, 'w') as file:
        archivo_csv = csv.writer(file)
        archivo_csv.writerow((account.expendable, account.savings))
