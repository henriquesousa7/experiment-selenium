class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return 'Product name: ' + self.name + ', Price' + self.price


