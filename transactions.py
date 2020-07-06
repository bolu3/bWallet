class Transaccion:

    def __init__(self, categoria, descripcion, monto, fecha):
        self.categoria = categoria
        self.descripcion = descripcion
        self.monto = monto
        self.fecha = fecha


class Gasto(Transaccion):
    pass


class Ingreso(Transaccion):
    pass
