from transacciones import Ingreso
from transacciones import Gasto


class Account:
    # Representation of an Account

    def __init__(self, name, ahorro=0, gastable=0, transaccionList=None):
        # Constructor de una cuenta

        self.name = name
        self.ahorro = ahorro
        self.gastable = gastable
        if transaccionList is None:
            transaccionList = []
        self.transaccionList = transaccionList

    def addIngreso(self, ingreso):
        # Agregar un ingreso a la cuenta cuenta
        taxdeahorro = 1
        self.transaccionList.append(ingreso)  # Suma un ingreso a la lista de transacciones
        self.ahorro += ingreso.monto * taxdeahorro  # Suma una cantidad X de plata al atributo de ahorro
        self.gastable += ingreso.monto * (1 - taxdeahorro)  # Suma una cantidad X de plata al atributo de gastable

    def getName(self):
        return self.name
