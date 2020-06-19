from transacciones import Ingreso
from transacciones import Gasto
from funcionesGenerales import verificacion, verificacionFloat
import csv


class Account:
    # Representation of an Account

    def __init__(self, name, ahorro = 0, gastable = 0, transaccionList=None):
        # Constructor de una cuenta

        self.name = name
        self.ahorro = ahorro
        self.gastable = gastable
        if transaccionList is None:
            transaccionList = []
        self.transaccionList = transaccionList


    def addGasto(self):
        #Agregar un Gasto en una cuenta determinada.

        categoria = input("Ingrese la categoria del gasto: ")
        descripcion = input("Breve descripcion del gasto: ")
        monto = verificacion("Monto: ")
        fecha = verificacion("probando fecha:")

        gasto = Gasto(categoria, descripcion, monto, fecha)
        self.transaccionList.append(gasto)

        self.gastable = int(self.gastable) #Tengo que cambiarlo, ya que me lo devuelve como string.. todavía no se porque

        self.gastable -= monto #Actualiza la cantidad de dinero gastable de dicha cuenta

        guardarTransacciones("%s.csv" % self.name ,gasto)

    def addIngreso(self):
        # Agregar un ingreso a la cuenta cuenta

        categoria = input("Ingrese la categoria del ingreso: ")
        descripcion = input("Breve descripcion del ingreso: ")
        monto = verificacion("Monto: ")
        fecha = verificacion("probando fecha: ")

        ingreso = Ingreso(categoria, descripcion, monto, fecha)
        self.transaccionList.append(ingreso) # Suma un ingreso a la lista de transacciones


        taxdeahorro = verificacionFloat("Porcentaje del sueldo a ahorrar: ") 
        taxdeahorro /= 100

        self.ahorro = int(self.ahorro) #Este también me lo devuelve como string y no se porque..
        self.gastable = int(self.gastable) #Tengo que cambiarlo, ya que me lo devuelve como string.. todavía no se porque


        self.ahorro += ingreso.monto * taxdeahorro  # Suma una cantidad X de plata al atributo de ahorro
        self.gastable += ingreso.monto * (1 - taxdeahorro)  # Suma una cantidad X de plata al atributo de gastable

        guardarTransacciones("%s.csv" % self.name,ingreso)

    def getName(self):
        return self.name
    
def guardarTransacciones(nombreArchivo, transaccion):
    with open(nombreArchivo, 'a') as archivo:
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerow((type(transaccion),transaccion.categoria,transaccion.descripcion,transaccion.monto,transaccion.fecha))
  
