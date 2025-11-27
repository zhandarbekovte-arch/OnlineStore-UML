from shopping_cart import ShoppingCart
from order import Order
from payment_method import PaymentMethod

class Customer:
    def __init__(self, cid, name, email):
        self.id = cid
        self.name = name
        self.email = email
        self.cart = ShoppingCart()

    def add_to_cart(self, product, qty):
        self.cart.add_item(product, qty)

    def place_order(self, payment: PaymentMethod):
        order = Order(self.id * 1000, self.cart.items)
        payment.pay(order.total)
        return order
