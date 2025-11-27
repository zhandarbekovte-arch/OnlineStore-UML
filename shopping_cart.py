from cart_item import CartItem

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, qty):
        self.items.append(CartItem(product, qty))

    def remove_item(self, product):
        self.items = [i for i in self.items if i.product.id != product.id]

    def get_total(self):
        return sum(item.get_subtotal() for item in self.items)
