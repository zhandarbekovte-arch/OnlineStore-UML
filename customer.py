from shopping_cart import ShoppingCart
from order import Order
from payment import Payment

class Customer:
    def __init__(self, cid, name, email):
        self.id = cid
        self.name = name
        self.email = email
        self.cart = ShoppingCart()

    def add_to_cart(self, product, qty):
        self.cart.add_item(product, qty)

    def place_order(self):
        order = Order(oid=self.id * 1000, items=self.cart.items)
        Payment(order.id, order.total).pay()
        return order
