class Transaccion:
    # The objective of this, is to create a "transaction" object

    def __init__(self, category, description, amount, date):
        self.category = category
        self.description = description
        self.amount = amount
        self.date = date


class Gasto(Transaccion):
    # Expendable object
    pass


class Ingreso(Transaccion):
    # Income object
    pass
