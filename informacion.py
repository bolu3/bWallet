from account import Account
import csv

def guardarCuentas(nombreArchivo, ListaCuentas):
    #Guardar todos los datos de las cuentas que se encuentren en el programa
    with open(nombreArchivo,'w', newline='') as archivo:
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerow(("Nombre de cuenta", "Dinero Ahorrado", "Dinero Disponible"))
        for x in ListaCuentas:
            archivo_csv.writerow((x.name, x.ahorro, x.gastable))

def abrirCuentas(nombreArchivo, accountList):
    #Utilizado para leer las cuentas que ya existen
    with open('data.csv') as file:
        reader = csv.reader(file)
        item = next(reader, None)
        item = next(reader, None) #Saltearse los encabezados.

        while item:
            name = str(item[0])
            account = Account(name)
            account.ahorro = item[1]
            account.gastable = item[2]
            accountList.append(account)
            item = next(reader, None)





