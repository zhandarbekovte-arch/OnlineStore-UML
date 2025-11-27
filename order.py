class Order:
    def __init__(self, oid, items):
        self.id = oid
        self.items = items
        self.total = self.calculate_total()

    def calculate_total(self):
        return sum(item.get_subtotal() for item in self.items)
