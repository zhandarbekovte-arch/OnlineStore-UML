class Product:
    def __init__(self, pid, name, price):
        self.id = pid
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name} - {self.price}₸"
