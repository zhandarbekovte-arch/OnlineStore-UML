class Order:
    def __init__(self, oid, items):
        self.id = oid
        self.items = items
        self.total = self.calculate_total()

    def calculate_total(self):
        return sum(i.get_subtotal() for i in self.items)
