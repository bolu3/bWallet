from account import Account
import transacciones
import csv

def guardarCuentas(nombreArchivo, ListaCuentas):
    #Guardar todos los datos de las cuentas que se encuentren en el programa
    with open(nombreArchivo,'w', newline='') as archivo:
        archivo_csv = csv.writer(archivo)
        for x in ListaCuentas:
            archivo_csv.writerow([x.name])

def abrirCuentas(nombreArchivo, accountList):
    #Utilizado para cargar las cuentas que ya existen
    with open('data.csv') as file:
        reader = csv.reader(file)
        item = next(reader, None)

        while item:
            name = str(item[0])
            account = Account(name)
            accountList.append(account)
            item = next(reader, None)
            
            
def abrirTransacciones(nombreArchivo, account):
    #Función para cargar los transacciones de una cuenta en particular
    with open("%sTransacciones.csv" % account.name ) as file:
        reader = csv.reader(file)
        item = next(reader, None)

        while item:
            categoria = item[0]
            descripcion = item[1]
            monto = int(item[2])
            fecha = item[3]

            if monto > 0:
                ingreso = transacciones.Ingreso(categoria, descripcion, monto, fecha)
                account.transaccionList.append(ingreso)
            else:
                gasto = transacciones.Gasto(categoria,descripcion,monto,fecha)
                account.transaccionList.append(gasto)

            item = next(reader, None)

def abrirStatus(nombreArchivo, account):
    with open(nombreArchivo) as file:
        reader = csv.reader(file)
        status = next(reader, None)
        account.gastable = status[0]
        account.ahorro = status[1]
        
            





